import gradio as gr
import tempfile
from openai import OpenAI
first_alert = "1mp3.mp3"
next_alert = "3mp3.mp3"

def Txt_To_Speech(api_key, model, voice,speed,text):
    if api_key == '':
        output= first_alert
    else:
        try:
           client = OpenAI(api_key=api_key)
           response = client.audio.speech.create(
                model=model,
                voice=voice,
                speed=speed,
                input=text
            )
           with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_file.write(response.content)

            temp_file_path = temp_file.name
           output = temp_file_path 
        except :
           output = next_alert
    return output


with gr.Blocks() as demo:
    gr.Markdown("# TTS Text To Speech using OpenAI ")

    text1 = gr.Textbox(type = 'password',label="Enter your API-Key", placeholder="API-Key", lines=1)
    model = gr.Dropdown(choices=["tts-1", "tts-1-hd"], label="Model", value="tts-1")
    voice = gr.Dropdown(choices=["alloy", "echo", "fable", "onyx", "nova", "shimmer"], label="Voice Options",
                            value="alloy")
    speed = gr.Slider(minimum=0.25, maximum=4.0, value=1.0, step=0.01, label="Speed")

    text = gr.Textbox(label="Please Enter text",placeholder="Enter your Input")


    
        
    
    gr.Interface(
        Txt_To_Speech,
        [
            text1,model,voice,speed,text
        ],
        outputs=gr.Audio(label="Speech Output")
    )

    

demo.launch()
