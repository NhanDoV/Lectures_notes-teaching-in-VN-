import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np, pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("data/all_logs.xlsx")
df['total_consume'] = pd.to_numeric(df['total_consume'], errors='coerce')
total_nb_inputs = len(df)
n_uniq_conv = len(df['conv_id'].value_counts())
n_nega_inp = len(df[df['if_negative'] == True])
perc = pd.pivot_table(df, index='topic_detected', columns='if_negative', 
                      aggfunc='count', values='conv_id', fill_value=0)
perc['percentage'] = perc[True] / (perc[True] + perc[False])
most_nega_inpty_val = perc[True].max()
most_nega_inpty_nm = perc[True].idxmax()
highest_nega_inpty_val = 100*perc["percentage"].max()
highest_nega_inpty_nm = perc["percentage"].idxmax()
y_true = df['topic_detected'].astype(str)
y_pred = df['input_type'].fillna("null").astype(str)
classes = y_pred.value_counts().index.tolist()
df['date'] = pd.to_datetime(df['create_at'], format="%Y-%m-%d").dt.date

# print(df.loc[(df['input'].str.contains('sinh trắc')) & (df['input_type'] == 'unrelated'), ['input', 'choice', 'input_type', 'topic_detected', 'keywords']])

st.set_page_config(layout="wide")
page = st.sidebar.radio("Chọn trang", ("Trang 1", "Trang 2", "Trang 3"))

# Trang 1
if page == "Trang 1":
    st.header("Page 1: Overview")        
    col_1_1, col_1_2, col_1_3, col_1_4 = st.columns(4)
    with col_1_1:
        st.metric(label="Total number of questions", value=f"{total_nb_inputs}")
    with col_1_2:
        st.metric(label="Nb of distinct conversation", value=f"{n_uniq_conv}")
    with col_1_3:
        st.metric(label="Total number of\n negative input", value=f"{n_nega_inp}")            
    with col_1_4:
        st.metric(label="n-unique negative-inp per conv-id", 
                  value=f"{len(df.loc[df['if_negative'] == True, 'conv_id'].value_counts())}")
                
    # Second row with 2 columns
    col_2_1, col_2_2, col_2_3 = st.columns(3)
    with col_2_1:
        st.metric(label="longest-conversation recorded", 
                  value=f"{df['conv_id'].value_counts().values[0]}", 
                  delta=f"{df['conv_id'].value_counts().index[0]}")
    with col_2_2:
        st.metric(label="input type has highest negative-percentage response",
                  value=f"{highest_nega_inpty_val:.2f} %", delta=f"-topic: {highest_nega_inpty_nm}")
    with col_2_3:
        st.metric(label="input type has the most negative-percentage response",
                  value=f"{most_nega_inpty_val}", delta=f"-topic: {most_nega_inpty_nm}")

    col_3_1, col_3_2 = st.columns([2, 3])
    with col_3_1:
        perc_df = df['topic_detected'].value_counts()
        st.subheader("Distribution of golden-input-type")
        fig_pie = go.Figure(data=[go.Pie(labels=perc_df.index, values=perc_df.values)])
        st.plotly_chart(fig_pie)
    with col_3_2:        
        fig_bar_line = go.Figure()
        perc['percentage'] = (100*perc['percentage']).round(2)
        fig_bar_line.add_trace(go.Bar(x=perc.index, y=perc[True], 
                                      text=perc[True].values, textposition='auto',
                                      name="count", marker_color='lightblue') )                # Adding Bar chart
        fig_bar_line.add_trace(go.Scatter(x=perc.index, y=perc['percentage'].values, 
                                          text=[f'{s:.2f} %' for s in perc['percentage'].values], textposition='top center',
                                          mode='lines+markers', name="percentage (%)", line=dict(width=1, color='red'), yaxis="y2"))         # Adding Line chart                
        fig_bar_line.update_layout(
            title="Negative-content (count & percentage) by golden-input-type",
            yaxis=dict(title="count"),
            yaxis2=dict(
                title="Percentage (%)", 
                overlaying='y',  # Trục y2 sẽ chia sẻ trục x với y
                side='right'  # Đặt secondary y-axis ở bên phải
            ),
            xaxis=dict(title="golden-input-type"),
            legend=dict(x=1, y=1, xanchor='right', yanchor='top')
        )
        st.plotly_chart(fig_bar_line)        

    col_4_1, col_4_2 = st.columns(2)
    with col_4_1:
        st.subheader("Count of question-type")
        df_ques = df[df['topic_detected'] == 'question'].groupby('tool_used')['conv_id'].count().reset_index()
        df_ques.columns = ['question', 'count']
        df_ques = df_ques.sort_values(by='count')
        fig = px.bar(df_ques, x='count', y='question', text_auto=True)
        st.plotly_chart(fig)
        
    with col_4_2:
        df_c = pd.pivot_table(df, index='month', columns='if_negative', aggfunc='count', 
                              values='conv_id', fill_value=0)
        df_c['count-all'] = df_c[False] + df_c[True]
        df_c['nega-percentage'] = 100*df_c[True] / df_c['count-all']
        df_c = df_c.reset_index().sort_values(by='month', ascending=False)
        
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Bar(x=df_c['month'], y=df_c['count-all'], 
                                      text=df_c['count-all'].values, textposition='auto',
                                      name="count", marker_color='lightblue') )                # Adding Bar chart
        fig_bar_line.add_trace(go.Scatter(x=df_c['month'], y=df_c['nega-percentage'].values, 
                                          text=[f'{s:.2f} %' for s in df_c['nega-percentage'].values], textposition='top center',
                                          mode='lines+markers', name="percentage (%)", line=dict(width=1, color='red'), yaxis="y2"))
        fig_bar_line.update_layout(
            title="Negative-content (count & percentage) by month",
            yaxis=dict(title="count"),
            yaxis2=dict(
                title="Percentage (%)", 
                overlaying='y',  # Trục y2 sẽ chia sẻ trục x với y
                side='right'  # Đặt secondary y-axis ở bên phải
            ),
            xaxis=dict(title="month"),
            legend=dict(x=1, y=1, xanchor='left', yanchor='top')
        ) 
        st.plotly_chart(fig_bar_line)

    _, row5 = st.columns([1, 9])
    with row5:        
        ddf1 = df.groupby('date')['conv_id'].count()
        ddf2 = df[df['if_negative'] == True].groupby('date')['conv_id'].count()
        df_daily_cnt = pd.concat([ddf1, ddf2], axis=1).fillna(0)
        df_daily_cnt.columns = ['count.all', 'count.negative']
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Scatter(x=df_daily_cnt.index, y=df_daily_cnt['count.all'], 
                                          mode="lines", name="count.all", marker_color='lightblue') ) 
        fig_bar_line.add_trace(go.Scatter(x=df_daily_cnt.index, y=df_daily_cnt['count.negative'].values, 
                                          mode='lines+markers', name="count.negative", 
                                          line=dict(color='red'), yaxis="y2"))
        fig_bar_line.update_layout(
            title="Counts Over Time",
            yaxis=dict(
                title="count.all",  # Title for the primary y-axis
                side='left'  # Place it on the left side
            ),
            yaxis2=dict(
                title="count.negative",  # Title for the secondary y-axis
                overlaying='y',  # Overlay on the primary y-axis
                side='right'  # Place it on the right side
            ),
            xaxis=dict(title="date"),  # Set title for the x-axis
            legend=dict(x=1, y=1, xanchor='left', yanchor='top')
        )        
        st.plotly_chart(fig_bar_line)
    
elif page == "Trang 2":
    st.header("Page 2: Model-accuracy")
    col_1_1, col_1_2, col_1_3, col_1_4 = st.columns(4)
    with col_1_1:
        st.metric(label="Average-accuracy", value="86.37 %")
    with col_1_2:
        st.metric(label="average-precison", value="82.83 %")
    with col_1_3:
        st.metric(label="n-null-input-types", value="1069")
    with col_1_4:
        st.metric(label="n-questions most frequently misclassified as unrelated", value="93", delta="- topic: eKyc")
    
    col_2_1, col_2_2 = st.columns([1, 2])
    df_cm = pd.DataFrame(confusion_matrix(y_pred, y_true, labels=classes), index=classes, columns=classes)
    with col_2_1:
        fig, ax = plt.subplots(figsize=(6, 6))
        sns.heatmap(df_cm, annot=True, fmt='d', cmap='Blues', xticklabels=df_cm.columns, 
                    yticklabels=df_cm.index, ax=ax)
        plt.xticks(rotation=45)
        ax.set_xlabel("golden-input-type (actual)")
        ax.set_ylabel("input-type (predicted)")        
        fig.suptitle("Confusion matrix")
        st.pyplot(fig)
    with col_2_2:
        classes = ['question', 'greetings_farewells', 'feedback_chatbot', 'feedback_VIB', 'personal', 'unrelated']
        cm = confusion_matrix(y_true, y_pred, labels=classes)
        # Initialize lists to store precision and recall values
        precision_per_class = []
        recall_per_class = []
        accuracy_per_class = []
        # Calculate precision and recall per class
        for i, category in enumerate(classes):
            TP = cm[i, i]  # True Positive: correct predictions for this class
            FP = cm[:, i].sum() - TP  # False Positive: predicted as this class but are not
            FN = cm[i, :].sum() - TP  # False Negative: actually this class but predicted as something else
            
            precision = TP / (TP + FP) if (TP + FP) != 0 else 0
            recall = TP / (TP + FN) if (TP + FN) != 0 else 0
            f1_score = 2*(precision*recall)/(precision + recall)
            
            precision_per_class.append(precision)
            recall_per_class.append(recall)
            accuracy_per_class.append(f1_score)
            
        # Metric names and their values
        metric_names = ['Precision', 'Recall']
        metric_values = [precision_per_class, recall_per_class]

        # Create a Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Bar(x=classes, y=precision_per_class, name='Precision', marker_color='lightblue', 
                             text=[f'{(100*s):.2f} %' for s in precision_per_class], textposition='outside'))
        fig.add_trace(go.Bar( x=classes, y=recall_per_class, name='Recall', marker_color='lightgreen',
                             text=[f'{(100*s):.2f} %' for s in recall_per_class], textposition='outside'))
        fig.add_trace(go.Scatter(x=classes, y=accuracy_per_class, mode='lines+markers', name='f1-score', 
                                 text=[f'{(100*s):.2f} %' for s in accuracy_per_class], line=dict(color='red', width=1, dash='solid')))
        fig.update_layout(
            title="Precision, Recall, and f1-score per Class",
            xaxis_title="golden-input-type", yaxis_title="Scores",
            barmode='group', template="plotly_white",  # Chọn theme cho biểu đồ
            showlegend=True  # Hiển thị legend
        )
        st.plotly_chart(fig)   
    
    col_3_1, col_3_2, col_3_3 = st.columns(3)
    with col_3_1:
        df_c = pd.pivot_table(df, index='month', columns='need_check', aggfunc='count', values='conv_id', fill_value=0)
        df_c['count-all'] = df_c[False] + df_c[True]
        df_c['nega-percentage'] = 100 * df_c[True] / df_c['count-all']
        df_c = df_c.reset_index().sort_values(by='month', ascending=False)
        
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Bar(x=df_c['month'], y=df_c[False], 
                                      text=df_c[False].values, textposition='outside',
                                      name="n-predicted-false", marker_color='lightblue') )                # Adding Bar chart
        fig_bar_line.add_trace(go.Scatter(x=df_c['month'], y=df_c['nega-percentage'].values, 
                                          mode='lines+markers', name="accuracy (%)", line=dict(color='red'), yaxis="y2"))
        fig_bar_line.update_layout(
            title="Negative-content (count & percentage) by month",
            yaxis=dict(title="count"),
            yaxis2=dict(
                title="Percentage (%)", 
                overlaying='y',  # Trục y2 sẽ chia sẻ trục x với y
                side='right'  # Đặt secondary y-axis ở bên phải
            ),
            xaxis=dict(title="month"),
            legend=dict(x=1, y=1, xanchor='left', yanchor='top')
        ) 
        st.plotly_chart(fig_bar_line)

    with col_3_2:
        df_c = df.loc[(df['input_type'].isnull()) & (df['topic_detected'] == 'question'), ['conv_id', 'tool_used', 'if_negative']]
        df_c = df_c.groupby(['tool_used', 'if_negative']).count().reset_index()
        df_c.columns = ['tool_used', 'if_negative', 'count']
        tool_used_list = ['QnA', 'get_saving_rate', 'get_exchange_rate']
        if_negative_list = [True, False]            
        fig = px.bar(df_c, x='count', y='tool_used', color='if_negative', barmode='group', text_auto=True, 
                     color_discrete_map={True: '#ff4d4d', False: 'lightgreen'},
                     text='count', category_orders={'tool_used': tool_used_list, 'if_negative': [True, False]})
        st.plotly_chart(fig)
        
    with col_3_3:
        df_c = df.loc[(df['input_type'].isnull()) & (df['topic_detected'] != 'question'), ['conv_id', 'topic_detected', 'if_negative']]
        df_c = df_c.groupby(['topic_detected', 'if_negative']).count().reset_index()
        df_c.columns = ['topic_detected', 'if_negative', 'count']
        tool_used_list = ['unrelated', 'personal', 'feedback_chatbot', 'greetings_farewells', 'feedback_VIB']
        if_negative_list = [True, False]                
        fig = px.bar(df_c, x='count', y='topic_detected', color='if_negative', barmode='group', text_auto=True, 
                     category_orders={'topic_detected': tool_used_list, 'if_negative': [True, False]}, 
                     color_discrete_map={True: '#ff4d4d', False: 'lightgreen'})
        st.plotly_chart(fig)
                  
    _, r4 = st.columns([1, 9])
    with r4:
        df_c = pd.pivot_table(df, index='date', columns='need_check', values='conv_id', aggfunc='count')
        df_c['count.all'] = df_c[True] + df_c[False]
        df_c['accuracy'] = 100*df_c[True] / df_c['count.all']    
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['count.all'], 
                                          mode="lines+markers", name="count.all", marker_color='lightblue') ) 
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['accuracy'].values, 
                                          mode='lines+markers', name="accuracy (%)", line=dict(color='red'), yaxis="y2"))
        fig_bar_line.update_layout(title="Accuracy Over Time", 
                                   yaxis=dict(title="count.all",side='left'),
                                   yaxis2=dict(title="accuracy", overlaying='y', side='right'),
                                   xaxis=dict(title="date"), legend=dict(x=1, y=1, xanchor='left', yanchor='top')
                                )        
        st.plotly_chart(fig_bar_line)
    _, r5, _ = st.columns([1, 9, 1])
    with r5:
        st.subheader("Error 1: Competitors (unrelated -> question)")     
        sub_df = df.loc[df['stop_since'] == 'competitors', ['input', 'choice', 'input_type', 'topic_detected', 'keywords']]
        st.dataframe(sub_df)
    _, r6, _ = st.columns([1, 9, 1])
    with r6:
        st.subheader("Error 2: Missed-context database (unrelated -> question)")     
        sub_df = df.loc[(df['input'].str.contains('sinh trắc')) & (df['input_type'] == 'unrelated'), ['input', 'choice', 'input_type', 'topic_detected']]
        st.dataframe(sub_df)    
    _, r7, _ = st.columns([1, 9, 1])
    with r7:
        st.subheader("Error 3: Missed-schema in question-keyword confused from tool.config")     
        sub_df = df.loc[df['input_type'].isnull() & (df['tool_used'].isin(['get_saving_rate', 'get_exchange_rate'])), 
                        ['input', 'choice', 'input_type', 'topic_detected', 'keywords']]
        st.dataframe(sub_df)
        
elif page == "Trang 3":
    st.header("Page 3: Model-performance")
    col_1_1, col_1_2, col_1_3, col_1_4, col_1_5 = st.columns(5)
    with col_1_1:
        st.metric(label="AVG-time-consume", value=f"{df['total_consume'].mean():.2f}")
    with col_1_2:
        st.metric(label="AVG-completion-tokens", value=f"{df['completion_tokens'].mean():.2f}")
    with col_1_3:
        st.metric(label="AVG-prompt-tokens", value=f"{df['prompt_tokens'].mean():.2f}")
    with col_1_4:
        st.metric(label="nb(input.completion.tokens > 600)", value=f"{len(df[df['completion_tokens'] > 600])}")
    with col_1_5:
        st.metric(label="nb(input.time.consume > 10 secs)", value=f"{len(df[df['total_consume'] > 10])}")
        
    col_2_1, col_2_2, col_2_3 = st.columns([3, 4, 3])
    with col_2_1:
        fig = px.box(df, y='topic_detected', x='total_consume', color='topic_detected', title="Boxplot on time.consume",
                     category_orders={'topic_detected': ['question', 'feedback_VIB', 'personal', 'feedback_chatbot', 'greetings_farewells', 'unrelated']})
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)
    with col_2_2:
        fig = px.box(df, y='topic_detected', x='prompt_tokens', color='topic_detected', title="Boxplot on n_prompt_tokens",
                     category_orders={'topic_detected': ['question', 'feedback_VIB', 'personal', 'feedback_chatbot', 'greetings_farewells', 'unrelated']})
        st.plotly_chart(fig)
    with col_2_3:
        fig = px.box(df, y='topic_detected', x='completion_tokens', color='topic_detected', title="Boxplot on n_completion_tokens",
                     category_orders={'topic_detected': ['question', 'feedback_VIB', 'personal', 'feedback_chatbot', 'greetings_farewells', 'unrelated']})
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig)        

    col_3_1, col_3_2 = st.columns([2, 3])
    with col_3_1:
        df_c = df.groupby('month')[['total_consume', 'prompt_tokens', 'completion_tokens']].mean()
        df_c = df_c.reset_index().sort_values(by='month', ascending=False)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_c['month'], y=df_c['prompt_tokens'], name='AVG completion Tokens',
            text=[f"prompt_tk: {df_c['prompt_tokens'].values[k]:.2f} <br> compl_tk: {df_c['completion_tokens'].values[k]:.2f}" for k in range(len(df_c))],
            textposition='outside', hoverinfo='x+text+y',  marker_color='lightgreen'
        ))
        fig.add_trace(go.Scatter(
            x=df_c['month'],  y=df_c['total_consume'], mode='lines+markers', 
            name='AVG time.consume', line=dict(color='blue', width=1), hoverinfo='x+y', yaxis="y2"
        ))
        fig.update_layout(
            title='Average statistics by month',
            xaxis_title='month',
            yaxis=dict(title="n_tokens",side='left', range=[10000, 16000]),
            yaxis2=dict(title="time.consume (seconds)", overlaying='y', side='right', range=[2, 11]),
            barmode='group', template='plotly_dark', hovermode='closest',
            legend=dict(x=1, y=1, xanchor='left', yanchor='top')
        )
        st.plotly_chart(fig)
        
    with col_3_2:
        df_c = df.groupby('topic_detected')[['total_consume', 'prompt_tokens', 'completion_tokens']].mean().reset_index()
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_c['topic_detected'], y=df_c['prompt_tokens'], name='AVG completion Tokens',
            text=[f"prompt_tk: {df_c['prompt_tokens'].values[k]:.2f} <br> compl_tk: {df_c['completion_tokens'].values[k]:.2f}" for k in range(len(df_c))],
            textposition='outside', hoverinfo='x+text+y',  marker_color='lightgreen'
        ))
        fig.add_trace(go.Scatter(
            x=df_c['topic_detected'],  y=df_c['total_consume'], mode='lines+markers', 
            name='AVG time.consume', line=dict(color='blue', width=1), hoverinfo='x+y', yaxis="y2"
        ))
        fig.update_layout(
            title='Average statistics by golden-input-types (topic-detected)',
            xaxis_title='topic_detected',
            yaxis=dict(title="n_tokens",side='left', range=[1000, 16000]),
            yaxis2=dict(title="time.consume (seconds)", overlaying='y', side='right', range=[2, 11]),
            barmode='group', template='plotly_dark', hovermode='closest',
            legend=dict(x=1, y=1, xanchor='left', yanchor='top')
        )
        st.plotly_chart(fig)
        
    _, r4, _ = st.columns([1,9,1])
    with r4:
        df_c = df.groupby('date')[['total_consume', 'prompt_tokens']].mean()
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['total_consume'], 
                                          mode="lines+markers", name="total_consume", marker_color='lightblue') ) 
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['prompt_tokens'].values, 
                                          mode='lines+markers', name="prompt_tokens", line=dict(color='red'), yaxis="y2"))
        fig_bar_line.update_layout(title="Daily average.statistics of time-consume vs prompt-tokens", 
                                   yaxis=dict(title="time.consume",side='left'),
                                   yaxis2=dict(title="n-tokens", overlaying='y', side='right'),
                                   xaxis=dict(title="date"), legend=dict(x=1, y=1, xanchor='left', yanchor='top')
                                )        
        st.plotly_chart(fig_bar_line)
        
    _, r5, _ = st.columns([1,9,1])
    with r5:
        df_c = df.groupby('date')[['total_consume', 'completion_tokens']].mean()
        fig_bar_line = go.Figure()
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['total_consume'], 
                                          mode="lines+markers", name="total_consume", marker_color='lightblue') ) 
        fig_bar_line.add_trace(go.Scatter(x=df_c.index, y=df_c['completion_tokens'].values, 
                                          mode='lines+markers', name="completion_tokens", line=dict(color='red'), yaxis="y2"))
        fig_bar_line.update_layout(title="Daily average.statistics of time-consume vs completion_tokens", 
                                   yaxis=dict(title="time.consume",side='left'),
                                   yaxis2=dict(title="n-tokens", overlaying='y', side='right'),
                                   xaxis=dict(title="date"), legend=dict(x=1, y=1, xanchor='left', yanchor='top')
                                )        
        st.plotly_chart(fig_bar_line)
        
    _, r6, _ = st.columns([1, 9, 1])
    with r6:
        st.subheader("Case 1")
        sub_df = df.loc[df['prompt_tokens'] == 0, ['input', 'choice', 'prompt_tokens', 'completion_tokens', 'input_type', 'topic_detected', 'total_consume']]
        st.dataframe(sub_df)

    _, r7, _ = st.columns([1, 9, 1])
    with r7:
        st.subheader("Case 2")
        sub_df = df.loc[df['completion_tokens'] > 600, ['input', 'choice', 'prompt_tokens', 'completion_tokens', 'input_type', 'topic_detected', 'total_consume']]
        st.dataframe(sub_df)
        
    _, r8, _ = st.columns([1, 9, 1])
    with r8:
        st.subheader("Case 3")
        sub_df = df.loc[df['total_consume'] > 10, ['input', 'choice', 'total_consume', 'prompt_tokens', 'completion_tokens', 'input_type', 'topic_detected']]
        st.dataframe(sub_df)        