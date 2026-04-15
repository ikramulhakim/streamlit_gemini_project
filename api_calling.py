from google import genai
from dotenv import load_dotenv
from gtts import gTTS

import os
import io
load_dotenv()

my_api_key= os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=my_api_key)


#note generator
def note_generate(images):

    prompt="""Summarize the picture in note format,make sure to add necessary details and make it concise. 
              add markdown to differentiate sections,in bangla and english both)."""

    response=client.models.generate_content(
        model="gemini-2.5-flash-preview",
        contents=[images,prompt]
        )
    
    return response.text



def audio_generate(text):
    speech=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer



def quiz_generate(images,difficulty):

    prompt=f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"

    response=client.models.generate_content(
        model="gemini-2.5-flash-preview",
        contents=[images,prompt]
        )
    return response.text


