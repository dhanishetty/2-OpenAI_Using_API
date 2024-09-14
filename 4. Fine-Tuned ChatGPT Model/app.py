import gradio as gr
from openai import OpenAI

with gr.Blocks() as demo:
    def Chat_bot(prompt, history, api_key):
        if api_key == '':
            output= "Please provide API Key"
        else:
            try:
                messages = [{"role": "system", "content": "you are an English teaching chatbot who replies everything in both English and Korean. but each line should be in English and Korean."}, {"role": "user", "content": prompt}] 
                client = OpenAI(api_key= api_key )
                response = client.chat.completions.create(
                    model="ft:gpt-3.5-turbo-0613:personal::8fjNPFEp",
                    messages=messages,
                    temperature=0 )
                output = response.choices[0].message.content
            except :
                output = "Please check your API-Key and try again"
        return output




    gr.Markdown(
    """
    # Fine-tuned English training ChatGPT model.
    
    <img src = "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width=300px> 
    
    #  Please provide API-Key and start the class
    
    """)
       
    gr.ChatInterface(Chat_bot, 
                        additional_inputs=[
                            gr.Textbox( type = 'password', label="Enter your API-Key", placeholder="API-Key", lines=1)                            
                        ]
                       )  
if __name__ == "__main__":

    demo.launch()

