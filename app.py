from moviepy.editor import VideoFileClip
import whisper
from transformers import pipeline
import streamlit as st

model = whisper.load_model('base')
pipe = pipeline(model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

# Streamlit app layout
st.title("Video Analysis: Speech-to-Text and Sentiment Analysis")

# File upload
uploaded_file = st.text_input("Upload a video file path",None)

if uploaded_file is not None:
    # Convert video to audio
    with st.spinner('Extracting audio from video...'):
        video_clip = VideoFileClip(uploaded_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile('sample1.mp3')

    with st.spinner('Transcribing audio...'):
        result = model.transcribe('sample1.mp3',word_timestamps=True)

    st.subheader("Sentiment Analysis")
    for txt in result['segments']:
        prompt = txt['text']
        timestmp = txt['start']
        resp = pipe(prompt)
        label = resp[0]['label']
        score = resp[0]['score']
        st.write(f"At {timestmp} '{prompt}' sentiment is {label} with a score of "+"{:.4f}.".format(score))