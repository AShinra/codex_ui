import streamlit as st
from pymongo import MongoClient

def gradient_line():
    st.markdown("""
    <div style='height: 4px; 
                background: linear-gradient(90deg, #5f27cd, #48dbfb, #10ac84);
                border-radius: 10px; 
                margin-bottom: 20px;'>
    </div>
    """,
    unsafe_allow_html=True)

@st.cache_resource
def connect_to_client():
    return MongoClient(st.secrets['mongodb']['uri'])

@st.cache_resource
def connect_to_codexdb():
    client = connect_to_client()
    return client['codex']

@st.cache_resource
def connect_to_codex_collections(collection_name):
    db = connect_to_codexdb()
    return db[collection_name]

