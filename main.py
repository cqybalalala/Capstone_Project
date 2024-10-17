import ast

import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

from email_server import to_send_email
from image_search_function import it_product_analysis
from llmmodel import json_translate, list_gen, suggestion_gen
from webscraping import amazon_scraper_sort


# Define the functions for each page
def home():
    st.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playfair Display Example</title>

            <!-- Link to Google Fonts for Playfair Display -->
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700&display=swap" rel="stylesheet">

            <style>
                body {
                    font-family: 'Playfair Display', serif; /* Use Playfair Display for body text */
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4; /* Light background for contrast */
                }

                h1 {
                    font-size: 55px; /* Set font size to 50 pixels */
                    color: #333; /* Dark color for text */
                    margin-bottom: 20px; /* Add some space below the header */
                }

                p {
                    font-family: 'Playfair Display', serif; /* Ensure the paragraph also uses Playfair Display */
                    font-size: 36px; /* Optional: Set a specific size for paragraph text */
                    color: #555; /* Slightly lighter color for paragraph text */
                }
            </style>
        </head>
        <body>

            <h1>Welcome to Playfair Display</h1>
            <p>This is an example of text using the Playfair Display font at a size of 50 pixels for the header and a more standard size for the body text.</p>

        </body>
        </html>

    """    
    )
    st.image("IT.jpeg", use_column_width=True)
    st.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playfair Display Example</title>

            <!-- Link to Google Fonts for Playfair Display -->
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700&display=swap" rel="stylesheet">

            <style>
                body {
                    font-family: 'Playfair Display', serif; /* Use Playfair Display for body text */
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4; /* Light background for contrast */
                }

                h1 {
                    font-size: 30px; /* Set font size to 50 pixels */
                    color: #333; /* Dark color for text */
                    margin-bottom: 20px; /* Add some space below the header */
                }

                p {
                    font-family: 'Playfair Display', serif; /* Ensure the paragraph also uses Playfair Display */
                    font-size: 22px; /* Optional: Set a specific size for paragraph text */
                    color: #555; /* Slightly lighter color for paragraph text */
                }
            </style>
        </head>
        <body>

            <h1>1. Product Suggesstion </h1>
            <p>This is an example of text using the Playfair Display font at a size of 50 pixels for the header and a more standard size for the body text.</p>

        </body>
        </html>

    """    
    )
    st.image("advice.jpg", use_column_width=True)
    st.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playfair Display Example</title>

            <!-- Link to Google Fonts for Playfair Display -->
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700&display=swap" rel="stylesheet">

            <style>
                body {
                    font-family: 'Playfair Display', serif; /* Use Playfair Display for body text */
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4; /* Light background for contrast */
                }

                h1 {
                    font-size: 30px; /* Set font size to 50 pixels */
                    color: #333; /* Dark color for text */
                    margin-bottom: 20px; /* Add some space below the header */
                }

                p {
                    font-family: 'Playfair Display', serif; /* Ensure the paragraph also uses Playfair Display */
                    font-size: 22px; /* Optional: Set a specific size for paragraph text */
                    color: #555; /* Slightly lighter color for paragraph text */
                }
            </style>
        </head>
        <body>

            <h1>2. Image-Based Product Search Function </h1>
            <p>This is an example of text using the Playfair Display font at a size of 50 pixels for the header and a more standard size for the body text.</p>

        </body>
        </html>

    """    
    )
    st.image("image.jpg", use_column_width=True)
    st.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Playfair Display Example</title>

            <!-- Link to Google Fonts for Playfair Display -->
            <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700&display=swap" rel="stylesheet">

            <style>
                body {
                    font-family: 'Playfair Display', serif; /* Use Playfair Display for body text */
                    margin: 0;
                    padding: 20px;
                    background-color: #f4f4f4; /* Light background for contrast */
                }

                h1 {
                    font-size: 30px; /* Set font size to 50 pixels */
                    color: #333; /* Dark color for text */
                    margin-bottom: 20px; /* Add some space below the header */
                }

                p {
                    font-family: 'Playfair Display', serif; /* Ensure the paragraph also uses Playfair Display */
                    font-size: 22px; /* Optional: Set a specific size for paragraph text */
                    color: #555; /* Slightly lighter color for paragraph text */
                }
            </style>
        </head>
        <body>

            <h1>3. Assemble Service...(Future) </h1>
            <p>Provide </p>

        </body>
        </html>

    """    
    )
    st.image("service.jpg", use_column_width=True)

    

def product():
    st.image("advice.jpg", use_column_width=True)
    st.write("Welcome to the product suggestion page")

    product = st.text_input("What product/package do you want:")
    budget = st.text_input("Enter your budget:")
    usage = st.text_input("Enter the usage:")
    requirement = st.text_input("Enter the requirement:")

    if st.button("Generate"):
        #suggestion = suggestion_gen(budget, usage, requirement)  
        suggestion = suggestion_gen(product, budget, usage, requirement)
        st.write(suggestion)
        category_list = json_translate(suggestion)
        st.write(category_list)
        list2 = ast.literal_eval(category_list)
        list1 = []
        for i in list2:
            st.write(i)
            content = amazon_scraper_sort(i)
            list1.append(content)
        recommendation = list_gen(list1)
        st.write(recommendation)
        st.session_state.recommendation = recommendation
        if st.button('Send me a copy'):
            email()
            

def image():
    st.image("image.jpg", use_column_width=True)
    st.title("IT Product Identifier")

    # Upload an image
    product_image = st.file_uploader("Upload a picture of an IT product", type=["jpg", "jpeg", "png"])

    if product_image is not None:
        # Open and display the uploaded image
        img = Image.open(product_image)
        img.thumbnail((800, 800))  # Resize the image to max 800x800 pixels
        st.image(img, caption="Uploaded IT Product Image", use_column_width=True)

        # Analyze the image for IT product identification
        if st.button("Analyze Product"):
            try:
                result = it_product_analysis(img)
                # Display the result from the it_product_analysis function
                st.write(result)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.write("Please upload a picture of an IT product to identify.")

def email():
    st.image("email.jpg", use_column_width=True)
    st.write("Welcome to the email section")
    email = st.text_input("Enter your email:")
    if st.button('Send me a copy'):
        to_send_email(email, st.session_state.recommendation, 'Your Copy')
        st.write('Email Sent!')
    

# Create a horizontal navigation menu
selected = option_menu(
    menu_title="IT Devices Suggestion Model",
    options=["Home", "Suggestion", "Search", "Email"],
    icons=["house", "search", "cloud-upload", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
# Home Section
if selected == "Home":
    home()
# Product Suggestion Section
elif selected == "Suggestion":
    product()
# Upload Section
elif selected == "Search":
    image()
# Email Section
if selected == "Email":
    email()