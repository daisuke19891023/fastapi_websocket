import requests
import streamlit as st
import os
import logging
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
BACKEND_URL = os.environ.get("BACKEND_URL")


def is_authenticated(id: str, password: str) -> bool:
    temp_id = "hoge"
    temp_pass = "abc123"
    return temp_id == id and temp_pass == password


def main_screen():
    uploadedfile = st.file_uploader("upload")
    if st.button("Check Backend Connection"):
        files = {"file": uploadedfile.getvalue()}
        res = requests.post(f"{BACKEND_URL}/files/", files=files)
        st.write(res.text)


if __name__ == "__main__":
    uploadedfile = st.file_uploader("upload")
    if st.button("Check Backend Connection"):
        files = {"file": uploadedfile.getvalue()}
        res = requests.post(f"{BACKEND_URL}/files/", files=files)
        st.write(res.text)
    # Password Form
    st.title("Welcome APP!")
    # logging.info(f"backend_url is {BACKEND_URL}")
    id_block = st.empty()
    password_block = st.empty()
    id = id_block.text_input('Id')
    password = password_block.text_input("Enter a password", type="password")
    if is_authenticated(id, password):
        id_block.empty()
        password_block.empty()
        # main_screen()
        res = requests.get(f"{BACKEND_URL}/")
        st.write(res.text)

    elif password:
        st.info("Please enter a valid password")
