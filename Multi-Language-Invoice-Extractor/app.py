from dotenv import load_dotenv
load_dotenv() # loading env variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# To Load Google Gemini Pro Vision and Get Responses
model = genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input, image, prompt):
    '''
    input: system prompt
    image: image file
    prompt: user prompt
    '''
    response = model.generate_content([input, image[0], prompt]) # for specific image-related response
    return response.text

def input_image_details(upload_file):
   if uploaded_file is not None:
       # read the file into bytes
       bytes_data = uploaded_file.getvalue()

       image_parts = [
           {
               'mime_type': uploaded_file.type,
                'data': bytes_data
           }
       ]
       return image_parts
   else:
       raise FileNotFoundError("No file was uploaded")
   

# Streamlit App 
st.set_page_config(page_title="Multi-Language Invoice Extractor")
st.header("Multi-Language Invoice Extractor")
input = st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Upload an image of the invoice...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Invoice.', use_column_width=True)

submit = st.button("Extract Details from the Invoice!")

input_prompt = """
You are an expert in understanding invoices. We will upload an image of an invoice
and you will have to answer any questions based on the uploaded invoice image.
"""

# If the user clicks the submit button

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Gemini's Response:")
    st.write(response)