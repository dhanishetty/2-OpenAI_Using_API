import gradio as gr
from openai import OpenAI


def Txt_Generation(prompt, model,temperature, api_key):
    if api_key == '':
        output= gr.Textbox("*** Please provide API Key ***")
    else:
        try:
            messages = [{"role": "user", "content": prompt}]
            client = OpenAI(api_key=api_key) 
            response = client.chat.completions.create(
                model=model,
                temperature=temperature,
                messages=messages   )
            output = response.choices[0].message.content
        except :
           output = gr.Textbox("*** Please check your API-Key and try again ***")
    return output


models = ["gpt-3.5-turbo-1106","gpt-4-0613","gpt-4-32k-0613" ]

title = "Enter your Prompt"
description = """<img src = "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width=300px> 

 # Provide OpenAI API Key, select your model
"""

gr.Interface(    
    Txt_Generation,
    [
      gr.Textbox(label="Enter your Prompt",),
      gr.Dropdown(models, label="choose your Model", value= "gpt-3.5-turbo-1106" ),  
      gr.Slider(minimum=0.1, maximum=1, step=0.1),
      gr.Textbox(type = 'password',label="Enter your API-Key", placeholder="API-Key", lines=1),
    ]
,outputs="text",
title=title,
description=description,


).launch()