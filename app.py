import streamlit as st
import requests

# Title
new_title = '<p style="font-family:DomaineDisplayNarrow, Georgia, serif; text-align: center; font-size: 42px;"> Welcome to MemoBrain </p>'
st.markdown(new_title, unsafe_allow_html=True)

st.set_page_config(layout="wide")


col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])

with col1:
    st.button("Alzheimer's")
with col2:
    st.button('MRI Images')
with col3:
    st.button('Research')
with col4:
    st.button('News')
with col5:
    st.button('About Us')
with col6:
    st.button('Contact Us')
