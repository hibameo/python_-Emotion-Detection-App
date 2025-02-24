import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# NLTK ke sentiment analyzer ko initialize karna
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Streamlit Title
st.title("🧠 Emotion Detection App")

# User input
user_text = st.text_area("Write something...", "I am feeling great today!")

if st.button("Analyze Emotion"):
    if user_text:
        sentiment_score = sia.polarity_scores(user_text)["compound"]

        # Emotion detection logic
        if sentiment_score > 0.2:
            emotion = "😊 Happy"
        elif sentiment_score < -0.2:
            emotion = "😞 Sad"
        else:
            emotion = "😐 Neutral"

        st.subheader("Detected Emotion:")
        st.write(emotion)
    else:
        st.warning("Please enter some text!")

