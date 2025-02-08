from flask import Flask, render_template, request, jsonify
from speech2text import HindiTranscriber
from text_answer import HindiBot
from text2speech import HindiTTS
import uuid
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio'

transcriber = HindiTranscriber()
bot = HindiBot()
tts = HindiTTS(slow=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        # Save audio file
        audio_file = request.files['audio']
        filename = f"{uuid.uuid4()}.m4a"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)
        
        # STT
        user_text = transcriber.transcribe_audio(audio_url=filepath)
        print('stt')
        
        # LLM Response
        bot_response = bot.get_response(user_text)
        print('llm')
        
        # TTS
        audio_output = f"response_{filename}"
        tts.synthesize_speech(bot_response, 
                            output_file=os.path.join(app.config['UPLOAD_FOLDER'], audio_output))
        print('tts')
        
        return jsonify({
            'user_text': user_text,
            'bot_text': bot_response,
            'audio_url': f'/static/audio/{audio_output}'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)