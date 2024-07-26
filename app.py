# 
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Set the title of the app
st.title("Welcome! To Shayari Generating App!!")

# Display a welcome message
st.write("Hello! Please enter the subject on which you want to generate the Shayari!! Example: 'friendship', 'mom', 'dad', etc... ")

# Create an input text box
subject = st.text_input("Enter your subject:")

# Load the API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Create a submit button
if st.button("Submit"):
    if subject:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Write a Beautyfull shayari about {subject} in English."
        response = model.generate_content(prompt)
        
        # Check if the response contains candidates
        if response.candidates:
            candidate = response.candidates[0]
            if candidate.finish_reason == 'SAFETY':
                st.write("The generated content was blocked due to safety reasons. Please try a different subject.")
            else:
                # Access the text from the response
                content = candidate.content
                parts = content.parts
                shayari = parts[0].text if parts else 'No content generated'
                st.write(shayari)
        else:
            st.write("No content was generated. Please try again with a different subject.")
    else:
        st.write("Please enter a subject.")

