# 
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st

# Load environment variables
load_dotenv()

# Set the title of the app
st.title("Welcome! AI-Enhanced Content Generation Application!!")

# Display a welcome message
st.write("Features")
st.write("Feature 1: Text Generation")

# Create an input text box
subject = st.text_input("Enter your prompt or Topic:")

# Load the API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Create a submit button
if st.button("Submit"):
    if subject:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"generates creative and contextually relevant text about {subject} in English."
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
        st.write("Please enter a Topic or prompt.")

st.write("Feature 2: Text Summarization")

subject2 = st.text_input("Enter the Topic you want to summarize:")

if st.button("submit"):
    if subject2:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Summarize the given content {subject2} in less then 100 words. Provide the answer in pointers use english language"
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
        st.write("Please enter a Topic or prompt.")

st.write("Feature 3: Language Translation")

content = st.text_input("Provide the content you want to translate:")

language = st.selectbox("Provide the language in which you want the translation:",
("Arabic (ar)",
 "Bengali (bn)",
"Bulgarian (bg)",
"Chinese simplified",
"traditional (zh)",
"Croatian (hr)",
"Czech (cs)",
"Danish (da)",
"Dutch (nl)",
"English (en)",
"Estonian (et)",
"Finnish (fi)",
"French (fr)",
"German (de)",
"Greek (el)",
"Hebrew (iw)",
"Hindi (hi)",
"Hungarian (hu)",
"Indonesian (id)",
"Italian (it)",
"Japanese (ja)",
"Korean (ko)",
"Latvian (lv)",
"Lithuanian (lt)",
"Norwegian (no)",
"Polish (pl)",
"Portuguese (pt)",
"Romanian (ro)",
"Russian (ru)",
"Serbian (sr)",
"Slovak (sk)",
"Slovenian (sl)",
"Spanish (es)",
"Swahili (sw)",
"Swedish (sv)",
"Thai (th)",
"Turkish (tr)",
"Ukrainian (uk)",
"Vietnamese (vi)"))

if st.button("submit", key="translate_button"):
    if language:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Translate the following content to {language}:\n\n{content}"
        response = model.generate_content(prompt)
        st.write("Translation:")
        st.write(response.text)

