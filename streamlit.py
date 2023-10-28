import streamlit as st
import easyocr
import openai
import os
from PIL import Image

openai.api_key='Enter your API key'

img = Image.open(r'C:\Users\shilp\OneDrive\Documents\Luminar\Internship\Toxicity\Toxicity-detector.png')

def main():
    st.sidebar.header('Home')
    selected_section = st.sidebar.radio("", ['About', 'Search by Image', 'Search by Product'])

    if selected_section == "About":
        home_section()

    elif selected_section == 'Search by Image':
        image_section()

    elif selected_section=='Search by Product':
        text_section()


def home_section():
    st.header('Toxicity Detector')
    st.write(
        'This application identifies the product, detects the toxic ingredients in it and its side effects. You can either upload an image or give the name of the product')
    st.image(img)


def image_section():
    st.header("Check Toxicity by Uploading Image")
    st.warning('Upload the image here')
    uploaded_image = st.file_uploader("Upload the image", type=['jpg', 'jpeg', 'png'])

    if st.button('Get Toxic Ingredients and Side Effects'):
        if uploaded_image:

            with open(os.path.join("temp", uploaded_image.name), "wb") as f:
                f.write(uploaded_image.read())

            image_path = os.path.join("temp", uploaded_image.name)
            image = Image.open(image_path)

            reader = easyocr.Reader(['en'], gpu=True)
            results = reader.readtext(image)
            name = ''
            for detection in results:
                text = detection[1]
                name = name + " " + text

            prompt = f"what are the toxic ingredients in '{name}' and its side effects"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300,
                temperature=0.1,
            )
            side_effects = response.choices[0].text.strip()

            st.write(side_effects)
        else:
            st.warning('Please upload an image.')

def text_section():
    st.title('Check Toxicity by Product Name')
    product = st.text_input('Enter the product name')

    if st.button('Get Toxic Ingredients and Side Effects'):
        if product:
            prompt = f"What are the toxic ingredients of '{product}' and its side effects"
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=300,
                temperature=0.1,
            )
            side_effects = response.choices[0].text.strip()
            st.write(side_effects)
        else:
            st.warning('Please enter a product name.')



if __name__ == "__main__":
    main()