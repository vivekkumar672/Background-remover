API_KEY = "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"

import openai
import requests
from PIL import Image
import os

def generate(text):
    res = openai.Image.create(
        prompt = text,
        n = 1,
        size = "256x256"
    )

    return res["data"][0]["url"]

text = "batman art in red and blue color"
url = generate(text)
response = requests.get(url)
Image.open(response.raw)