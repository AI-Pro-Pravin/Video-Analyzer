from pydub import AudioSegment
import streamlit as st
import ffmpeg

# Streamlit app layout
st.title("Video Analysis: Speech-to-Text and Sentiment Analysis")

# File upload
#uploaded_file = st.text_input("Upload a video file path",None)
uploaded_file = st.file_uploader("Upload a video file",type=['mp4'])

if uploaded_file is not None:
    # Convert video to audio
    with st.spinner('Extracting audio from video...'):
        audio = AudioSegment.from_file(uploaded_file)
        audio.export('sample1.mp3', format="mp3")

print('done')