import streamlit as st, time, json, boto3, graphviz
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
from openai import AzureOpenAI
from streamlit_geo_helper import *
from get_supplement_text_vrs import *

azure_client = AzureOpenAI(
  api_key = "your_api_key",        
  api_version = "2024-02-15-preview",                  
  azure_endpoint = "your_api_endpoint"
)

with open(r"aws_key.json", 'r', encoding='utf-8') as file:
    all_keys = json.load(file)
    bedrock_client = boto3.client( service_name="bedrock-runtime",
                                    aws_access_key_id = all_keys['aws_access_key_id'],
                                    aws_secret_access_key = all_keys['aws_secret_access_key'],
                                    aws_session_token = all_keys['aws_session_token'],
                                    region_name="us-east-1",
                                    verify = False
                                    )
    print("OK")
    
credits_card_data = pd.read_excel("all_credit_cards.xlsx")
json_data = credits_card_data.set_index('card_name').to_dict(orient='index')
json_str = json.dumps(json_data)

st.set_page_config(layout="wide")
# Tiêu đề cho ứng dụng
st.markdown("""
    <style>
        .title {
            background: linear-gradient(to right, #E0FFFF, #00FFFF);  /* Light cyan gradient */
            -webkit-background-clip: text;
            color: transparent;
            font-size: 40px;  /* Adjust the font size as needed */
            font-weight: bold;
        }
    </style>
    <h1 class="title"> Card-banking recommendation </h1>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Chọn trang", ("Trang 1", "Trang 2", "Trang 3", "Trang 4", "Trang 5", "Trang 6"))

# Trang 1
if page == "Trang 1":
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #87CEFA, #1E90FF);  /* Light sky blue to ocean blue gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 30px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang1">Trang 1: Dataset description </h1>
    """, unsafe_allow_html=True) 
            
    r11, r12 = st.columns(2)        
    with r11:
        st.markdown("#### User Information")
        # Add CSS for styling: font-size, text wrapping, and header alignment
        st.markdown("""
            <style>
            table {
                font-size: 14px !important;  /* Set font size for the entire table */
                border-collapse: collapse;
                width: 100%;
            }
            table td, table th {
                padding: 5px;
                white-space: normal !important;
                word-wrap: break-word;
                overflow-wrap: break-word;
            }
            table th {
                text-align: center !important;  /* Center-align table headers */
                background-color: #FFCCCC;  /* Green background color for headers */
                color: black
            }
            </style>
            """, unsafe_allow_html=True)        
        df = pd.DataFrame({
            'cols': ['user_id', 'dob', 'age-group', 'gender', 'income-level', 'emp_idx'],
            'type': ['string', 'datetime', 'categorical', 'categorical', 'categorical', 'categorical'],
            'description': ['Unique identifier for each user (customer)', 'date of birth', 'inferred from dob to understand demographic preferences.', 
                            'E.g., male or female; for targeted recommendations.', 'Income bracket of the user (e.g., low, medium, high) to tailor product offerings.',
                            'Employee-index (e.g, active / ex employed /  filial / not employee / pasive)'
                            ]
        })
        html = df.to_html(escape=False, index=False)
        st.markdown(html, unsafe_allow_html=True)
        
    with r12:
        st.markdown("#### User preference & interaction")
        df = pd.DataFrame({
           'cols': ['n-transactions', 'amount', 'ratings', 'credit_score', 'product-type', 'transaction_history'],
           'type': ['int', 'int', 'int', 'int', 'category', 'string'],
           'description': ['number of transactions', 
                           "Amount of money for all transaction",
                           "User's rating for each credit card (e.g., from 1 to 5) to capture user satisfaction.",
                           "User’s credit score, which is crucial for determining eligibility for certain cards.",
                           "Type of banking product (e.g., credit card, loan) to categorize offerings.",
                           "Summary of past transactions or interactions with financial products, which can be used to analyze spending habits."
                           ]
        })
 
        # Hiển thị bảng dưới dạng HTML
        html = df.to_html(escape=False, index=False)
        st.markdown(html, unsafe_allow_html=True)
                
    r21, r22= st.columns([3, 5])
    with r21:    
        st.markdown("#### Card details")
        product_type = st.selectbox("Product-type", ["Credit-cards", "Payment-cards"])
        if product_type == "Credit-cards":
            card_type = st.selectbox("Select type of credit-cards", ("VIB Cash Back", "VIB Premier Boundless", "VIB Travel Élite", "VIB Rewards Unlimited", "VIB Online Plus 2in1",
                                                                    "VIB Family Link", "VIB Financial Free", "VIB LazCard", "VIB Ivy Card", "VIB Super Card"))
        elif product_type == "Payment-cards":
            card_type = st.selectbox("Select type of payment-cards", ("Thẻ thanh toán toàn cầu VIB Ivy Card", 
                                                                      "Thẻ thanh toán VIB Online Plus 2in1",
                                                                      "Thẻ thanh toán toàn cầu VIB Platinum",
                                                                      "Thẻ thanh toán toàn cầu VIB iCard",
                                                                      "Thẻ thanh toán VIB LazCard",
                                                                      "Thẻ thanh toán nội địa VIB Values (ATM)"))
        st.markdown("#### Cards information")
        df = pd.DataFrame({
            'cols': ['card_id', 'card_type', 'card_name', 'annual_fee', 'reward_rate', 'is_cashback', 'is_low_interest', 
                    'for_shopping', 'for_food', 'for_entertainment', 'for_insurance', 'for_education'],
            'type': ['string', 'string', 'string', 'float', 'float', 'bool', 'bool', 
                    'bool', 'bool', 'bool', 'bool', 'bool'],
            'description': [
                'Unique identifier for each credit card, 12 digits.',
                'Type of banking card (e.g., credit card, loan) to categorize offerings',
                'Name of the credit card (e.g., "VIB Online Plus 2in1", "VIB Ivy Card", "VIB Cash Back").',
                'Annual fee associated with the credit card.',
                'Reward rate offered by the card (e.g., cashback percentage).',
                'Indicates if the card offers cashback rewards (True/False).',
                'Indicates if the card offers low interest rates (True/False).',
                'Indicates if the card is suitable for shopping purchases (True/False).',
                'Indicates if the card is suitable for food-related purchases (True/False).',
                'Indicates if the card is suitable for entertainment purchases (True/False).',
                'Indicates if the card is suitable for insurance purchases (True/False).',
                'Indicates if the card is suitable for education-related purchases (True/False).'
            ]
        })
        html = df.to_html(escape=False, index=False)
        st.markdown(html, unsafe_allow_html=True)
        
    with r22:
        st.markdown("#### Features")        
        json_dict = get_json_card_info(card_type)
        st.json(json_dict)
        
elif page == "Trang 2":
    st.markdown("""
        <style>
            .title-trang2 {
                background: linear-gradient(to right, cyan, violet);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 29px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang2"> Trang 2: Overview credit-card data </h1>
    """, unsafe_allow_html=True)    
    card_list = credits_card_data["card_name"].values.tolist()
    c1, c2 = st.columns([1, 3])
    with c1:
        compare = st.checkbox("Wanna compare?")        
        if compare:  # If the user wants to compare, show two selectboxes
            st.markdown("""
            <style>
                .stCheckbox .st-bx > label {
                    color: blue;
                    font-weight: bold;
                }
            </style>
            """, unsafe_allow_html=True)
            sel_card_name = st.selectbox("Select the first credit card name", card_list)
            sel_card_compare = st.selectbox("Select the second credit card name to compare", card_list)
        else:  # If not, show only one selectbox
            st.markdown("""
            <style>
                .stCheckbox .st-bx > label {
                    color: red;
                    font-weight: bold;
                }
            </style>
            """, unsafe_allow_html=True)
            sel_card_name = st.selectbox("Select the credit card name", card_list)
            sel_card_compare = None  # No second card selected
    with c2:
        multiple_col = st.multiselect("Select columns to display", credits_card_data.columns.tolist(), default=credits_card_data.columns.tolist())
    
    df = credits_card_data.loc[credits_card_data['card_name'].isin([sel_card_name, sel_card_compare]), multiple_col].set_index('card_name').T
    html = df.to_html(escape=False)
    st.markdown("""
        <style>
        table {
            font-size: 14px !important;  /* Set font size for the entire table */
            border-collapse: collapse;
            width: 100%;
        }
        table td, table th {
            padding: 5px;
            white-space: normal !important;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }
        table th {
            text-align: center !important;  /* Center-align table headers */
            background-color: gray;  /* Gray background color for headers */
            color: black
        }
        </style>
        """, unsafe_allow_html=True)          
    st.markdown(html, unsafe_allow_html=True)

elif page == "Trang 3":
    st.markdown("""
        <style>
            .title-trang3 {
                background: linear-gradient(to right, violet, #4682B4);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 29px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang3"> Trang 3: Credit-card recommender </h1>
    """, unsafe_allow_html=True)    

    def gpt_analytic(client, text, max_tokens, temperature, top_p):
        explaination_here = get_credit_cards_CoT()
        pre_defined_message = f"""
        You are a professional virtual asistant at VIB, your task will be consultant any customer which credit-card they must use, below is your credit-cards information:
        {json_str}
        {explaination_here}      
        .................................................................
        Remember, your response must be clarify, shorten such that not exceeded {max_tokens} token
        .................................................................
        Now, you will get the user-information 
        {text}
        ................................................................
        The answers MUST be in VIETNAMESE        
        """

        response = client.chat.completions.create(
            model="intbot-prod-gpt-4o",
            messages=[{"role":"system","content": pre_defined_message}, 
                    {"role":"user","content":"---\nYOUR_QUESTION\nOutput:\n"}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        answers =  response.choices[0].message.content.replace('\n"','"')
        num_tokens = len(pre_defined_message.split())
        return answers, num_tokens

    def haiku_chat(message_content, max_tokens, temperature, top_p):
        explaination_here = get_credit_cards_CoT()
        pre_defined_message = f"""
        You are a professional virtual asistant at VIB, your task will be consultant any customer which credit-card they must use, below is your credit-cards information:
        {json_str}
        {explaination_here}
        .................................................................
        Remember, your response must be clarify, shorten such that not exceeded {max_tokens} token        
        .................................................................
        Now, you will get the user-information 
        {message_content}
        ................................
        In the output, please state:
            - The requirements of the card you suggest (minimum income, credit conditions),
            - As well as its features (cashback or not, credit limit, annual fees, etc.), and summarize it briefly.
        The answers MUST be in VIETNAMESE
        """    
        messages = [{
            "role": "user",
            "content": [{"text": pre_defined_message}]
        }]
        
        response = bedrock_client.converse(
            modelId= "anthropic.claude-3-haiku-20240307-v1:0", # "anthropic.claude-3-5-haiku-20241022-v1:0",
            messages=messages,
            system=[{"text":pre_defined_message}],
            inferenceConfig={
                "maxTokens": max_tokens,
                "temperature": temperature,
                "topP": top_p
            }
        )

        output_message = response['output']['message']['content'][0]['text']
        num_tokens = len(pre_defined_message.split())
        
        return output_message, num_tokens

    # Select your parameters
    p1, _, p2, _, p3 = st.columns(5)
    with p1:
        max_tokens = st.slider("Max-tokens", min_value=256, max_value=512)
        if max_tokens < 500:
            a_height = 450
        else:
            a_height = 900
    with p2:
        temperature = st.slider("Temperature", min_value=0.01, max_value=0.999)
    with p3:
        top_p = st.slider("Top_p", min_value=0.0, max_value=1.0)
                
    your_request = st.text_area(label="Enter your question here", height=120)
    
    c1, c2 = st.columns(2)
    with c1:
        #st.text_area("GPT response", value=gpt_analytic(azure_client, your_request, max_tokens, temperature, top_p), height=a_height)
        st.subheader("GPT responses")
        t0 = time.time()
        response, n_tokens = gpt_analytic(azure_client, your_request, max_tokens, temperature, top_p)
        st.write(response)
        st.write(f"Elappsed time: {(time.time() - t0):.2f} seconds")
        st.write(f"Prompt-tokens: {n_tokens}")        
    with c2:
        #st.text_area("Haiku response", haiku_chat(your_request, max_tokens, temperature, top_p), height=a_height)
        st.subheader("Haiku response")
        t0 = time.time()
        response, n_tokens = haiku_chat(your_request, max_tokens, temperature, top_p)
        st.write(response)
        st.write(f"Elappsed time: {(time.time() - t0):.2f} seconds")
        st.write(f"Prompt-tokens: {n_tokens}")
        
elif page == "Trang 4": 
    st.markdown("""
        <style>
            .title-trang4 {
                background: linear-gradient(to right, #FFCCCC, #FF6666);
                -webkit-background-clip: text;
                color: transparent;
                font-size: 30px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang4"> Trang 4: Flow Architecture of Credit Card Recommendation System </h1>
    """, unsafe_allow_html=True)    
    st.write("Below is the flow architecture illustrating how the chatbot returns the credit cards that best match your provided information.")

    a1, a2 = st.columns([1, 4])
    with a1:
        st.write("#### Recommender function")
    with a2:  
        # Create a flowchart
        flowchart = graphviz.Digraph(format='png', engine='dot', graph_attr={'rankdir': 'LR'})
        
        # Define nodes and edges
        flowchart.node('A', 'Web.scraper credit-cards info \n 10 cards only', shape='box')
        flowchart.node('B', 'Cleansing data', shape='box')
        flowchart.node('C', 'Write to json \n or xlsx file', shape='box')
        flowchart.node('D', 'Bedrock AWS \n or OpenAI azure', shape='box')
        flowchart.node('E', 'get response', shape='box')

        flowchart.edges(['AB', 'BC', 'CD', 'DE'])
        flowchart.edge('B', 'D', label='prompting')

        # Render the flowchart in Streamlit
        st.graphviz_chart(flowchart)    
        
    c1, c2 = st.columns(2)
    with c1:
        fig1 = get_chart_avg(credits_card_data)
        st.plotly_chart(fig1)
    with c2:
        fig2 = get_chart_cnt(credits_card_data)
        st.plotly_chart(fig2)
            
elif page == "Trang 5":
    st.markdown("""
        <style>
            .title-trang5 {
                background: linear-gradient(to right, red, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 29px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang5"> Page 5: Fun with New Year's Resolution </h1>
    """, unsafe_allow_html=True)
    st.write("""
            The first 4 pages of this web will support you find the credit-cards that fit the most to you, from this page, it is for entertaiment and education, so ignore or drop this out \n
            
            All of these pages belongs to NhanDov : https://github.com/NhanDoV
            
            Welcome to the New Year's Resolution Game!
            Let's reflect on the achievements of the past year and set exciting goals for the year ahead. 
        """)
    # Create columns for "This Year" (completed tasks) and "Next Year" (new tasks)
    col1, _, col2 = st.columns([3,1,3])
    with col1:
        # Define how many tasks to create for this year
        st.write("### This Year")
        n_tasks = st.selectbox("Select number of targets this year", (2, 3, 4, 5, 6, 7, 8))
        col_11, col_12 = st.columns([2, 1])  # Adjust column widths for task input
        tasks = {}

        # Create input fields for tasks and checkboxes for completion status
        for i in range(n_tasks + 1):
            if i == 0:
                with col_11:
                    st.write("##### Tasks")
                with col_12:
                    st.write("##### Completed or not?")
            else:
                with col_11:
                    task_name = st.text_input(f"Task {i}", key=f"task_name_{i}")            
                with col_12:
                    # Use a unique key for each selectbox to avoid duplication
                    is_finish = st.selectbox(f"Is Task {i} completed?", (True, False), key=f"task_checkbox_{i}")
                    
                # Store task name and completion status
                tasks[task_name] = is_finish

    with col2:
        # Define how many goals to create for next year
        st.write("### Goals for Next Year")
        n_goals = st.selectbox("Select number of goals for next year", (2, 3, 4, 5, 6, 7, 8))        
        col_21, col_22 = st.columns([2, 1])  # Adjust column widths for goals input
        goals = {}

        # Create input fields for goals (no completion checkbox for goals)
        for i in range(n_goals + 1):
            if i == 0:
                with col_21:
                    st.write("##### Goals")
            else:
                with col_21:
                    goal_name = st.text_input(f"Goal {i}", key=f"goal_name_{i}")
                
                # Store goal name
                if goal_name:
                    goals[goal_name] = "Not Completed Yet"

    # Add one submit button below the inputs
    import random
    
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds spacing before the button
    if st.button("Submit All Tasks and Goals", key="submit_button"):
        # Left column: Filter out completed tasks (those marked as True)
        incomplete_tasks = {task: status for task, status in tasks.items() if not status}

        # Combine incomplete tasks and new goals
        all_tasks_and_goals = list(incomplete_tasks.keys()) + list(goals.keys())

        # Generate random predicted success percentages for each task/goal
        predictions = [random.randint(50, 100) for _ in range(len(all_tasks_and_goals))]

        # Create a DataFrame with the results
        df = pd.DataFrame({
            "Task/Goal": all_tasks_and_goals,
            "Completion Status": ["Incomplete"] * len(incomplete_tasks) + ["Not Completed Yet"] * len(goals),
            "Predicted Success (%)": predictions
        })

        # Display the DataFrame
        st.write("### Here's your summary:")
        html = df.to_html(escape=False, index=False)
        st.markdown("""
            <style>
            table {
                font-size: 14px !important;  /* Set font size for the entire table */
                border-collapse: collapse;
                width: 100%;
            }
            table td, table th {
                padding: 5px;
                white-space: normal !important;
                word-wrap: break-word;
                overflow-wrap: break-word;
            }
            table th {
                text-align: center !important;  /* Center-align table headers */
                background-color: #FFCCCC;  /* Green background color for headers */
                color: black
            }
            </style>
            """, unsafe_allow_html=True)        
         
        st.markdown(html, unsafe_allow_html=True)
        
else:
    
    relax_game = st.selectbox("Choose the topic to relax", ("math-quizz", "funny/scary-stories", "thơ ca nhảm địtz"))
    if relax_game == "funny/scary-stories":
        st.markdown("""
            <style>
                .title-trang6 {
                    background: linear-gradient(to right, #B2FF66, #32CD32);  /* Lime green gradient */
                    -webkit-background-clip: text;
                    color: transparent;
                    font-size: 27px;  /* Adjust the font size as needed */
                    font-weight: bold;
                }
            </style>
            <h1 class="title-trang6"> Page 6: Fun story in free-time </h1>
        """, unsafe_allow_html=True)
        
        def story_teller(client, text, max_tokens, temperature, top_p):
            examples = story_teller_examples()
            pre_defined_message = f"""
            - Bạn là một người kể chuyện tài ba, lỗi lạc, và văn phong chuẩn mực. Các tác phẩm của bạn thường là những tác phẩm ngắn, những tiểu phẩm chỉ tầm 100-200 words nhưng rất cô đọng, ý nghĩa và nhân văn
            - Các dòng tác phẩm của bạn chủ yếu gồm các thể loại như 
                * truyện ngắn kinh dị:
                * truyện cười:
                * truyện tình buồn:
                * các câu ngắn truyền cảm hứng: 
            - Dưới đây là một số ví dụ, nếu có tham khảo rồi hãy thay đổi để nó rùng rợn hơn (truyện kinh dị) hoặc xúc tích hơn
            {examples}
            .................................................................
            Bây giờ, bạn sẽ nhận được yêu cầu: {text}
            ................................................................
            Kết quả trả ra phải là dạng json-dictionary và không chứa bất kỳ string nào khác trước đó
            """

            response = client.chat.completions.create(
                model="intbot-prod-gpt-4o",
                messages=[{"role":"system","content": pre_defined_message}, 
                        {"role":"user","content":"---\nYOUR_QUESTION\nOutput:\n"}],
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            json_string =  response.choices[0].message.content.replace('\n"','"').replace('\n}','}')
            cleaned_json_string = json_string.replace('```json\n', '').replace('```', '')
            num_tokens = len(pre_defined_message.split())
            return json.loads(cleaned_json_string), num_tokens
        
        p1, _, p2, _, p3 = st.columns(5)
        with p1:
            max_tokens = st.slider("Max-tokens", min_value=256, max_value=784)
        with p2:
            temperature = st.slider("Temperature", min_value=0.01, max_value=0.999)
        with p3:
            top_p = st.slider("Top_p", min_value=0.0, max_value=1.0)
            
        input_req = st.text_input("Nhập yêu cầu của bạn ở đây")    
        c1, c2 = st.columns([4, 1])
        with c1:
            st.subheader("Result")
            t0 = time.time()
            js_output, num_tokens = story_teller(azure_client, input_req, max_tokens, temperature, top_p)
            st.json(js_output)
        with c2:
            st.subheader("Performance & Token Usage")
            st.write(f"Ellapsed time: {(time.time() - t0):.2f} seconds")
            st.write(f"n_input tokens: {num_tokens} ")
    elif relax_game == "thơ ca nhảm địtz":
        st.markdown("""
            <style>
                .title-trang6 {
                    background: linear-gradient(to right, #FFB84D, #D17F34);  /* Light orange to brownish-orange gradient */
                    -webkit-background-clip: text;
                    color: transparent;
                    font-size: 27px;  /* Adjust the font size as needed */
                    font-weight: bold;
                }
            </style>
            <h1 class="title-trang6"> Page 6: Relax with funny poem </h1>
            """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns([2, 3, 2])
        
        def poem_generator(client, text):
            examples_68 = get_poem68_examples()
            examples_7w = get_poem7w_examples()
            examples_fr = get_freestyle_poem_samples()
            
            pre_defined_message = f"""
            Bạn là một nhà sáng tác thơ với 3 thể loại chính:
            - lục bát
                <requirements>
                    - là bài thơ gồm số câu là số chẵn, cứ mỗi 2 câu sẽ ghép thành một cặp (câu 6 chữ và câu 8 chữ)
                        Luật bằng trắc
                            Câu 6 chữ: Tiếng 1-Bằng-Tiếng 3-Trắc-Tiếng 5-Bằng
                            Câu 8 chữ: Tiếng 1-Bằng-Tiếng 3-Trắc-Tiếng 6-Bằng-Tiếng 7-Bằng.
                        Luật ngắt quãng
                            Câu 6 chữ: 2 / 2 / 2 hoặc 3 / 3
                            Câu 8 chữ: 2/2/2/2 hoặc 4 / 4
                    - từ cuối trong câu 6 từ sẽ có cùng vần với từ 6 trong câu 8 từ. Xem các ví dụ dưới đây
                    - ý tứ các câu phải có nghĩa và liên kết rõ ràng
                    <examples>
                        {examples_68}
                    </examples>              
                        - Trong example_1, từ "cao" trong câu 6 chữ có cùng vần với từ "sao" trong câu 8 chữ
                        - Ở example_2, tương tự ta có "ta" trong câu 6 chữ cùng vần với "là" trong câu 8 chữ
                </requirements>
            - thất ngôn
                <requirements>
                    - là thể thơ mỗi câu có 7 chữ, thường sẽ gieo thành cặp 2 câu 7 chữ hoặc 4 câu 7 chữ
                        Luật ngắt quãng : 2 / 2 / 3 hoặc đôi lúc có thể là 4 / 3
                        Luật vần:
                            Luật bằng trắc của thơ thất ngôn bát cú hoặc thơ tứ tuyệt luật Đường thường được tóm gọn bằng câu: “nhất – tam – ngũ bất luận, nhị – tứ - lục phân minh”, tức là các tiếng (âm tiết) thứ nhất, thư ba, thứ năm trong câu không cần sắp xếp theo đúng luật bằng/ trắc; còn các tiếng thứ hai, thứ tư, thứ sáu trong câu cần tuân theo luật bằng/ trắc rõ ràng. 
                            Nếu tiếng thứ hai của câu 1 là tiếng thanh bằng (thanh ngang hoặc thanh huyền) thì bài thơ được làm theo luật bằng. Nếu tiếng thứ hai của câu 1 là tiếng thanh trắc (các thanh sắc, hỏi, ngã, nặng) thì bài thơ được làm theo luật trắc
                    <examples>
                        {examples_7w}
                    </examples>
                </requirements>            
            - tự do
                <requirements>
                    - là thể thơ tự do không bị ràng buộc bởi các luật về bằng trắc nhưng vẫn phải tuân theo luật về vần và các câu liên kết sao cho có ý nghĩa
                    - dưới đây là các thể loại thơ tự do
                    <examples>
                        {examples_fr}
                    </examples>                
                </requirements>            
            .................................................................
            Bây giờ, bạn sẽ nhận được yêu cầu: {text}
            ................................................................
            Kết quả trả ra phải là dạng json-dictionary và không chứa bất kỳ string nào khác trước đó
            """

            response = client.chat.completions.create(
                model="intbot-prod-gpt-4o",
                messages=[{"role":"system","content": pre_defined_message}, 
                        {"role":"user","content":"---\nYOUR_QUESTION\nOutput:\n"}],
                temperature=0.2,
                max_tokens=256,
                top_p=0.99,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            json_string =  response.choices[0].message.content.replace('\n"','"').replace('\n}','}')
            cleaned_json_string = json_string.replace('```json\n', '').replace('```', '')
            num_tokens = len(pre_defined_message.split())
            return json.loads(cleaned_json_string), num_tokens        
        
        with c1:            
            input_req = st.text_input("Nhập chủ đề yêu cầu của bạn ở đây")
            t0 = time.time()
            submit_button = st.button("Play")
            
            if submit_button:
                js_output, n_tokens = poem_generator(azure_client, input_req)
                poem_type = js_output["thể loại"]
                poem_res = js_output["sample"]
                poem_formated = poem_res.replace(".", ".<br>")                
                with c2:
                    st.write("#### Result")
                    st.markdown(poem_formated, unsafe_allow_html=True)                
                with c3:
                    ans = "" # your function here            
                    st.subheader("Performance & Token Usage")
                    st.write(f"Ellapsed time: {(time.time() - t0):.2f} seconds")
                    st.write(f"n_input tokens: {n_tokens} ")
                    st.write(f"thể thơ: {poem_type}")         

        if submit_button:
            js_output["request"] = input_req 
            st.subheader("Logs")
            st.json(js_output)
    
    elif relax_game == "math-quizz":
        st.markdown("""
            <style>
                .title-trang6 {
                    background: linear-gradient(to right, #FFFFB2, #FFA500);  /* Light yellow to orange gradient */
                    -webkit-background-clip: text;
                    color: transparent;
                    font-size: 27px;  /* Adjust the font size as needed */
                    font-weight: bold;
                }
            </style>
            <h1 class="title-trang6"> Page 6: Quizz game puzzle in math </h1>
            """, unsafe_allow_html=True)
        c1, _, c2, _, c3 = st.columns([6, 1, 8, 1, 10])
        with c1:
            math_topic = st.selectbox("Chọn chủ đề", ("Hình học", "Phương trình lượng giác", "Tập hợp - chuỗi số - hàm số", "Ma trận", 
                                                      "Xác suất Thống kê", "Tích phân đạo hàm", "Logical - brain teaser", "Algorithms"))
            levels = st.selectbox("Chọn cấp độ thử thách", ("Dễ", "Trung bình", "Khó"))
            quiz_num = get_quiz_num(math_topic, levels)                                                                              

        import seaborn as sns
        sns.set_theme(style="whitegrid")
        
        if math_topic == "Hình học":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        question_hinh_hoc_1_easy()
                        submit_button = st.button("See the answers")
                        if submit_button:
                            fig = illustration_hinh_hoc_1_easy()
                            st.pyplot(fig)                        
                            with c3:
                                solution_hinh_hoc_1_easy()
                            
            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        question_hinh_hoc_1_medium()
                        submit_button = st.button("See the answers")
                        if submit_button:
                            fig = illustration_hinh_hoc_1_medium()
                            st.pyplot(fig)                        
                            with c3:
                                solution_hinh_hoc_1_medium()
                                                        
                elif quiz_num == "câu 2":
                    with c2:
                        question_hinh_hoc_2_medium()
                        submit_button = st.button("See the answers")
                        if submit_button:                    
                            fig = illustration_hinh_hoc_2_medium()
                            st.pyplot(fig)                    
                            with c3:
                                solution_hinh_hoc_2_medium()
                                                                
            else:
                if quiz_num == "câu 1":
                    with c2:
                        question_hinh_hoc_1_hard()
                        submit_button = st.button("See the answers")
                        if submit_button:
                            fig = cube_inside_cube_plot()                        
                            st.pyplot(fig)
                            additional_explaination()
                            with c3:
                                if submit_button:
                                    solution_hinh_hoc_1_hard()
                                                                                                            
                elif quiz_num == "câu 2":
                    with c2:
                        question_hinh_hoc_2_hard()
                        submit_button = st.button("See the answers")
                        if submit_button:
                            fig1 = illustration_hinh_hoc_2_hard()
                            fig2 = illustration_hinh_hoc_2_hard_projection()
                            st.pyplot(fig2)
                            st.pyplot(fig1)
                            with c3:
                                solution_hinh_hoc_2_hard()
                                                                            
                elif quiz_num == "câu 3":
                    with c2:
                        question_hinh_hoc_3_hard()
                        fig = illustration_hinh_hoc_3_hard()
                        st.pyplot(fig)
                        submit_button = st.button("See the answers")
                    with c3:
                        if submit_button:
                            solution_hinh_hoc_3_hard()
                            
        elif math_topic == "Phương trình lượng giác":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_trigonometric_1_easy()
                    with c3:
                        if submit_button:
                            solution_trigonometric_1_easy()
                            
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_trigonometric_2_easy()
                    with c3:
                        if submit_button:
                            solution_trigonometric_2_easy()                            
                            fig = illustration_trigonometric_2_easy()
                            st.pyplot(fig)

            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_trigonometric_1_medium()                        
                        fig = illustration_trigonometric_1_medium()
                        st.pyplot(fig)
                    with c3:
                        if submit_button:
                            solution_trigonometric_1_medium()
                                                    
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_trigonometric_2_medium()
                    with c3:
                        if submit_button:
                            solution_trigonometric_2_medium()
                            
            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_trigonometric_1_hard()
                        fig = illustration_trigonometric_1_hard()
                        st.pyplot(fig)                                     
                    with c3:
                        if submit_button:                           
                            solution_trigonometric_1_hard()
        
        elif math_topic == "Ma trận":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_matrix_1_easy()
                    with c3:
                        if submit_button:
                            solution_matrix_1_easy()        
                            
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_matrix_2_easy()
                    with c3:
                        if submit_button:
                            solution_matrix_2_easy()

            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_matrix_1_medium()       
                    with c3:
                        if submit_button:
                            solution_matrix_1_medium()
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_matrix_2_medium()       
                    with c3:
                        if submit_button:
                            solution_matrix_2_medium()
                                                                         
            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_matrix_1_hard()
                    with c3:
                        if submit_button:
                            solution_matrix_1_hard()

                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_matrix_2_hard()
                    with c3:
                        if submit_button:
                            solution_matrix_2_hard()
                                                                                                                                                                
        elif math_topic == "Xác suất Thống kê":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_StatsnProba_1_easy()
                        fig = illustration_StatsnProba_1_easy()
                        st.pyplot(fig)
                    with c3:
                        if submit_button:
                            solution_StatsnProba_1_easy()

                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_StatsnProba_2_easy()
                        if submit_button:
                            fig = illustration_StatsnProba_2_easy()
                            st.pyplot(fig)
                            with c3:
                                solution_StatsnProba_2_easy()

                elif quiz_num == "câu 3":
                    with c2:
                        submit_button = question_StatsnProba_3_easy()
                        if submit_button:
                            fig = illustration_StatsnProba_3_easy()
                            st.pyplot(fig)
                            solution_StatsnProba_3_easy_additional()
                            with c3:
                                solution_StatsnProba_3_easy()

                elif quiz_num == "câu 4":
                    with c2:
                        submit_button = question_StatsnProba_4_easy()
                        if submit_button:
                            fig = illustration_StatsnProba_4_easy()
                            st.pyplot(fig)
                            with c3:
                                solution_StatsnProba_4_easy()

                elif quiz_num == "câu 5":
                    with c2:
                        submit_button = question_StatsnProba_5_easy()
                        if submit_button:
                            with c3:
                                solution_StatsnProba_5_easy()                 

            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_StatsnProba_1_medium()
                        if submit_button:
                            fig = illustration_StatsnProba_1_medium()
                            st.pyplot(fig)
                            with c3:
                                solution_StatsnProba_1_medium()
                        
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_StatsnProba_2_medium()
                        if submit_button:
                            fig = illustration_StatsnProba_2_medium()
                            st.pyplot(fig)
                            with c3:
                                solution_StatsnProba_2_medium()

                elif quiz_num == "câu 3":
                    with c2:
                        submit_button = question_StatsnProba_3_medium()
                        
            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_StatsnProba_1_hard()
                    
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_StatsnProba_2_hard()
                    
                elif quiz_num == "câu 3":
                    with c2:
                        submit_button = question_StatsnProba_3_hard()

                elif quiz_num == "câu 4":
                    with c2:
                        submit_button = question_StatsnProba_4_hard()
                        if submit_button:
                            fig = illustration_StatsnProba_4_hard()
                            st.pyplot(fig)
                            with c3:
                                solution_StatsnProba_4_hard()
                    
                elif quiz_num == "câu 5":
                    with c2:
                        submit_button = question_StatsnProba_5_hard()

                elif quiz_num == "câu 6":
                    with c2:
                        submit_button = question_StatsnProba_6_hard()

        elif math_topic == "Tích phân đạo hàm":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_Calculus_1_easy()
                        fig = illustration_Calculus_1_easy()
                        st.pyplot(fig)
                    with c3:
                        if submit_button:
                            solution_Calculus_1_easy()
                
                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_Calculus_2_easy()
                        fig = illustration_Calculus_2_easy()
                        st.pyplot(fig)
                    with c3:
                        if submit_button:
                            solution_Calculus_2_easy()

            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_Calculus_1_medium()
                    with c3:
                        if submit_button:
                            solution_Calculus_1_medium()

            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_Calculus_1_hard()
        
        elif math_topic == "Logical - brain teaser":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_logical_1_easy()
                        if submit_button:
                            fig = illustration_logical_1_easy()
                            st.pyplot(fig)
                            with c3:
                                solution_logical_1_easy()

                elif quiz_num == "câu 2":
                    with c2:
                        submit_button = question_logical_2_easy()
                        if submit_button:
                            fig = illustration_logical_2_easy()
                            st.pyplot(fig)
                            with c3:
                                solution_logical_2_easy()
                                                   
            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_logical_1_medium()
                        if submit_button:
                            fig = illustration_logical_1_medium()
                            st.pyplot(fig)                            
                            with c3:
                                solution_logical_1_medium()
                        
                if quiz_num == "câu 2":
                    with c2:
                        submit_button = question_logical_2_medium()
                        if submit_button:
                            fig = illustration_logical_2_medium()
                            st.pyplot(fig)                            
                            with c3:
                                solution_logical_2_medium()
            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_logical_1_hard()
                        if submit_button:
                            fig = rule_of_2015_exponent()
                            st.pyplot(fig)
                            with c3:
                                solution_logical_1_hard()
                                                        
        elif math_topic == "Tập hợp - chuỗi số - hàm số":
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_numeric_serial_1_easy()
                    with c3:
                        if submit_button:
                            solution_numeric_serial_1_easy()
                            fig = illustration_numeric_serial_1_easy()
                            st.pyplot(fig)
                            
            elif levels == "Trung bình":
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_numeric_serial_1_medium()
                    with c3:
                        if submit_button:
                            solution_numeric_serial_1_medium()
                            fig = illustration_numeric_serial_1_medium()
                            st.pyplot(fig)
                            
            else:
                if quiz_num == "câu 1":
                    with c2:
                        submit_button = question_numeric_serial_1_hard()        
                    with c3:
                        if submit_button:
                            solution_numeric_serial_1_hard()
                            fig = illustration_numeric_serial_1_hard()
                            st.pyplot(fig)
                if quiz_num == "câu 2":
                    with c2:
                        submit_button = question_numeric_serial_2_hard()
                    with c3:
                        if submit_button:
                            solution_numeric_serial_2_hard()
                            fig = illustration_numeric_serial_2_hard()
                            st.pyplot(fig)                    

        else:                            
            if levels == "Dễ":
                if quiz_num == "câu 1":
                    with c2: 
                        submit_button = question_algorithm_1_easy()