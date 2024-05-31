from openai import OpenAI
from .chat_gpt_api_key import API_KEY

def GenerateDescription(details):
    textPost = ''
    with open(details['textFilePath'], 'r') as file:
        textPost = file.readlines()
        textPost = ''.join(textPost)

    prompt = f'Create a TikTok description for the following Reddit story transcript: \"{textPost}\". Make sure to include the hashtags: #Reddit, #redditstories. Please also generate a few more hashtags related to this'

    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ],
        temperature=0.7,
        max_tokens=64,
    )

    details['description'] = response.choices[0].message.content
    print(details['description'])