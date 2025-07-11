import streamlit as st
import os
from speech_to_text import transcribe_audio
from emotion_analysis import analyze_emotion

st.set_page_config(page_title="Offline Voice Emotion Detector")
st.title("🎙 Offline Voice Emotion Detector")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file:
    filepath = os.path.join("audio_samples", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(filepath)
    st.info("Transcribing audio...")
    transcript = transcribe_audio(filepath)
    st.success(f"📝 Transcript: {transcript}")

    st.info("Analyzing emotion...")
    emotion, score = analyze_emotion(transcript)
    st.subheader(f"Detected Emotion: {emotion}")
    st.caption(f"Polarity Score: {score}")