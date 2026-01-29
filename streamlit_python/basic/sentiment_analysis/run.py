import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from helper import *

st.set_page_config(page_title="Sentiment Analysis", layout="wide")
st.title("🎭 Rule-Based Sentiment Analysis (VI / EN)")

st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #1e3a8a 40%,
            #2563eb 100%
        );
    }

    /* Make content cards readable */
    section[data-testid="stSidebar"],
    div[data-testid="stMetric"],
    div[data-testid="stPlotlyChart"],
    div[data-testid="stDataFrame"],
    div[data-testid="stMarkdown"],
    div[data-testid="stContainer"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 12px;
    }

    /* Title & text */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #f8fafc;
    }

    /* Text area */
    textarea {
        background-color: rgba(255,255,255,0.08) !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Button */
    button[kind="primary"] {
        background-color: #2563eb !important;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, _, col2 = st.columns([2, 0.1, 7])

with col1:
    st.subheader("📝 Input Text")
    input_text = st.text_area(
        "Enter your text here:",
        height=200,
        placeholder="Ví dụ: ngu vãi lồn"
    )

    if st.button("🔍 Analyze Sentiment", type="primary"):
        if input_text.strip():
            st.session_state.results = calculate_sentiment_scores(input_text)
        else:
            st.warning("Please enter some text!")

with col2:
    c1, _, c2 = st.columns([1, 0.05, 2])

    if 'results' in st.session_state:

        with c1:
            scores, keyword_hits, lang = st.session_state.results
            st.subheader("📊 Results")

            max_sentiment = max(scores, key=scores.get)
            label_map = {
                'positive': '🟢 Positive',
                'negative': '🔴 Negative',
                'neutral': '🟡 Neutral'
            }
            st.metric(
                "Sentiment",
                label_map[max_sentiment],
                f"{scores[max_sentiment]*100:.1f}%"
            )

            # Pie chart
            fig_pie = go.Figure(
                data = [go.Pie(
                    labels = list(scores.keys()),
                    values = list(scores.values()),
                    hole = 0.45,
                    marker_colors = ['#10B981', '#EF4444', '#F59E0B']
                )]
            )
            fig_pie.update_layout(
                height = 300,
                paper_bgcolor = 'rgba(0,0,0,0)',
                plot_bgcolor = 'rgba(0,0,0,0)',
                font_color = 'white',
                legend = dict(
                    orientation = "h",
                    yanchor = "bottom",
                    y = 1.25,
                    xanchor = "center",
                    x = 0.5
                ),
                margin = dict(
                    l = 10,
                    r = 10,
                    t = 40,
                    b = 10
                )
            )

            fig_pie.update_traces(
                domain = dict(x = [0, 1], y = [0, 0.99])
            )

            st.plotly_chart(fig_pie, width='stretch')

        # Keywords
        with c2:
            st.subheader("🏷️ Top Keywords Found & Sentiment-scores")
            top_kw = get_top_keywords(keyword_hits)

            if any(top_kw.values()):
                rows = []
                for cat, kws in top_kw.items():
                    for kw, score in kws:
                        rows.append({
                            'Keyword': kw,
                            'Count': abs(score),
                            'Category': cat.title(),
                            'Label': f"{abs(score):.2f}"
                        })

                df = pd.DataFrame(rows)

                # define height with respect to number of vocabs
                n_words = len(df)

                if n_words <= 3:
                    bar_height = 300
                else:
                    bar_height = n_words * 80

                # generate colors per category
                colors = []
                for cat in df['Category'].unique():
                    mask = df['Category'] == cat
                    count = mask.sum()

                    if cat == 'Negative':
                        shades = generate_shades('#EF4444', count)
                    elif cat == 'Positive':
                        shades = generate_shades('#10B981', count)
                    else:
                        shades = generate_shades('#F59E0B', count)

                    colors.extend(shades)

                df['Color'] = colors

                fig_bar = go.Figure()

                fig_bar.add_trace(go.Bar(
                    x = df['Count'],
                    y = df['Keyword'],
                    orientation = 'h',
                    marker_color = df['Color'],
                    text = df['Label'],                     
                    textposition = 'inside',
                    textfont = dict(
                        size = 16,          # <-- tăng size
                        color = 'white'
                    ),
                    insidetextanchor = 'middle',          
                    hovertemplate = '<b>%{y}</b><br>Score: %{x}<extra></extra>'
                ))

                fig_bar.update_layout(
                    height = bar_height,
                    showlegend = False,
                    paper_bgcolor = 'rgba(0,0,0,0)',
                    plot_bgcolor = 'rgba(0,0,0,0)',
                    font_color = 'white',
                    xaxis = dict(
                        gridcolor = 'rgba(255,255,255,0.1)',
                        zerolinecolor = 'rgba(255,255,255,0.2)',
                        tickfont = dict(size = 13)
                    ),
                    yaxis = dict(
                        categoryorder = 'total ascending',
                        gridcolor = 'rgba(255,255,255,0.05)',
                        tickfont=dict(size=15) 
                    )
                )

                st.plotly_chart(fig_bar, width = 'stretch')

            else:
                st.info("No sentiment keywords detected.")

st.markdown("---")
a1, a2 = st.columns([5, 1])
with a1:
    st.caption("Pure rule-based Vietnamese / English sentiment analysis")
with a2:
    st.caption("NhanDov")