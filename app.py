import streamlit as st
from bbctest import retrieve_doc
import pandas as pd

data=pd.read_csv('headings.csv')

message = st.text_input('Type a Heading to get relevant matches: ')


if st.button('Search'):
    st.write(retrieve_doc(message,raw_docs=data,colname =  "Article"))
