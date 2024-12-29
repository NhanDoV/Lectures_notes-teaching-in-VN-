from flask import Flask, render_template, request, redirect, url_for
import plotly.express as px
import plotly.io as pio
import pandas as pd

# Load and preprocess data
df = pd.read_excel("data/user_chat.xlsx")
df = df[['date', 'conversation_id', 'question_id', 'question', 'quest_type_cate', 'quest_content_level2',
         'quest_content_level1', 'haiku_answer', 'haiku_qualify', 'haiku_manual_check']]
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S")
df['qualify'] = df['haiku_qualify'].replace({'CHECK': 'PASS'})

# Calculate statistics
date_thresholds = {
    'today': '2024-07-31',
    'this-week': '2024-07-24',
    'this-month': '2024-07-01'
}

def calculate_statistics():
    stats = {}
    for period, start_date in date_thresholds.items():
        mask = df['date'] >= start_date
        stats[f'n_quest_{period}'] = len(df[mask])
        stats[f'n_fail_{period}'] = len(df[mask & (df['haiku_qualify'] == 'FAIL')])
    return stats

stats = calculate_statistics()
print(stats)

# Launching app
app = Flask(__name__)

def generate_bar_chart(df, pie_chart_type, title):
    t = df[pie_chart_type].value_counts().head(3).reset_index().sort_values(by='count', ascending=False)
    t['perc'] = (t['count'] / len(df)).apply(lambda x: f"{(100*x):.2f}%")
    fig = px.bar(t, y=pie_chart_type, x='count', text_auto=True, color=pie_chart_type,
                 hover_data='perc', width=500, height=300, title=title)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1),
        font=dict(size=10, color="green"))
    fig.update_yaxes(title_text='')
    return pio.to_html(fig, full_html=False)

@app.route("/", methods=["GET"])
def index():
    pie_chart_type = request.args.get('pie_chart_type', 'quest_type_cate')
    df_selection = request.args.get('df_selection', 'today')

    if pie_chart_type not in ['quest_type_cate', 'quest_content_level1', 'quest_content_level2']:
        return "Invalid pie chart type", 400

    if df_selection not in date_thresholds:
        return "Invalid DataFrame selection", 400

    selection_date = date_thresholds[df_selection]
    dfe = df[df['date'] >= selection_date]

    bar_chart_htmls = {
        period: generate_bar_chart(df[df['date'] >= start_date], pie_chart_type, f"{period.capitalize()} ({pie_chart_type})")
        for period, start_date in date_thresholds.items()
    }

    # Generate pie chart
    df_pie = dfe[pie_chart_type].value_counts().reset_index()
    df_pie.columns = [pie_chart_type, 'count']
    fig_pie = px.pie(df_pie, names=pie_chart_type, values='count', 
                     title=f"{pie_chart_type}-({df_selection})", width=540, height=400)
    fig_pie.update_layout(
        font_family="Courier New",
        font_color="blue",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green"
    )
    pie_chart_html = pio.to_html(fig_pie, full_html=False)

    # Generate additional bar chart
    df4 = dfe.groupby([pie_chart_type, 'qualify']).count()['question'].reset_index()
    df4.columns = ['cate', 'qualify', 'count']
    fig_bar = px.bar(df4, x='cate', color='qualify', y='count', width=1000, height=400,
                     range_y=(0, df4['count'].max() * 1.1), title=f"Qualification ({df_selection}) by question_type / question_content",
                     barmode='group', text_auto=True)
    fig_bar.update_layout(
        font_family="Courier New",
        font_color="blue",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green"
    )
    additional_bar_chart_html = pio.to_html(fig_bar, full_html=False)

    # Render the template with both charts and statistics
    return render_template(
        "admin_home.html",
        bar_chart_1_html=bar_chart_htmls['today'],
        bar_chart_2_html=bar_chart_htmls['this-week'],
        bar_chart_3_html=bar_chart_htmls['this-month'],
        pie_chart_html=pie_chart_html,
        additional_bar_chart_html=additional_bar_chart_html,
        n_quest_today=stats['n_quest_today'],
        n_quest_week=stats['n_fail_this-week'],
        n_quest_month=stats['n_quest_this-month'],        
        n_fail_today=stats['n_fail_today'],
        n_fail_inweek=stats['n_fail_this-week'],
        n_fail_inmonth=stats['n_fail_this-month']
    )

@app.route("/edit_data", methods=["GET"])
def edit_data():
    ext_df = df[['date', 'question', 'haiku_answer', 'haiku_qualify']]
    ext_df.columns = ['date', 'question', 'answer', 'qualify']
    ext_df = ext_df.sort_values(by='date', ascending=False)
    return render_template("admin_edit.html", df=ext_df)

@app.route("/update_data", methods=["POST"])
def update_data():
    global df
    ext_df = df[['date', 'question', 'haiku_answer', 'haiku_qualify']]
    ext_df.columns = ['date', 'question', 'answer', 'qualify']
    ext_df['date'] = pd.to_datetime(ext_df['date'], errors='coerce')
    ext_df = ext_df.sort_values(by='date', ascending=False)

    for index in request.form:
        if index.startswith('date_'):
            idx = int(index.split('_')[1])
            ext_df.loc[idx, 'question'] = request.form.get(f'question_{idx}')
            ext_df.loc[idx, 'answer'] = request.form.get(f'answers_{idx}')
            ext_df.loc[idx, 'qualify'] = request.form.get(f'qualify_{idx}')

    ext_df.to_excel("data/user_chat_updated.xlsx", index=False)
    return redirect(url_for('edit_data'))

if __name__ == "__main__":
    app.run(debug=True)