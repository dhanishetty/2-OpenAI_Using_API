import gradio as gr
from transformers import pipeline
from openai import OpenAI
import numpy as np

transcriber_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")


def voice_commands(api_key, audio):
    if api_key == '':
        output= gr.Textbox("*** Please provide API Key ***")
    else:
        try:
            sr, y = audio
            y = y.astype(np.float32)
            y /= np.max(np.abs(y))
            prompt = transcriber_pipe({"sampling_rate": sr, "raw": y})["text"]
            client = OpenAI(api_key=api_key)
            messages = [{"role": "user", "content": prompt}] 
            model = "gpt-3.5-turbo-1106"
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0
            )
            output = response.choices[0].message.content
        except :
           output = gr.Textbox(" *** Please check your API-Key and try again ***")
    return output

with gr.Blocks() as demo:
    gr.Markdown(
        """
        # Voice Commands to prompt Chatgpt using Whisper.
        # OpenAI's Whisper is used to translate voice to text, to prompt ChatGPT.
        <img src = "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width=300px> 
        """)
    
    gr.Interface(    
        voice_commands,
        [
          gr.Textbox(type = 'password',label="Enter your API-Key", placeholder="API-Key", lines=1),
          gr.Audio(sources=["microphone"])
          
        ],
        [
            "text"
        ]    
    )
demo.launch()