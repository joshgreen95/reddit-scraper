import requests
import os

def isMale(content):
    isMaleWords = ['wife', 'girlfriend']
    isFemaleWords = ['husband', 'boyfriend']
    isMaleCounter = 0
    isFemaleCounter = 0 
        
    for word in isMaleWords:
        isMaleCounter += content.count(word)
            
    for word in isFemaleWords:
        isFemaleCounter += content.count(word)  
 
    return(isMaleCounter > isFemaleCounter)


def GenerateVoiceID(isMale):
    if(isMale):
        return 'CYw3kZ02Hs0563khs1Fj';
    else:
        return '21m00Tcm4TlvDq8ikWAM';
    

def GenerateVoice(contentPath):
    with open('elkey.env', 'r') as file:
        XI_API_KEY = file.read()
        file.close()
    CHUNK_SIZE = 1024


    for file in os.listdir(contentPath):
        filePath = contentPath + '/' + file
        
        with open(filePath) as openedFile: 
            contents = openedFile.read()
            VOICE_ID = GenerateVoiceID(isMale(contents))
            OUTPUT_PATH = f'{filePath}.mp3'

            tts_url = f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream'
            
            headers = {
                        'Accept': 'application/json',
                        'xi-api-key': XI_API_KEY
            }

            data = {
                    'text': contents,
                    'model_id': 'eleven_multilingual_v2',
                    'voice_settings': {
                        'stability': 0.05,
                        'similarity_boost': 0.8,
                        'style': 0.0,
                        'use_speaker_boost': True,
                    }
            }
    
            response = requests.post(tts_url, headers=headers, json=data, stream=True)

            if response.ok:
                with open(OUTPUT_PATH, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                        f.write(chunk)
                f.close()

                print('Audio Stream Saved Successfully')
            else:
                print(response.text)
