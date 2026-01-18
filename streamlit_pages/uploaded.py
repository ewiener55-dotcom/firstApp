import streamlit as st
import requests

API = "http://127.0.0.1:8000/activities/"

st.title("SUPER FUN APP")
st.header("All Activities")

res = requests.get(API)

if res.status_code == 200:
    for item in res.json():
        st.subheader(item["Title"])
        img_url = item['Image']

        st.image(img_url, width=150)

        st.write("Rating:", item["Rating"])
        st.divider()
else:
    st.error("Could not connect to Django API")
