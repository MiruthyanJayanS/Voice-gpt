from gtts import gTTS
import os

def generate_and_save_voice(story_text, folder_path, language):
    serial_number = len(os.listdir(folder_path)) + 1
    output_file = os.path.join(folder_path, f"audio_{serial_number}.mp3")
    tts = gTTS(text=story_text, lang=language)
    tts.save(output_file)
    return output_file

def play_audio(audio_file):
    os.system(f"start {audio_file}")
