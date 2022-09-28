import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

st.title('🎈 ipyvizzu')

def create_chart():

    # Initialize chart
    chart = Chart(width="640px", height="360px", display="manual")

    # Data
    data_frame = pd.read_csv("https://raw.githubusercontent.com/vizzuhq/ipyvizzu/gh-pages/docs/data/chart_types_eu.csv", dtype={"Year": str, "Timeseries": str})
    data = Data()
    data.add_data_frame(data_frame)

    # Chart
    chart = Chart()
    chart.animate(data)

    chart.animate(
        data.filter(
            """
      [ 'AT', 'BE', 'DE', 'DK', 'ES' ]
      .includes(record.Country_code)
      """
        ),
        Config(
            {
                "channels": {
                    "x": {"set": ["Value 3 (+)", "Country"]},
                    "y": {"set": ["Year", "Joy factors"]},
                    "color": {"set": ["Country"]},
                },
                "title": "Stacked Bar Chart",
            }
        ),
    )

    return chart._repr_html_()


create_chart()


