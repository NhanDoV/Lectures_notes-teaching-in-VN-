from flask import Flask, render_template, request
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np

app = Flask(__name__)
df = pd.read_excel(r"data\user_answers.xlsx")
dfs = pd.read_excel(r"D:\NhanDV\chatbot\openai\data\true_false.xlsx")

# Prepare the DataFrames for charts
z = pd.concat([df['gpt4o_qualify'].value_counts(), 
               df['gpt35_qualify'].value_counts(),
               df['haiku_qualify'].value_counts(),
               df['sonet_qualify'].value_counts()
              ], axis=1)
z.columns = ['GPT4o', 'GPT3.5', 'Haiku', 'Sonet']
z = pd.DataFrame(z.stack()).reset_index()
z.columns = ['qualify', 'chatbot', 'count']

zf = pd.concat([dfs['haiku_manual_check'].fillna(1).value_counts(), 
                dfs['gpt35_manual_check'].fillna(1).value_counts()], axis=1)
zf.columns = ['haiku_manual_check', 'gpt35_manual_check']
zf.index = [True, False]
zf = pd.DataFrame(zf.stack()).reset_index()
zf.columns = ['qualify', 'chatbot', 'count']

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/chart')
def chart():
    chart_type = request.args.get('chart_type', 'gpt35_qualify')
    pie_chart_type = request.args.get('pie_chart_type', 'quest_type_cate')
    df_selection = request.args.get('df_selection', 'z')  # New dropdown for df selection

    if chart_type not in ['gpt35_qualify', 'haiku_qualify', 'gpt4o_qualify', 'sonet_qualify']:
        return "Invalid chart type", 400
    
    if pie_chart_type not in ['quest_type_cate', 'quest_content_level1', 'haiku_manual_check', 'gpt35_manual_check']:
        return "Invalid pie chart type", 400
    
    if df_selection == 'z':
        df4 = z
        df4_title = 'Qualification by Type'
    elif df_selection == 'zf':
        df4 = zf
        df4_title = 'Manual Check by Type'
    else:
        return "Invalid DataFrame selection", 400
    
    # Pie chart logic remains the same
    if pie_chart_type == 'quest_type_cate':
        df_pie = df.groupby('quest_type_cate').count().reset_index()
        fig_pie = px.pie(df_pie, names='quest_type_cate', values='question', 
                        title='Distribution of quest_type_cate', height=400)
    elif pie_chart_type == 'quest_content_level1':
        df_pie = df.groupby('quest_content_level1').count().reset_index()
        fig_pie = px.pie(df_pie, names='quest_content_level1', values='question', 
                        title='Distribution of question_type', height=400)
    elif pie_chart_type == 'gpt35_manual_check':
        df_pie = dfs['gpt35_manual_check'].fillna(1).value_counts().reset_index()
        fig_pie = px.pie(df_pie, names='gpt35_manual_check', values='count', 
                        title='Distribution of gpt35_manual_check', height=400)
    elif pie_chart_type == 'haiku_manual_check':
        df_pie = dfs['haiku_manual_check'].fillna(1).value_counts().reset_index()
        fig_pie = px.pie(df_pie, names='haiku_manual_check', values='count', 
                        title='Distribution of haiku_manual_check', height=400)
    
    start_color = np.array([245, 160, 122])  # RGB for #ADD8E6 (light blue)
    end_color = np.array([173, 216, 230])      # RGB for #2F4F4F (dark slate gray)
        
    for i in range(100):
        ratio = i / (100 - 1)
        interpolated_color = (start_color * (1 - ratio) + end_color * ratio).astype(int)
        color_hex = '#{:02X}{:02X}{:02X}'.format(*interpolated_color)
        
        fig_pie.add_shape(
            type='rect',
            x0=i / 100,  
            y0=0,             
            x1=(i + 1) / 100,  
            y1=1,              
            fillcolor=color_hex,
            line=dict(color='rgba(0,0,0,0)'),  
            opacity=1,
            layer='below'
        )
    
    fig_pie.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  
        plot_bgcolor='rgba(0,0,0,0)'    
    )
    
    # Generate pie chart HTML
    pie_chart_html = pio.to_html(fig_pie, full_html=False)
    
    # Generate additional bar chart
    fig4 = px.bar(df4, x='chatbot', y='count', color='qualify',
                 text_auto=True, barmode='group', height=400, 
                 title=df4_title)
    
    start_color = np.array([255, 160, 122])   # RGB for #ADD8E6 (light blue)
    end_color = np.array([211, 211, 211])        # RGB for #2F4F4F (dark slate gray)
    num_bands = 50

    for i in range(num_bands):
        ratio = i / (num_bands - 1)
        interpolated_color = (start_color * (1 - ratio) + end_color * ratio).astype(int)
        color_hex = '#{:02X}{:02X}{:02X}'.format(*interpolated_color)
        
        fig4.add_shape(
            type='rect',
            x0=i / num_bands,  
            y0=0,             
            x1=(i + 1) / num_bands,  
            y1=1,              
            fillcolor=color_hex,
            line=dict(color='rgba(0,0,0,0)'),  
            opacity=1,
            layer='below'
        )
    
    fig4.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  
        plot_bgcolor='rgba(0,0,0,0)'    
    )
    
    additional_bar_chart_html = pio.to_html(fig4, full_html=False)
    
    # Chart 1 and Chart 2 logic remain the same
    df1 = df.groupby(['quest_content_level1', chart_type]).count()['question'].reset_index()
    fig1 = px.bar(df1, x='quest_content_level1', y='question', color=chart_type, 
                 text_auto=True, barmode='group', height=400, 
                 title=f"Chatbot: {chart_type}")

    df2 = df.groupby(['quest_type_cate', chart_type]).count()['question'].reset_index()
    fig2 = px.bar(df2, x='quest_type_cate', y='question', color=chart_type, 
                 text_auto=True, barmode='group', height=400, 
                 title=f"Chatbot: {chart_type}")
    
    for fig in [fig1, fig2]:
        for i in range(num_bands):
            ratio = i / (num_bands - 1)
            interpolated_color = (start_color * (1 - ratio) + end_color * ratio).astype(int)
            color_hex = '#{:02X}{:02X}{:02X}'.format(*interpolated_color)
            
            fig.add_shape(
                type='rect',
                x0=i / num_bands,  
                y0=0,             
                x1=(i + 1) / num_bands,  
                y1=1,              
                fillcolor=color_hex,
                line=dict(color='rgba(0,0,0,0)'),  
                opacity=1,
                layer='below'
            )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',  
            plot_bgcolor='rgba(0,0,0,0)'    
        )    
    
    graph_html1 = pio.to_html(fig1, full_html=False)    
    graph_html2 = pio.to_html(fig2, full_html=False)
    
    return render_template('home.html', 
                           pie_chart_html=pie_chart_html,
                           additional_bar_chart_html=additional_bar_chart_html,
                           chart_html1=graph_html1,
                           chart_html2=graph_html2
                           )

if __name__ == '__main__':
    app.run(debug=True)