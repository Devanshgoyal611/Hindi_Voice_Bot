import assemblyai as aai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class HindiTranscriber:
    def __init__(self, api_key: str = None, language_code: str = 'hi'):
        self.api_key = api_key or os.getenv('ASSEMBLYAI_API_KEY')
        if not self.api_key:
            raise ValueError("ASSEMBLYAI_API_KEY is missing. Provide it explicitly or set it in the environment variables.")
        
        aai.settings.api_key = self.api_key
        self.config = aai.TranscriptionConfig(language_code=language_code)
        self.transcriber = aai.Transcriber(config=self.config)
    
    def transcribe_audio(self, audio_url: str, output_file: str = "response.txt") -> str:
        transcript = self.transcriber.transcribe(audio_url)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcript.text)
        return transcript.text