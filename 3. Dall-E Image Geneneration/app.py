from PIL import Image
import requests 
from openai import OpenAI
import gradio as gr
img1 = "img1.png"
img3 = "img3.png"


def get_image(prompt, api_key):
    if api_key == '':
        output= img1
    else:
        try:
            client = OpenAI(api_key=api_key)
            response = client.images.generate(
                model = "dall-e-3",
                prompt = prompt,
                size = "1024x1024",
                n = 1
            )
            image_url = response.data[0].url
            data = requests.get(image_url).content
            f = open('img.jpg','wb') 
            f.write(data)
            f.close()
            img = Image.open('img.jpg')
        
            output = img
        except :
           output = img3
    return output


title = "Please Provide API-Key and Enter your Prompt"
description = """
<img src = "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width=300px> 

# A model that can generate images given a natural language prompt using DALL-E
"""

gr.Interface(
    get_image,
    [
        gr.Textbox(label="Enter your Prompt",),
        gr.Textbox(type = 'password',label="Enter your API-Key", placeholder="API-Key", lines=1)
    ],
    outputs= gr.Image(type='pil'),
    title=title,
    description=description,
 ).launch()


