import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world!")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)



tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    sql_query = st.text_area(label="Enter your SQL query")
    result = duckdb.query(sql_query).df()
    st.write(f"You entered the following query: {sql_query}")
    st.dataframe(result)
