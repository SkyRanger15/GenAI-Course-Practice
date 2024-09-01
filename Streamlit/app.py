import streamlit as st
import pandas as pd
import numpy as np

#Title of the app
st.title("Streamlit test app")
#Display a text
st.write("This is a test app to check the functionalities of Streamlit")
#Display a dataframe
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })
st.write(df)
#Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)