from utils import story_generator, audio_generator
import os

def main():
    user_input = input("Enter a topic for the bedtime story: ")
    api_key = input("Enter your OpenAI API key: ")
    language = input("Enter the language code (e.g., en, fr, de): ")

    story_text = story_generator.generate_story(user_input, api_key)
    print("Generated Story:")
    print(story_text)

    output_folder = "audio_files"
    os.makedirs(output_folder, exist_ok=True)

    audio_file = audio_generator.generate_and_save_voice(story_text, output_folder, language)
    print("Audio file saved as:", audio_file)

    audio_generator.play_audio(audio_file)

if __name__ == "__main__":
    main()
