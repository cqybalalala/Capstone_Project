import os
import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from PIL import Image as PILImage

# Initialize Google Generative AI client
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])  # Replace with your actual key

#Text model
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Who are Donald Trump?')

#model = genai.GenerativeModel("gemini-1.5-flash")
#response = model.generate_content("Write a story about a magic backpack.")
print(response)

