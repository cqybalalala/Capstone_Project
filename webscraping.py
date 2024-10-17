import json
import os
import streamlit as st
import requests
from openai import OpenAI

def recommend_product(code):
  client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])
  system_prompt = '''
  You are a IT devices sales man. You will be given a list of prodcut in json format, find the best 3 product with explanation.
  '''

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': code }
      ],
      temperature = 1.1,
      max_tokens = 2000
  )
  return response.choices[0].message.content

def amazon_scraper_sort(product):    
    api_key = st.secrets['SCRAPER_API_KEY']
    url = f"https://www.amazon.com/s?k={product.replace(' ', '+')}"

    payload = {'api_key': api_key, 'url': url}
    resp = requests.get('https://api.ecommerceapi.io/amazon_search', params=payload)

    data = json.loads(resp.text)
    sponsored_products = data["results"]

    # Check if there are products available
    if not sponsored_products:
        print("No products found.")
        return json.dumps({"error": "No products found."})

    # Prepare a list to store valid products with integer total reviews
    valid_products = []
    for product in sponsored_products:
        title = product.get('title', 'Not available')
        price = product.get('price_string', 'Not available')
        stars = product.get('stars', 'Not available')

        # Safely extract total reviews, default to 0 if unavailable
        total_reviews_str = product.get('total_reviews', 'Not available')

        if total_reviews_str.isdigit():  # Check if it's a digit for conversion
            total_reviews = int(total_reviews_str)  # Convert to integer
        else:
            total_reviews = 0  # Default to 0 if not available

        valid_products.append({
            "title": title,
            "price": price,
            "stars": stars,
            "total_reviews": total_reviews,  # Use integer value
            "url": product.get('url', 'Not available')
        })

    # Get the top ten products (without sorting)
    top_ten_products = valid_products[:10]  # Slicing the first 10 products

    # Convert the top ten products to JSON format
    json_output = json.dumps(top_ten_products, indent=2)

    # Display the JSON output

    return json_output

def amazon_scraper(product):
    api_key = st.secrets['SCRAPER_API_KEY']
  url = f"https://www.amazon.com/s?k={product.replace(' ', '+')}"

  payload = {'api_key': api_key, 'url':url}
  resp = requests.get('https://api.ecommerceapi.io/amazon_search', params=payload)
  
  url = f"https://www.amazon.com/s?k={product.replace(' ', '+')}"
  
  data = json.loads(resp.text)
  sponsored_products = data["results"]
  json_data = json.dumps(sponsored_products)

  # Check if there are products available
  if not sponsored_products:
      print("No products found.")
  else:
      # Separate different products and print their details
      for index, product in enumerate(sponsored_products):
          print(f"Product {index + 1}:")
          title = product.get('title', 'Not available')
          price = product.get('price_string', 'Not available')
          stars = product.get('stars', 'Not available')
          total_reviews = product.get('total_reviews', 'Not available')
          url = product.get('url', 'Not available')

          print(f"  Title: {title}")
          print(f"  Price: {price}")
          print(f"  Rating: {stars} stars")
          print(f"  Total Reviews: {total_reviews}")
          print(f"  URL: {url}\n")
        
  return json_data








  
