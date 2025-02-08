# Code for using ParlerTTS model for text-to-speech synthesis in Hindi. 

# import torch
# from parler_tts import ParlerTTSForConditionalGeneration
# from transformers import AutoTokenizer
# import soundfile as sf

# class ParlerTTS:
#     def __init__(self, model_name="ai4bharat/indic-parler-tts"):
#         self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
#         self.model = ParlerTTSForConditionalGeneration.from_pretrained(model_name).to(self.device)
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.description_tokenizer = AutoTokenizer.from_pretrained(self.model.config.text_encoder._name_or_path)
    
#     def synthesize_speech(self, prompt, output_file="indic_tts_out.wav"):
#         description = "Rohit's voice is slightly expressive and animated speech with a moderate speed and pitch."
#         description_input_ids = self.description_tokenizer(description, return_tensors="pt").to(self.device)
#         prompt_input_ids = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        
#         generation = self.model.generate(
#             input_ids=description_input_ids.input_ids,
#             attention_mask=description_input_ids.attention_mask,
#             prompt_input_ids=prompt_input_ids.input_ids,
#             prompt_attention_mask=prompt_input_ids.attention_mask
#         )
        
#         audio_arr = generation.cpu().numpy().squeeze()
#         sf.write(output_file, audio_arr, self.model.config.sampling_rate)
#         print(f'Text-to-speech synthesis completed. Output saved to {output_file}')

# Example usage
# if __name__ == "__main__":
#     tts = ParlerTTS()
#     tts.synthesize_speech("अरे, तुम आज कैसे हो?")

from gtts import gTTS
import os

class HindiTTS:
    def __init__(self, lang='hi', slow=False):
        self.lang = lang
        self.slow = slow  # Slower pronunciation

    def synthesize_speech(self, text, output_file="output.mp3"):
        try:
            tts = gTTS(text=text, lang=self.lang, slow=self.slow)
            tts.save(output_file)
            return output_file
        except Exception as e:
            print(f"TTS Error: {str(e)}")
            return None