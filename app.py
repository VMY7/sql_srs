import streamlit as st
import pandas as pd
import duckdb as db

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cats", "Dogs", "Owls"])

with tab1:
    st.dataframe(df)
    input_text = st.text_input(label="Enter a text")
    st.write(db.sql(input_text))

