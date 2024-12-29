from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    # Sample data
    df1 = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Pears", "Grapes"],
        "Amount": [10, 15, 7, 5]
    })
    df2 = pd.DataFrame({
        "Country": ["USA", "Canada", "Mexico", "Brazil"],
        "Population (Millions)": [331, 38, 128, 213]
    })
    
    # Create a Plotly chart
    fig = px.bar(df1, x="Fruit", y="Amount", title="Fruit Amounts")

    # Convert the Plotly figure to HTML
    graph_html1 = pio.to_html(fig, full_html=False)
    
    # Create the second Plotly chart
    fig2 = px.pie(df2, names="Country", values="Population (Millions)", title="Country Populations")
    graph_html2 = pio.to_html(fig2, full_html=False)

    # Render the template with both charts
    return render_template("index.html", 
                           graph_html1=graph_html1, 
                           graph_html2=graph_html2)

if __name__ == "__main__":
    app.run(debug=True)
