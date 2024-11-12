import streamlit as st
from pandas import *
from main import *
import wikipedia 

kana= None
roumaji= None
type_ = None

st.title("_Streamlit_")

option = st.selectbox(
    "Select ",
    romaji_list(),
    index=None,
    placeholder="Select...",
)
try:
    kana, roumaji, type_ = rom(option)
except:
    pass        

st.write(f"You selected:", kana)
try:
    st.write(f"{wikipedia.summary(kana, sentences = 2)}")
except:
    pass 
try:
    with st.spinner('Wait for it...'):
        wp_page = wikipedia.page(kana)
        list_img_urls = wp_page.images
        for i in list_img_urls:
            if "order" in i:
                st.image(i)
                break
except:
    pass 

