from pytube import YouTube
import streamlit as st

st.markdown('<h1 align="center"> YOU TUBE VEDIO DOWNLOADER <h1>' , unsafe_allow_html=True)
st.markdown('<h5 align="center">Give link to download vedio from youtube<h5>',unsafe_allow_html=True)
link = st.text_input(" ")
st.markdown('<h5 align="center">select resolution<h5>',unsafe_allow_html=True)
resolution = st.selectbox("",("High","Medium","low"))
st.markdown('<h5 align="center"> flie path to save<h5>',unsafe_allow_html=True)
file_path = st.text_input("")

yt = YouTube(link)
if resolution == "High":
    stream = yt.streams.all()[1]
elif resolution == "Medium":
    stream = yt.streams.all()[5]
else:
    stream = yt.streams.all()[-6]    


stream.download(file_path)

st.markdown('<h1 align="center"> your vedio downloaded <h1>',unsafe_allow_html=True)
