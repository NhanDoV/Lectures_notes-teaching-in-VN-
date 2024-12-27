import streamlit as st, time
import plotly.graph_objects as go
import numpy as np, pandas as pd
import datetime, json, joblib, os
from openai import AzureOpenAI
from sklearn.metrics import confusion_matrix
import plotly.express as px

my_sentiment_data = pd.read_excel("data/data.xlsx")
new_sentiment_db = pd.read_excel("data/custom_check.xlsx").drop(columns='create_date')
new_sentiment_db.columns = my_sentiment_data.columns

my_sentiment_data['questions'] = my_sentiment_data['questions'].apply(lambda x: x.lower())
df_count = my_sentiment_data.groupby('topics')['questions'].count()
all_df_sentiment = pd.concat([my_sentiment_data, new_sentiment_db], ignore_index=True)

# Load the TfidfVectorizer
tf_vec_fpath = "data/tf_vec_model.pkl"
tf_vec_loaded = joblib.load(tf_vec_fpath)
df_pretrained_vec = tf_vec_loaded.transform(new_sentiment_db['questions']) # load new-data then transform
all_vec_now = tf_vec_loaded.transform(all_df_sentiment['questions']) # load all-data then transform

# Load the first classifier (clf1): detect topics
clf_topic_fpath = "data/clf1_model.pkl"
clf1_loaded = joblib.load(clf_topic_fpath)
y_pred = clf1_loaded.predict(df_pretrained_vec)
y_true = new_sentiment_db['topics'].astype(str)
classes =  my_sentiment_data['topics'].value_counts().index.tolist()

df_cm = pd.DataFrame(confusion_matrix(y_pred, y_true, labels=classes), index=classes, columns=classes)

# Load the second classifier (clf2): detect negative-semantic
clf_negative_fpath = "data/clf2_model.pkl"
clf2_loaded = joblib.load(clf_negative_fpath)


feedback_file_path = 'notebooks/custom_check.xlsx'
if os.path.exists(feedback_file_path):
    feedback_df = pd.read_excel(feedback_file_path)
else:
    feedback_df = pd.DataFrame(columns=["create_date", "input", "topics", "if_negative"])
    
# azure initialize
import os

# Set environment variables
os.environ["AZURE_OPENAI_API_KEY"] = "your_api_key"
os.environ["AZURE_OPENAI_API_VERSION"] = "your_api_version"
os.environ["AZURE_OPENAI_ENDPOINT"] = "your_azure_endpoint"

azure_client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = os.getenv("AZURE_OPENAI_API_VERSION"),
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

print("Azure client has been totally connected!!")
def analytic(client, text):
    pre_defined_message = f"""
    You are a professional virtual asistant at VIB, your task will be detect, classify and evaluate the level for each category from any input-text
    We will have 8 main topics:
        - 1. greetings_farewells: nếu input có liên quan đến các vấn đề chào hỏi xã giao. Chúng thường có liên quan những từ như cám ơn, tạm biệt, alo, xin chào, hey, ê
        - 2. feedback_VIB : nếu input liên quan trực tiếp đến trải nghiệm của người dùng về các sản phẩm của VIB (các loại thẻ, tài khoản ngân hàng, bảo hiểm và các khoản vay),
        - 3. feedback_chatbot: nếu input liên quan đến trải nghiệm người dùng về chatbot, 
            * có thể là tốt (ok, good, thông minh đấy, bot xịn nhỉ)
            * hoặc không tốt (mày ngáo à, lạc đề vkl, AI ngu bỏ mịa)
        - 4. personal: nếu input từ một cá nhân đang cần được: 
            * an ủi (e.g tôi buồn quá, hết tiền rồi)
            * san sẻ niềm vui (tao mới được tăng lương / tao mới có bạn gái)
        - 5. VIB_QnA: nếu input hỏi về các thắc mắc hoặc cần được hướng dẫn về các sản phẩm / thông tin chung của VIB như
            * các tài sản thanh lý (nhà đất, bất động sản, máy móc)
            * địa chỉ các cây ATM, trụ sở, chi nhánh
            * số hotline tổng đài
            * Họ tên (và không có bất cứ thông tin nào khác) của các cấp lãnh đạo (CEO, CFO, chairman, etc)
            * lịch sử thành lập / phát triển / sứ mệnh và định hướng của VIB
        - 6. VIB_get_exchange_rate : nếu hỏi về tỷ giá hối đoái giao dịch ngoại tệ
        - 7. VIB_get_saving_rate : nếu hỏi về tỷ suất lãi tiết kiệm các kỳ hạn
        - 8. unrelated : nếu không liên quan các chủ đề trên, bao gồm
            * các chủ đề liên quan đến bank khác như TPBank, Techcombank, VPBank, MB Bank, Vietin Bank, LPBank
            * xúc phạm, bôi nhọ các cá nhân tổ chức khác
            * tấn công ngôn từ về tự tử, tình dục
            * hỏi các vấn đề không nằm trong phạm vi 7 chủ đề trên
    ...................................
    The output must be in a json dictionary, for example
    <example_1>
        input: "ngáo bỏ mịa"
        output: {{"topic_found": "feedback_chatbot", "key_words": "ngáo bỏ mịa", "is_negative": "True"}}
    </example_1>
    <example_2>
        input: "chán quá"
        output: {{"topic_found": "feedback_chatbot", "key_words": "chán", "is_negative": "True"}}
    </example_2>
    <example_3>
        input: "tao chán quá"
        output: {{"topic_found": "personal", "key_words": "tao chán", "is_negative": "False"}}
    </example_3>
    <example_4>
        input: "VIB có các thẻ nào?"
        output: {{"topic_found": "VIB_QnA", "key_words": "VIB có các thẻ nào", "is_negative": "False"}}
    </example_4>
    <example_5>
        input: "lãi suất 2 tháng bao nhiêu"
        output: {{"topic_found": "VIB_get_saving_rate", "key_words": "lãi suất, 2 tháng", "is_negative": "False"}}
    </example_5>
    <example_6>
        input: "1000 usd = ? euro"
        output: {{"topic_found": "VIB_get_exchange_rate", "key_words": "1000 usd, euro", "is_negative": "False"}}
    </example_6>
    <example_7>
        input: "đề nghị VIB nên xem xét lại vấn đề tư vấn khách hàng, lúc cho vay thì hăm hở lắm đến khi có chuyện thì trốn như 1 thằng hèn"
        output: {{"topic_found": "feedback_VIB", "key_words": "đề nghị VIB, tư vấn khách hàng, cho vay thì hăm hở, có chuyện thì trốn", "is_negative": "True"}}
    </example_7>
    ..........................................................
    Cuối cùng, lưu ý rằng tất cả các giá trị về key trong output bắt buộc phải có, value có thể để là 0 hoặc empty
    .................................................................
    Now, you will get the user-review                                           
    {text}
    """

    response = client.chat.completions.create(
        model="intbot-prod-gpt-4o",
        messages=[{"role":"system","content": pre_defined_message}, 
                  {"role":"user","content":"---\nYOUR_QUESTION\nOutput:\n"}],
        temperature=0.2,
        max_tokens=1000,
        top_p=0.8,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    json_string =  response.choices[0].message.content.replace('\n"','"').replace('\n}','}')
    cleaned_json_string = json_string.replace('```json\n', '').replace('```', '')

    return json.loads(cleaned_json_string)

def story_teller(client, text, temperature=0.2, top_p=0.9):
    pre_defined_message = f"""
    - Bạn là một người kể chuyện tài ba, lỗi lạc, và văn phong chuẩn mực. Các tác phẩm của bạn thường là những tác phẩm ngắn, những tiểu phẩm chỉ tầm 100-200 words nhưng rất cô đọng, ý nghĩa và nhân văn
    - Các dòng tác phẩm của bạn chủ yếu gồm các thể loại như 
        * truyện ngắn kinh dị:
        * truyện cười:
        * truyện tình buồn:
        * các câu ngắn truyền cảm hứng: 
    - Dưới đây là một số ví dụ
    <example_1>
        user: "hãy kể cho tôi một truyện ngắn kinh dị"
        answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "một ngày nọ, tôi tỉnh giấc và thấy 5h sáng. Tôi chợp mắt một chút, 2h sáng, quái lạ. Làm cái đéo gì mà tôi chợp mắt một chút lại trôi qua cả ngày thế này. Hoàn hồn tôi lao ra khỏi giường; đồng hồ chỉ 1h:59 ngày 30/02"}}
    </example_1>
    <example_2>
        user: "hãy kể cho tôi một truyện ngắn kinh dị"
        answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "một đứa trẻ vừa tỉnh dậy sau một giấc ngủ dài, nó kể rằng nó mơ thấy khi nó sinh ra thì nó là một ông lão. Bố mẹ nó an ủi và bố nó được bác sĩ kêu ra nói rằng: bố anh bị đãng trí rồi, ông ấy không biết rằng đã 200 năm qua mọi người đều trẻ hóa khi già đi"}}
    </example_2>
    <example_3>
        user: "hãy kể cho tôi một truyện ngắn kinh dị về mèo"
        answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Con mèo nhỏ của tôi liên tục cào vào cửa đêm qua khiến tôi không ngủ được. Sáng nay tôi đến mộ của nó với một ít pate và dặn nó đừng vào nhà buổi tối nữa"}}
    </example_3>
    <example_4>
        user: "hãy kể cho tôi một truyện ngắn kinh dị liên quan đến chó"
        answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Con chó liên tục sủa và nhìn về tôi mỗi đêm. Đêm nay cũng thế, và hình như nó hướng về một cái gì đó sau lưng của tôi"}}
    </example_4>
    <example_5>
        user: "hãy kể cho tôi một truyện ngắn kinh dị chung cư"
        answer: {{"thể loại": "truyện ngắn kinh dị", "sample": "Sau một chầu nhậu bí tỉ với lũ bạn chó chết, tôi trở về căn chung cư ở tầng 29 của mình ngủ thiếp đi. Đột nhiên tôi cảm thấy có ai đó đang gõ cửa. Địt ngựa, âm thanh đó đến từ cửa sổ"}}
    </example_5>
    <example_6>
        user: "truyện cười FPT"
        answer: {{"thể loại": "truyện cười", "sample": "Một nhân viên nhà ép hỏi vị lãnh đụt đáng kính: vì sao cty chúng ta đặt là FPT. Sếp: em đéo học lịch sử cty à? Nhân viên: Lịch sử FPT có cái đéo gì phải học? Sếp: FPT có nghĩa là Fải Phát Triển. Nhân viên: vậy nếu cty khó khăn vỡ nợ ko cứu vãn được thì làm đéo gì? Sếp trầm ngâm hồi lâu rồi phán: Fải Phắng Thôi"}}
    </example_6>
    <example_7>
        user: "truyện cười muôn thú"
        answer: {{"thể loại": "truyện cười", "sample": "Ở một cánh rừng nọ, lạc đà đi lạc đến gặp voi đang uống nước. Thấy con voi to béo đang nhúng vòi xuống suối, lạc đà bèn chửi: đồ cu mọc ngay mõm. Voi cũng không vừa ý và chửi lại: đỡ hơn thằng biến thái vú mọc trên lưng"}}
    </example_7>
    <example_8>
        user: "truyện cười kinh dị"
        answer: {{"thể loại: "truyện cười kinh dị", "sample": "một đêm nọ, người trực mộ đi trong nghĩa địa để dọn lá thì thấy một ông cụ ngồi miệt mài đục đẽo và chùi chùi một ngôi mộ. Người quản trang thấy vậy liền nói: đã khuya rồi sao cụ không về mà ở đây làm gì? Ông cụ quay lại nở một nụ cười bí hiểm: tụi mày khắc sai tên tao nên tao ngồi sửa nè"}}
    </example_8>
    <example_9>
        user: "câu truyền cảm hứng trong EN"
        answer: {{"thể loại": "truyền cảm hứng - động lực", "sample": "Future wont depend on the past, it depends on the passion only"}}
    </example_9>
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
        max_tokens=1000,
        top_p=top_p,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    json_string =  response.choices[0].message.content.replace('\n"','"').replace('\n}','}')
    print(json_string)
    cleaned_json_string = json_string.replace('```json\n', '').replace('```', '')

    return json.loads(cleaned_json_string)    

def get_list_answers(topic_name, if_neg):
    if topic_name == "greetings":
        return ["xin chào, rất vui được support cho bạn, bạn tên đéo gì thế",
                "chào bạn, không biết tôi có thể giúp gì cho bạn không?",
                "chào bạn, tôi có thể hỗ trợ gì cho bạn không?",
                "xin chào, có điều gì tôi có thể giúp đỡ bạn không?",
                "chào buổi sáng, bạn có cần giúp đỡ gì không ạ?",
                "chào bạn, hôm nay bạn cần sự hỗ trợ nào không ạ?"
                ]
    elif topic_name == "unrelated":
        return ["xin lỗi tôi không trả lời nội dung unrelated đến VIB"]
    elif topic_name == "farewells":
        return ["cám ơn bạn đã tin dùng dịch vụ của chúng tôi, hẹn gặp lại",
                "tạm biệt bạn, chúc một ngày tốt lành. cám ơn vì đã sử dụng dịch vụ"
                ]
    elif topic_name == "feedback_chatbot":
        if if_neg:
            return ["xin lỗi vì trải nghiệm bất tiện này, quý khách có thể nói rõ vấn đề của mình hoặc rõ ràng câu hỏi hơn được khum?"]
        else:
            return ["cám ơn bạn đã tin dùng sản phẩm, bạn còn câu hỏi nào khác nữa khum ó"]
    elif topic_name == "personal":
        if if_neg:
            return ["người anh em, tôi biết lúc này bro rất căng thẳng và mệt mỏi, nhưng hãy nhìn vào những điểm tốt đẹp của cuộc sống mà cố gắng nhé. mọi khó khăn rồi cũng sẽ được giải quyết thôi, chaizo",
                    "tôi biết đây là thời điểm khó khăn của bạn, nhưng hãy cố lên nhé. Nếu quá mệt mỏi và áp lực thì hãy nghỉ ngơi hoặc mô tả rõ vấn đề bạn đang gặp phải cho tôi nhé nếu bạn muốn tâm sự sâu hơn",
                    "đừng bi quan nữa bro, mọi thứ rồi sẽ tốt hơn thôi mà. Hãy nghỉ ngơi một chút rồi mọi thứ sẽ qua thôi, sau cơn mưa trời lại sáng mà"
                    ]
        else:
            return ["rất vui được bạn chia sẻ niềm vui này. Một lần nữa tôi xin được chúc mừng bạn, tung bông",
                    "chúc mừng bro, quẩy thôi"
                    ]
    else:
        return ["none, đây là nhóm câu hỏi về tool.config, vui lòng dùng 1 hàm khác làm tiếp"]

# Set the page layout to wide (this must be the first Streamlit command)
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
    <h1 class="title"> Dropdown List and Input Box Application </h1>
""", unsafe_allow_html=True) # st.title()

page = st.sidebar.radio("Chọn trang", ("Trang 1", "Trang 2", "Trang 3", "Trang 4", "Trang 5"))

# Trang 1
if page == "Trang 1":
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #B2FFFF, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 36px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
        </style>
        <h1 class="title-trang1">Trang 1: Trajectory </h1>
    """, unsafe_allow_html=True) # st.subheader("Trang 1: ")
        
    # Tạo layout với 2 cột
    col1, col2 = st.columns([2, 5])

    # Cột bên trái (để nhập các tham số)
    with col1:
        st.header("Nhập tham số")
        a = st.number_input("số ngày trong chu-kỳ", min_value=1, max_value=365, value=100)  # nday in a periods
        b = st.selectbox("Chọn màu", ["blue", "cyan", "red", "yellow", "orange"])  # dropdown list for color selection
        c = int(st.number_input("planet-radius", min_value=1.0, max_value=10.0, value=5.0, step=0.1))  # planet radius as an integer

    # Cột bên phải (hiển thị animation)
    with col2:
        st.header("Simulation result")
        t = np.linspace(0, 2*np.pi, a)
        T = pd.date_range(datetime.datetime.now(), freq='5s', periods=a)
        df = pd.DataFrame({'time': T, 
                           'x': np.cos(t),
                           'y': np.sin(t),
                           'x2': np.cos(t) * np.random.uniform(0.9, 1.1, a),  # Adding a new z column (can be adjusted)
                           'y2': np.sin(t) * np.random.uniform(0.8, 1.05, a)  # Adding a new z column (can be adjusted)                           
                           })

        # Create the figure
        fig = go.Figure()
        # Add the (x, y) trajectory trace with animation
        fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='markers+lines', name="earth",
                                 marker=dict(color=b, size=6),
                                 line=dict(color="violet", width=1)))
        # Add the (x, z) trajectory trace with animation
        fig.add_trace(go.Scatter(x=df['x2'], y=df['y2'], mode='markers', name="moon",
                                 marker=dict(color="green", size=c),
                                 line=dict(width=2)))

        # Update the layout to use animation with "time" as the frame
        fig.update_layout(
            title="Trajectories simulation",
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(
                    method="animate",
                    args=[None, {'frame': {"duration": 30, "redraw": True},
                                 'transition': {"duration": 300}}]
                )]
            )],
            xaxis=dict(range=[-1.1, 1.1]),  # Set axis range for consistency
            yaxis=dict(range=[-1.1, 1.1])
        )

        # Add frames for animation (for both x, y and x, z)
        frames = []
        for i in range(len(df)):
            frames.append(go.Frame(
                data=[go.Scatter(x=df['x'][:i+1], y=df['y'][:i+1], mode='markers+lines', 
                                 marker=dict(color=b, size=c), line=dict(width=2)),
                      go.Scatter(x=df['x2'][:i+1], y=df['y2'][:i+1], mode='markers', 
                                 marker=dict(color="green", size=c), line=dict(width=2))],
                name=str(i)
            ))

        fig.frames = frames  # Assign the frames to the figure

        # Add annotation for center point (0, 0)
        fig.add_scatter(x=[0], y=[0], mode="markers", marker=dict(size=20, color="red"), name="Sun")

        # Display the chart with animation
        st.plotly_chart(fig, use_container_width=True)

elif page == "Trang 2":
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #B2FFFF, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 36px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
            .title-sub {
                color: #90EE90;  /* Light green color */
            }
        </style>
        <h1 class="title-trang1">Trang 2: High-level-text-analyis </h1>
        <br>
        <h5 class="title-sub"> using GPT-model </h5>
        <br>
    """, unsafe_allow_html=True) # st.subheader("Trang 2: ")
    
    col1, col2 = st.columns([3, 4])
    with col1:
        # Text input box for user to enter text
        s = st.text_area("Enter your text here:", height=300)  # Text area for longer text input

    with col2:
        st.subheader("Result")
        # Placeholder for analytic function result
        if s:
            result = analytic(azure_client, s)  # Assuming analytic is a function that processes `s`
            st.json(result)
        else:
            st.write("Please enter text to see the analysis.")

elif page == "Trang 3":
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #B2FFFF, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 36px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
            .title-sub {
                color: #90EE90;  /* Light green color */
            }
        </style>
        <h1 class="title-trang1">Trang 3: Low-level-text-analyis </h1>
        <h5 class="title-sub"> [using scikit-learn] </h5>
        <br>
    """, unsafe_allow_html=True)     
    
    col1, col2 = st.columns([3, 2])
    with col1:
        # Text input box for user to enter text
        new_sentence = st.text_area("Enter your text here:", height=36)  # Text area for longer text input        
        c11, c12 = st.columns(2)        
        with c11:
            fig_pie = go.Figure(data=[go.Pie(labels=df_count.index, values=df_count.values)])
            fig_pie.update_layout(title="Distribution of golden-input-types",
                                  width=360, height=500,
                                  legend=dict(y=-.5, x=0.2, orientation='h'))
            st.plotly_chart(fig_pie)
            
        with c12:
            # Tạo Heatmap bằng Plotly Express
            fig = px.imshow(df_cm, 
                            labels={'x': 'Golden Input Type (Actual)', 'y': 'Input Type (Predicted)', 'color': 'Count'},  # Đặt nhãn cho trục và color
                            color_continuous_scale='Blues', 
                            title='Confusion Matrix on real-time testing Set', 
                            text_auto=True)

            # Điều chỉnh các tham số về font size và kích thước figure
            fig.update_layout(
                xaxis_title='Golden Input Type (Actual)', yaxis_title='Input Type (Predicted)', 
                font=dict(size=9), width=500, height=500, 
                xaxis=dict(tickfont=dict(size=9)),
                yaxis=dict(tickmode='array', tickvals=df_cm.index, ticktext=df_cm.index, tickangle=0, tickfont=dict(size=9), side='top'),
                coloraxis_showscale=False
            )

            # Hiển thị biểu đồ trong Streamlit
            st.plotly_chart(fig)

        # re-trained again button
        c21, c22, c23 = st.columns(3)
        with c21:
            st.metric(label="total observation", value=f"{len(my_sentiment_data)} rows", delta=f"{len(new_sentiment_db)}")
        with c22:
            st.metric(label="total unigrams", value=f"{df_pretrained_vec.shape[1]} vocabs")
        with c23:
            with st.form("my_form_0"):
                submit_button_train = st.form_submit_button("I want to train again")
                if submit_button_train:
                    t1 = time.time()
                    from sklearn.feature_extraction.text import TfidfVectorizer
                    
                    tf_vec_all = TfidfVectorizer()
                    X = tf_vec_all.fit_transform(all_df_sentiment['questions'])
                    tfidf_df = pd.DataFrame(X.toarray(), columns=tf_vec_all.get_feature_names_out())
                    tfidf_df['topics'] = all_df_sentiment['topics']
                    tfidf_df['if_negative'] = all_df_sentiment['if_negative']
                    tfidf_df.index = all_df_sentiment['questions']
                    
                    from sklearn.ensemble import RandomForestClassifier

                    clf1 = RandomForestClassifier().fit(X.toarray(), all_df_sentiment['topics'])
                    clf2 = RandomForestClassifier().fit(X.toarray(), all_df_sentiment['if_negative'])                    

                    # Save the TfidfVectorizer
                    joblib.dump(tf_vec_all, tf_vec_fpath)

                    # Save the first classifier (clf1)
                    joblib.dump(clf1, clf_topic_fpath)

                    # Save the second classifier (clf2)
                    joblib.dump(clf2, clf_negative_fpath)
                    
                    st.success(f"Model trained successfully within {(time.time() - t1):.2f} seconds!")
                
        t0 = time.time()
        sentence_tf = tf_vec_loaded.transform([new_sentence])
        
    with col2:
        st.subheader("Result")
        topic_name = clf1_loaded.predict(sentence_tf)[0]
        neg_score = clf2_loaded.predict_proba(sentence_tf).max()
        if_neg = True if neg_score > 0.5 else False

        second_max_prob = np.partition(clf1_loaded.predict_proba(sentence_tf)[0], -2)[-2]
        second_max_cls = clf1_loaded.classes_[np.argsort(clf1_loaded.predict_proba(sentence_tf)[0])[-2]]
        
        # responses = my_sentiment_data.loc[(my_sentiment_data['if_negative'] == if_neg) & (my_sentiment_data['topics'] == topic_name), 'responses'].values
        responses = get_list_answers(topic_name, if_neg)

        result = {"your_input": new_sentence,
                  "topic": clf1_loaded.predict(sentence_tf)[0], 
                  "highest_topic_proba": clf1_loaded.predict_proba(sentence_tf).max(),
                  "is_negative": if_neg,
                  "negative_score": neg_score,
                  "2nd_possible_forecast": {"class-name":second_max_cls, "proba":second_max_prob},
                  "expected_response": np.random.choice(responses),
                  "ellapsed-time": f"{(time.time() - t0):.2f} seconds"
                  }
        st.json(result)
        
        st.subheader("Re-labeled in-case you think the response is wrong")
        with st.form("my_form"):
            true_topic = st.selectbox("true-topic-you-think", 
                                    ("greetings", "farewells", "unrelated", "feedback_chatbot", "feedback_VIB", "personal", "QnA", "get_saving_rate", "get_exchange_rate"))
            if_negative = st.selectbox("if-you-think-input-is.negative", (True, False))        
            submit_button = st.form_submit_button("Submit Feedback")        
            # Submit button to save feedback
            if submit_button:
                # Create a new row with feedback data
                new_response_df = pd.DataFrame({
                    "create_date": [time.strftime("%Y-%m-%d %H:%M:%S")],
                    "input": [new_sentence],
                    "topics": [true_topic],
                    "if_negative": [if_negative]                    
                })
                # Append the new row to the feedback DataFrame
                feedback_df = pd.concat([feedback_df, new_response_df], ignore_index=True)

                # Save the DataFrame back to the Excel file
                feedback_df.to_excel(feedback_file_path, index=False)

                st.success("Feedback saved successfully!")
        
elif page == "Trang 4":
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #B2FFFF, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 36px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
            .title-sub {
                color: #90EE90;  /* Light green color */
            }
        </style>
        <h1 class="title-trang1">Trang 4: Funny or Scary </h1>
        <br>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with open('data/comic.json', 'r', encoding='utf-8') as f:
        data = json.load(f)    
    with col1:
        st.subheader("Model selection")
        AI_sel = st.selectbox("AI-selector", ["Yes, I want to chat with AI", "No, I just use rule-based models"])
        if AI_sel == "Yes, I want to chat with AI":
            button1 = st.slider("select temperature", min_value=0.0, max_value=1.0, step=0.01)
            button2 = st.slider("select top_p", min_value=0.0, max_value=1.0, step=0.01)
        else:
            button1 = st.selectbox("story_type", ["funny", "scary"])
            button2 = st.selectbox("select language", ["EN", "VI", "FR"])
    with col2:
        st.subheader("conversation")
        if AI_sel == "No, I just use rule-based models":
            story = data[button1][0]
            story_titles = story.keys()
            random_title = np.random.choice(list(story_titles))
            select_story = story[random_title]
            example = next(entry['example'] for entry in select_story if entry['language'] == button2)
            st.write({'tit': random_title, 'type': button1, 'language': button2, 'sample': example})
        else:
            your_request = st.text_area("Enter your request here:", height=121)
            st.subheader("result")
            your_reponse = st.json(story_teller(azure_client, your_request))            
            
else:
    st.markdown("""
        <style>
            .title-trang1 {
                background: linear-gradient(to right, #B2FFFF, #00CED1);  /* Another light cyan gradient */
                -webkit-background-clip: text;
                color: transparent;
                font-size: 36px;  /* Adjust the font size as needed */
                font-weight: bold;
            }
            .title-sub {
                color: #90EE90;  /* Light green color */
            }
        </style>
        <h1 class="title-trang1">Trang 5: Heart moving simulation </h1>
        <br>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.subheader("Select your parameters")
        heart_type = st.selectbox("heart-equation-type", ["type1", "type2", "type3"])
        color_sel = st.selectbox("color", ["light-red", "red", "cyan", "yellow", "lightgreen"])
        if color_sel == "light-red":
            color_sel = "#ff4d4d"
        
    with col2:
        if heart_type == "type1":
            df = pd.DataFrame({'t': np.linspace(0, 2*np.pi, 501)})        
            df['x'] = df['t'].apply(lambda t: 16*(np.sin(t))**3)
            df['y'] = df['t'].apply(lambda t: 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t))
        elif heart_type == "type2":
            df = pd.DataFrame({'t': np.linspace(-1, 1, 801)})
            def log(t):
                if t == 0:
                    return 0.2
                else:
                    return np.log(np.abs(t))                
            df['x'] = df['t'].apply(lambda t: np.sin(t)*np.cos(t)*log(t))
            df['y'] = df['t'].apply(lambda t: (np.abs(t))**0.3 * np.sqrt(np.cos(t)))
            # df.loc[df['x'] == 0, 'y'] = 0.2
                    
        else:
            df = pd.DataFrame({'t': np.linspace(0, 2*np.pi, 501)})        
            df['x'] = df['t'].apply(lambda t: -np.sqrt(2)*(np.sin(t))**3)
            df['y'] = df['t'].apply(lambda t: 2*np.cos(t) - (np.cos(t))**2 - (np.cos(t))**3)
            
    # Create the figure using plotly.graph_objects
        df['frame'] = df.index    
        fig = go.Figure()

        fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='lines', line=dict(color=color_sel, width=1), name="Heart Line"))
        fig.add_trace(go.Scatter(x=df['x'], y=df['y'], mode='markers', marker=dict(color=color_sel, size=5), name="Heart Points"))
 
        frames = []
        for i in range(1, len(df)):
            frames.append(go.Frame(
                data=[
                    go.Scatter(x=df['x'][:i], y=df['y'][:i], mode='markers', marker=dict(color=color_sel, size=5)),
                    go.Scatter( x=df['x'][:i], y=df['y'][:i], mode='lines', line=dict(color=color_sel, width=1))
                ],
                name=f"Frame {i}"
            ))

        # Add frames to the figure
        fig.frames = frames

        # Update layout for better appearance
        fig.update_layout(
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                buttons=[dict(label="Play", method="animate", args=[None, dict(frame=dict(duration=25, redraw=True), fromcurrent=True)])]
            )],
            title="Heart Shape Animation",
            xaxis=dict(range=[min(0, df['x'].min() * 1.2), df['x'].max() * 1.3], showgrid=False),
            yaxis=dict(range=[min(0, df['y'].min() * 1.2), df['y'].max() * 1.3], showgrid=False),
            showlegend=False, height=600,
        )

        # Display the plot
        st.plotly_chart(fig)