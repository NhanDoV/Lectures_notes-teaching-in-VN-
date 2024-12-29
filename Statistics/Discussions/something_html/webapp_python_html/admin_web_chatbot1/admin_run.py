from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd

# Loading data
df = pd.read_excel("user_chat.xlsx")
df = df[['date', 'conversation_id', 'question_id', 'question', 'quest_type_cate', 'quest_content_level2',
         'haiku_answer', 'haiku_qualify', 'haiku_manual_check']]
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S")
# n-review
n_quest_today = len(df[df['date'] >= '2024-07-31'])
n_quest_week = len(df[df['date'] >= '2024-07-24'])
n_quest_month = len(df[df['date'] >= '2024-07-01'])

# n-fail
n_fail_today = len(df[(df['date'] >= '2024-07-31') & (df['haiku_qualify'] == 'FAIL')])
n_fail_inweek = len(df[(df['date'] >= '2024-07-24') & (df['haiku_qualify'] == 'FAIL')])
n_fail_inmonth = len(df[(df['date'] >= '2024-07-01') & (df['haiku_qualify'] == 'FAIL')])

# Launching app
app = Flask(__name__)
@app.route("/")

def index():
    # Sample data
    df1 = df.groupby(['quest_type_cate', 'haiku_qualify']).count()['question'].reset_index()
    df2 = df.groupby(['quest_content_level2', 'haiku_qualify']).count()['question'].reset_index()
    df3 = df['haiku_qualify'].value_counts().reset_index()
    df4 = df['quest_type_cate'].value_counts().reset_index()
    df5 = df['quest_content_level2'].value_counts().reset_index()
        
    # Create a Plotly chart
    fig1 =  px.bar(df1, y="quest_type_cate", color='haiku_qualify', x="question", barmode='group',
                    text_auto=True, title="quest_cate_type by haiky_qualify", width=400)
    fig2 = px.bar(df2, x="quest_content_level2", color='haiku_qualify', y="question", barmode='group',
                    text_auto=True, title="quest_content_level2 by haiky_qualify")    
    fig3 = px.pie(df3, names="haiku_qualify", values="count", title="percentage (overall)")
    fig4 = px.pie(df4, names="quest_type_cate", values="count", title="quest_type_cate (overall)")
    fig5 = px.pie(df5, names="quest_content_level2", values="count", title="quest_content_level2 (overall)")
    
    for fig in [fig1, fig2, fig3, fig4, fig5]:
        fig.update_layout(
            font_family="Courier New",
            font_color="blue",
            title_font_family="Times New Roman",
            title_font_color="red",
            legend_title_font_color="green"
        )
        fig.update_xaxes(title_font_family="Arial")    
    
    # Convert the Plotly figure to HTML
    graph_html1 = pio.to_html(fig1, full_html=False)
    graph_html2 = pio.to_html(fig2, full_html=False)
    graph_html3 = pio.to_html(fig3, full_html=False)
    graph_html4 = pio.to_html(fig4, full_html=False)
    graph_html5 = pio.to_html(fig5, full_html=False)
    graph_html6 = pio.to_html(fig1, full_html=False)

    # Render the template with both charts
    return render_template("index.html", 
                           graph_html1=graph_html1,
                           graph_html2=graph_html2, 
                           graph_html3=graph_html3,
                           graph_html4=graph_html4,
                           graph_html5=graph_html5,
                           graph_html6=graph_html6,
                           n_quest_today=str(n_quest_today),
                           n_quest_week=n_quest_week,
                           n_quest_month=n_quest_month,
                           n_fail_today=n_fail_today,
                           n_fail_inweek=n_fail_inweek,
                           n_fail_inmonth=n_fail_inmonth
                           )

if __name__ == "__main__":
    app.run(debug=True)
