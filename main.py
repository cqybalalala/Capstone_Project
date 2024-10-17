import streamlit as st
from PIL import Image
import json
import ast
from llmmodel import suggestion_gen 
from llmmodel import json_translate
from webscraping import amazon_scraper_sort, recommend_product
from llmmodel import list_gen

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
        
        
            
          
            
             

def image():
    st.write("Welcome to the image-based product search page")
    st.write("Please upload an image of the product you want to search for")

    if st.button("Upload"):
        Image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

        #Image = it_product_analysis(image)
        #st.image(Image)

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