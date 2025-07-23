import streamlit as st
import pandas as pd
import duckdb

st.write("""
# SQl SRS
Spaced Repetition System SQL practice
""")

option = st.selectbox(
    "What would you like to review ?",
    ["Joins", "Group By", "Windows Functions"],
    index=None,
    placeholder="Select a theme...",
)

st.write("You selected:", option)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cats", "Dogs", "Owls"])

with tab1:
    st.dataframe(df)
    input_text = st.text_input(label="Enter a text")
    st.write(duckdb.sql(input_text))