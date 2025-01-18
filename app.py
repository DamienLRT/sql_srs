import streamlit as st
import pandas as pd
import duckdb

st.write("Hello wolrd!")
data ={"a": [1,2,3], "b" : [4,5,6]}

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    input_text =st.text_area(label ="entrez votre input")
    st.write(input_text)

