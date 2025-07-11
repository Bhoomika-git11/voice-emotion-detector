# emotion_analysis.py
from textblob import TextBlob

def analyze_emotion(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.3:
        return "Happy 😊", polarity
    elif polarity < -0.3:
        return "Sad 😢", polarity
    else:
        return "Neutral 😐", polarity