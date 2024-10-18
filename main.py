import ast

import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

from email_server import to_send_email
from image_search_function import it_product_analysis
from llmmodel import json_translate, list_gen, suggestion_gen, product_extract
from webscraping import amazon_scraper_sort, recommend_product
from landing_page import home


# Define the functions for each page
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
        list2 = ast.literal_eval(category_list)
        list1 = []
        for i in list2:
            content = amazon_scraper_sort(i)
            list1.append(content)
        recommendation = list_gen(list1, budget)
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
                recommended_product = product_extract(result)
                st.write(recommended_product)
                product_result = amazon_scraper_sort(recommended_product)
                st.write(product_result)
                shortlisted_product = recommend_product(product_result)
                st.write(shortlisted_product)
                
                


            
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
    options=["Home", "Suggest", "Search", "Email"],
    icons=["house", "search", "cloud-upload", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)
# Home Section
if selected == "Home":
    home()
# Product Suggestion Section
elif selected == "Suggest":
    product()
# Upload Section
elif selected == "Search":
    image()
# Email Section
if selected == "Email":
    email()