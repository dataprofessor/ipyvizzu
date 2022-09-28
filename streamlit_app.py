import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style

st.title('🎈 ipyvizzu')

def create_chart():

    data_frame = pd.read_csv(
    "https://raw.githubusercontent.com/vizzuhq/ipyvizzu/gh-pages/docs/data/chart_types_eu.csv", dtype={"Year": str, "Timeseries": str}
    )
    data = Data()
    data.add_data_frame(data_frame)

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

    chart.animate(Config({"title": "Trellis Bar Chart", "split": True}))
    
    return chart._repr_html_()


CHART = create_chart()

html(CHART, width=650, height=370)
