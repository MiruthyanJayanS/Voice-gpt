import streamlit as st
from utils import story_generator, audio_generator

def main():
    st.title("Bedtime Story Generator")

    user_input = st.text_input("Enter a topic for the bedtime story:")
    api_key = st.text_input("Enter your OpenAI API key:")

    story_files_folder = "story_files"  # Path to the story files folder

    if "story" not in st.session_state:
        st.session_state.story = None

    if st.button("Generate Story"):
        st.info("Generating story...")
        story_text = story_generator.generate_openai_story(user_input, story_files_folder)  # Provide folder path
        st.success("Story generated!")
        st.session_state.story = story_text

    language = st.selectbox("Select the language:", ["en", "fr", "de", "es", "it"])

    if st.session_state.story:
        st.text("Generated Story:")
        st.text(st.session_state.story)

        if st.button("Generate Audio"):
            st.info("Generating audio...")
            audio_file = audio_generator.generate_and_save_voice(st.session_state.story, "audio_files", language)
            st.success("Audio generated!")
            st.audio(audio_file)

if __name__ == "__main__":
    main()
