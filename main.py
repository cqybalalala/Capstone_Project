import streamlit as st
from PIL import Image
import json
import ast
from llmmodel import suggestion_gen 
from llmmodel import json_translate
from webscraping import amazon_scraper_sort
from llmmodel import list_gen
from image_search_function import it_product_analysis
from smtp import send_email



# Define the functions for each page
def home():
    st.write("Welcome to the home page")

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
        if st.button('Send me an copy'):
            gmail = st.text_input('Enter your email:' )
            send_email(gmail, recommendation, 'Your recommendation')

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


# Page navigation using a sidebar
page = st.sidebar.selectbox("Choose a page", ["Home", "Product Suggestion", "Image-based Product Search", "Email"])



# Show the selected page
if page == "Home":
    home()
elif page == "Product Suggestion":
    product()
elif page == "Image-based Product Search":
    image()
elif page == "Email":
    email()