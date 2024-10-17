import os
import streamlit as st
import google.generativeai as genai
from openai import OpenAI
from PIL import Image as PILImage

# Initialize OpenAI client (if needed)
#openai_client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])  # Replace with your actual key

# Initialize Google Generative AI client
genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])  # Replace with your actual key

# Example of initializing a generative model with Google Generative AI for IT product search
it_product_model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="""
        You are an IT product identifier.
        The user will upload an image of an IT device (laptop, mouse, keyboard, etc.).
        Analyze the image and identify the product in terms of brand, model, and general specs.
        Provide suggestions for similar products based on the image, including product category, popular brands, and other key information.
        Output Contains:
        1. Identification of the product (brand, model).
        2. Brief specs or features (if recognizable).
        3. Suggestions for similar or related products.
    """
)

# Function for analyzing the uploaded image of an IT product
def it_product_analysis(image):
    user_message = "Identify and describe the product in the uploaded image."

    # Pass the image and prompt to the model for analysis
    response = it_product_model.generate_content([
        "Identify the IT product in the image", image
    ])

    return response.text.strip()


