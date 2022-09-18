import shutil # zip
from transformers import pipeline # translation

# Download translation model
translator_de_en = pipeline("translation", model=f'Helsinki-NLP/opus-mt-de-en')

# Save model to disk
translator_de_en.save_pretrained('translator_de_en')

### The code below can be useful to save space, if .zip files can be used as is
### With the transformers library, we need the folder to be decompressed

# # Make .zip archives
# shutil.make_archive(
#     base_name = 'translator_de_en',
#     format = 'zip',
#     base_dir = 'translator_de_en',
#     root_dir = '.'
# )

# # Delete uncompressed folder
# shutil.rmtree('translator_de_en')

### To download the SpaCy model (not necessary since installed via pip):

# from urllib import request
# spacy_model_url = 'https://github.com/explosion/spacy-models/releases/download/de_dep_news_trf-3.4.0/de_dep_news_trf-3.4.0.tar.gz'
# spacy_model_file = 'de_dep_news_trf-3.4.0.tar.gz'
# request.urlretrieve(spacy_model_url, spacy_model_file)