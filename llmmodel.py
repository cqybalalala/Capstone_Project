##The suggestion model

import os
from openai import OpenAI
import json
import streamlit as st

client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])


def suggestion_gen(product, budget, usage, requirement):
  system_prompt = '''
  You are a IT device suggestion generator. Your objective is to assist users—especially those lacking technical knowledge—in
selecting suitable personal or commercial IT devices tailored to their needs and budget.
  Provide a purchase list of customised suggestions based on user's requirement. Only provided the product name and model, with slightly explanation
  Output format example like below
  You might need:
  1. CPU (i5-13000K/ryzen6500x)
  2. GPU (RTX3060Ti)
  3. 512GB SSD (NVMe)
  '''
  prompt = f'I want to buy an {product},My budget is {budget}, my mainly usage is {usage}, I need to {requirement}'

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': prompt}
      ],
      temperature = 1.1,
      max_tokens = 2000
  )
  return response.choices[0].message.content



def list_gen(json_list, budget):
  system_prompt = f'''
  based on the list given, each element of the list represent component of computer. Analse it and choose each product from each component category,the total for all product should not exceed the budget {budget} 
  Suggest two package for me to choose
  generate the result as format below:
  product name:
  price:
  url:
  '''

  response = client.chat.completions.create(
      model = 'gpt-4o-mini',
      messages = [
          {'role': 'system', 'content': system_prompt},
          {'role': 'user', 'content': f"{json_list}"}
      ],
      temperature = 1.1,
      max_tokens = 2000
  )
  return response.choices[0].message.content

def json_translate(suggestion):
    system_prompt = '''
    Translate the list into following format(with only product name):
    ['product_name1', 'product_name2', 'product_name3']
    '''
    response = client.chat.completions.create(
          model = 'gpt-4o-mini',
          messages = [
              {'role': 'system', 'content': system_prompt},
              {'role': 'user', 'content': suggestion }
          ],
          temperature = 1.1,
          max_tokens = 2000
    )

    return response.choices[0].message.content


def product_extract(suggestion):
    system_prompt = '''
    Your will be given an output from a vison model which help users to identify the product. Extract the product from the list and output only the product name. If the model output cannot identify the product name or product model. You need to extract the product type.(eg. mouse)
    '''
    response = client.chat.completions.create(
          model = 'gpt-4o-mini',
          messages = [
              
              {'role': 'system', 'content': '''
              The image shows an Apple Magic Mouse 2.

              Specs:

              Wireless Bluetooth connection
              Rechargeable battery
              Multi-touch surface for gestures
              Compatible with macOS and Windows
              Suggestions for similar products:

              Wireless mice: Logitech MX Master 3, Razer Viper Ultimate, Microsoft Arc Mouse
              Apple Mice: Apple Magic Trackpad 2, Apple Magic Mouse (first generation)
              Other computer accessories: Keyboards, mousepads, webcams
              '''},
              {'role': 'assistant', 'content': 'Apple Magic Mouse 2'},
              {'role': 'system', 'content': system_prompt},
              {'role': 'assistant', 'content': suggestion},
              
          ],
          temperature = 1.1,
          max_tokens = 2000
    )

    return response.choices[0].message.content