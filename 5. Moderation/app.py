import gradio as gr
from openai import OpenAI

def Moderation(prompt,  api_key):
    if api_key == '':
        output= gr.Textbox("*** Please provide API Key ***")
    else:
        try:
            client = OpenAI(api_key= api_key)
            response = client.moderations.create(input=prompt)
            output = response.results[0]
        except :
           output = gr.Textbox("*** Please check your API-Key and try again ***")
    return output

title = "Enter your Prompt"
description = """
<img src = "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width=300px>



# Provide OpenAI API Key

# Moderation tool : A fine-tuned model that can detect whether text may be sensitive or unsafe.

 
"""

gr.Interface(    
    Moderation,
    [
      gr.Textbox(label="Enter your Prompt"),
      gr.Textbox(type = 'password',label="Enter your API-Key", placeholder="API-Key", lines=1),
    ]
,outputs="text",
title=title,
description=description,


).launch()