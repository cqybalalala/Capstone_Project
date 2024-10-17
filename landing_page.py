import streamlit as st

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

          <h1>Welcome to IT Devices Suggestion System</h1>
          <p>The IT Devices Suggestion System is an innovative platform designed to help users find the perfect desktop devices tailored to their specific needs. By leveraging advanced data crawling and language models, the system provides personalized recommendations.</p>

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
          <p>Users can input their budget and requirements for a desktop/it product purchase, and the system will crawl data from Amazon to identify suitable devices. Utilizing a language model, it generates recommendations and offers the option for users to receive a copy of the suggestions via email.</p>

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
          <p>This functionality allows users to search for products by uploading images. The system employs a vision-based language model to analyze the uploaded image and retrieve matching products from the database, providing relevant details and links.</p>

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
          <p>In the future, the system aims to partner with PC store vendors to offer assembly services for users who may need assistance building their desktops. Users can select their desired components and opt for professional assembly, ensuring a hassle-free experience.</p>

      </body>
      </html>

  """    
  )
  st.image("service.jpg", use_column_width=True)