import requests
import streamlit as st
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BACKEND_URL = os.environ.get("BACKEND_URL")

st.title("Welcome APP!")

st.write(BACKEND_URL)

if st.button("Style Transfer"):
    res = requests.get(BACKEND_URL)
    st.write(res.text)
