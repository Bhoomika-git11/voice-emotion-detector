# 🎙️ Voice Emotion Detector

> Upload a voice recording, get a transcript and the emotional tone behind the words, all in a clean Streamlit interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-TextBlob-4CAF50)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📖 Overview

**Voice Emotion Detector** turns spoken audio into insight. It takes a `.wav` file, converts the speech to text, and runs sentiment analysis on the transcript to classify the speaker's emotional tone as **Happy**, **Sad**, or **Neutral**, along with a numeric polarity score.

It is lightweight, easy to run locally, and a good starting point for exploring speech processing and NLP together.

## ✨ Features

- 🎧 **Upload WAV audio** directly in the browser
- 🔊 **Built-in audio playback** of the uploaded file
- 📝 **Speech-to-text transcription** using the `SpeechRecognition` library
- 😊 **Emotion classification** (Happy 😊 / Sad 😢 / Neutral 😐) from the transcript
- 📊 **Polarity score** (-1.0 to +1.0) so you can see *how* positive or negative the speech is
- 🖥️ **Simple Streamlit UI** with no frontend code needed
- 🎵 **Sample audio files included** for quick testing

## 🧠 How It Works

```
 ┌──────────────┐    ┌──────────────────┐    ┌──────────────────┐    ┌──────────────┐
 │  Upload .wav │ -> │  Speech-to-Text  │ -> │ Sentiment (NLP)  │ -> │ Emotion +    │
 │  (Streamlit) │    │ SpeechRecognition│    │    TextBlob      │    │ Polarity UI  │
 └──────────────┘    └──────────────────┘    └──────────────────┘    └──────────────┘
```

1. **Upload:** the user uploads a `.wav` file through the Streamlit interface.
2. **Transcribe:** `speech_to_text.py` reads the audio and converts it to text.
3. **Analyze:** `emotion_analysis.py` computes the text's sentiment polarity with TextBlob.
4. **Display:** the app shows the transcript, detected emotion, and polarity score.

### Emotion Rules

| Polarity Score | Detected Emotion |
|----------------|------------------|
| `> 0.3`        | Happy 😊         |
| `< -0.3`       | Sad 😢           |
| `-0.3 to 0.3`  | Neutral 😐       |

## 🛠️ Tech Stack

| Purpose            | Tool                                                              |
|--------------------|-------------------------------------------------------------------|
| Web interface      | [Streamlit](https://streamlit.io/)                                |
| Speech recognition | [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)  |
| Sentiment analysis | [TextBlob](https://textblob.readthedocs.io/)                      |
| Audio handling     | [pydub](https://github.com/jiaaro/pydub)                          |
| Language           | Python                                                            |

## 📁 Project Structure

```
voice-emotion-detector/
├── app.py                # Streamlit app (UI and main flow)
├── speech_to_text.py     # Audio transcription logic
├── emotion_analysis.py   # Sentiment-based emotion classification
├── requirements.txt      # Python dependencies
├── audio_samples/        # Sample .wav files for testing
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip`
- An internet connection (see the note below on transcription)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Bhoomika-git11/voice-emotion-detector.git
cd voice-emotion-detector

# 2. (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
python -m pip install -r requirements.txt
```

### Run the App

```bash
python -m streamlit run app.py
```

Then open the local URL shown in your terminal (usually `http://localhost:8501`).

## 💡 Usage

1. Launch the app.
2. Click **Upload a WAV file** and choose a recording (try one from `audio_samples/`).
3. Wait a moment while the audio is transcribed and analyzed.
4. View the **transcript**, **detected emotion**, and **polarity score**.

**Example output**

```
📝 Transcript: I am so happy with how this turned out!
Detected Emotion: Happy 😊
Polarity Score: 0.62
```

### Using MP3, FLAC, or other formats

Only `.wav` is supported by the uploader. Convert other formats first, for example with `ffmpeg`:

```bash
ffmpeg -i input.mp3 output.wav
```

or with an online converter such as [Convertio](https://convertio.co/).

## ⚠️ Limitations

- **Transcription needs internet.** The current implementation uses `recognize_google()`, which calls the Google Web Speech API. Fully offline use requires swapping in an offline engine (see roadmap).
- **Emotion is inferred from text only.** The model analyzes *what* is said, not *how* it is said, so tone, pitch, and sarcasm are not detected.
- **Three categories.** Output is limited to Happy, Sad, and Neutral.
- **WAV only.** Other formats must be converted first.
- Accuracy depends on audio quality, background noise, and clear English speech.

## 🗺️ Roadmap

- [ ] Fully offline transcription (e.g. Vosk or Whisper)
- [ ] Acoustic emotion detection from pitch, energy, and MFCC features
- [ ] More emotions (Angry, Fearful, Surprised)
- [ ] Support for MP3 / FLAC uploads
- [ ] Live microphone recording
- [ ] Emotion-over-time chart for longer recordings
- [ ] Multi-language support

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## 📄 License

Add a license of your choice (e.g. [MIT](https://choosealicense.com/licenses/mit/)) and reference it here.

## 🙌 Acknowledgements

- Sample audio from [Freesound](https://freesound.org/)
- Built with [Streamlit](https://streamlit.io/), [SpeechRecognition](https://pypi.org/project/SpeechRecognition/), and [TextBlob](https://textblob.readthedocs.io/)

---

⭐ If you found this project useful, consider giving it a star!
