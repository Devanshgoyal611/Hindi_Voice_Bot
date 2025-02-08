# Hindi Voice Chatbot 🤖🎤

A web-based chatbot that understands and responds in Hindi using speech-to-text, large language models (LLMs), and text-to-speech technologies.

## Features ✨

- **Speech-to-Text (STT):** Converts Hindi speech to text using AssemblyAI.
- **LLM Chatbot:** Generates contextual Hindi responses using Llama3 via Ollama.
- **Text-to-Speech (TTS):** Converts text responses to Hindi speech using gTTS.
- **Web Interface:** User-friendly UI with voice recording and audio playback.

## Technologies Used 🛠️

- **Backend:** Flask
- **STT:** AssemblyAI API
- **LLM:** Ollama + Llama3
- **TTS:** gTTS (Google Text-to-Speech)
- **Frontend:** HTML/CSS/JavaScript

## Installation 📥

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/hindi-voice-chatbot.git
   cd hindi-voice-chatbot
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables**
   - Create `.env` file:
     ```ini
     ASSEMBLYAI_API_KEY="your_assemblyai_key"
     ```
   - Get API key from [AssemblyAI Dashboard](https://www.assemblyai.com/)

4. **Ollama Setup**
   - Install [Ollama](https://ollama.ai/)
   - Pull Llama3 model:
     ```bash
     ollama pull llama3:8b
     ```
   - Start Ollama server:
     ```bash
     ollama serve
     ```

## Usage 🚀

1. **Start Flask Application**
   ```bash
   python app.py
   ```

2. **Access Web Interface**
   Open `http://localhost:5000` in your browser.

3. **Interact with the Bot**
   - Click microphone icon to start recording
   - Click again to stop recording
   - Wait for text response + audio playback

## Project Structure 📁

```
.
├── app.py                 # Main Flask application
├── speech2text.py         # AssemblyAI speech-to-text integration
├── text_answer.py         # Ollama LLM chatbot logic
├── text2speech.py         # gTTS text-to-speech implementation
├── static/                # Frontend assets
│   └── audio/             # Generated audio files
|   └── style.css
├── templates/             # HTML templates
│   └── index.html         
├── requirements.txt       # Python dependencies
└── .env                   # API keys configuration
```

## Configuration ⚙️

**TTS Options** (in `text2speech.py`):
- Switch between `gTTS` (default) and `ParlerTTS` (requires GPU)
- For ParlerTTS:
  1. Uncomment the ParlerTTS class
  2. Install PyTorch: `pip install torch`
  3. Requires CUDA-enabled GPU

## Troubleshooting 🛠️

**Common Issues:**
- **AssemblyAI Errors:** Verify API key in `.env`
- **Ollama Not Responding:** Ensure `ollama serve` is running
- **Audio Playback Issues:** Check browser console for errors
- **Missing Dependencies:** Run `pip install -r requirements.txt`

## License 📄

MIT License - See [LICENSE](LICENSE)

---

**Acknowledgements:**
- Speech-to-Text by [AssemblyAI](https://assemblyai.com)
- LLM powered by [Ollama](https://ollama.ai/)
- TTS via [gTTS](https://gtts.readthedocs.io/)
``` 