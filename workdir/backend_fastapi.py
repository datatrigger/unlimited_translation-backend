from fastapi import FastAPI
from pydantic import BaseModel
import os
import shutil # zip
import spacy # sentence segmentation
from transformers import pipeline # translation

### unzip models

if 'translator_de_en' not in os.listdir():
    shutil.unpack_archive(
        filename = f'translator_de_en.zip',
        extract_dir = '.'
        )

### load models
sentence_segmenter = spacy.load("de_dep_news_trf")
translator_de_en = pipeline("translation", model='translator_de_en')

def translate_de_en(text):
    '''Translate German input ``text`` to English'''
    text_segmented = sentence_segmenter(text)
    text_segmented_str = [*map(lambda sentence: sentence.text, text_segmented.sents)] # See https://spacy.io/usage/linguistic-features/ for details
    sentences_translated = translator_de_en(text_segmented_str)
    translated_text = ' '.join([sentence['translation_text'] for sentence in sentences_translated])
    return translated_text


app = FastAPI()

# Definition of objects sent by POST request
class Text(BaseModel):
    text_de: str

# I don't feel like putting the translation service in the root endpoint, not sure why
@app.get('/')
def home():
    return {'How to': 'Use endpoint /translate'}

# Endpoint for the translation service
@app.post('/translate')
def translate(text: Text):
    return {'text_en': translate_de_en(text.text_de)}