import openai

def set_openai_api_key(api_key):
    openai.api_key = api_key

def generate_openai_story(user_input):
    prompt = f"You: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()
