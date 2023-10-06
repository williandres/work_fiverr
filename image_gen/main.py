import os
import openai
import urllib.request
openai.api_key = ''

tx = "a kid playing in the park coloring page"

response = openai.Image.create(
            prompt = tx,
            n=1,
            response_format='url',
            size = '512x512')

if "data" in response:
    for key, obj in enumerate(response["data"]):
        filename ='my_image_'+str(key)+".jpg"
        urllib.request.urlretrieve(obj['url'], filename)
