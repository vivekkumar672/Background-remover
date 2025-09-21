API_KEY = "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"

import openai
import os
from PIL import Image
from imagegenerate import API_KEY

openai.api_key = API_KEY
response = openai.Image.create(prompt = "acat on the chair", n= 1) 