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
    st.markdown('**Welcome to the home page**')
    st.image("ITdevices.jpg", use_column_width=True)
    st.html(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Furniture Haven</title>

        <!-- Link to Google Fonts for Playfair Display -->
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@300;700&display=swap" rel="stylesheet">

        <style>
          body, html {
            height: 100%;
            margin: 0;
            font-family: 'Playfair Display', serif; /* Use Playfair Display for body text */
          }

          .hero {
            height: 100vh; /* Full viewport height */
            background-position: center;
            background-repeat: no-repeat;
            background-size: cover; /* Ensures the image covers the full area */
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center; /* Center alignment vertically */
            justify-content: center; /* Center alignment horizontally */
            transition: background-image 2s ease-in-out; /* Smooth transition when background image changes */
          }

          .tagline {
            position: absolute;
            top: 30px; /* Position the text near the top */
            font-size: 24px;
            color: white;
            font-weight: 700; /* Bold weight for the tagline */
          }

          h1 {
            color: white;
            font-size: 100px; /* Larger text size */
            font-weight: 300; /* Slimmer font weight for the heading */
            text-align: center;
            margin: 0;
            animation: slideUp 2s forwards;
          }

          @keyframes slideUp {
            from {
              transform: translateY(100%);
            }
            to {
              transform: translateY(-50%);
            }
          }
        </style>
        </head>
        <body>

        <div class="hero" id="hero">
          <div class="tagline">Furniture Haven</div> <!-- Furniture Haven text at the top -->
          <h1>Furniture, decor, and</h1>
          <h1>beyond</h1>
        </div>
        <!-- JavaScript for background slideshow -->
        <script>
        const hero = document.getElementById('hero');

        // Array of image paths for the slideshow
        const images = [
          "ITdevices.jpg", 
          "ITdevices.jpg",
          "ITdevices.jpg",
          "ITdevices.jpg",
          "ITdevices.jpg"
        ];

        let currentIndex = 0;

        // Function to change the background image smoothly
        function changeBackground() {
          // Update the background image
          currentIndex = (currentIndex + 1) % images.length;
          hero.style.backgroundImage = `url(${images[currentIndex]})`;
        }

        // Set initial background image
        hero.style.backgroundImage = `url(${images[0]})`;

        // Change the background every 4 seconds
        setInterval(changeBackground, 4000);
        </script>

        </body>
        </html>

        """        
    )

    #st.image("./ITdevices.png")

    #image = Image.open('content/IT deives.png')
    #st.image(image, caption = 'IT Devices')

    #st.image("ITdevices.jpg", caption="") 
def product():
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
    st.write("Welcome to the email section")
    email = st.text_input("Enter your email:")
    if st.button('Send me a copy'):
        to_send_email(email, st.session_state.recommendation, 'Your Copy')
        st.write('Email Sent!')
    

# Create a horizontal navigation menu
selected = option_menu(
    menu_title="IT Devices Suggestion Model",
    options=["Home", "Product Suggestion", "Product Search", "Email"],
    icons=["house", "search", "cloud-upload", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
# Home Section
if selected == "Home":
    home()
# Product Suggestion Section
elif selected == "Product Suggestion":
    product()
# Upload Section
elif selected == "Product Search":
    image()
# Email Section
if selected == "Email":
    email()