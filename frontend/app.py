import streamlit as st
from PIL import Image
import requests
import io
import openai

openai.api_key ='key_here'

# st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Architectural Styles Recognition App")
st.write("Upload or capture an image of an architectural style, and the app will identify the style and provide detailed information.")

# Image upload or capture section
st.subheader("Step 1: Upload or Capture an Image")

# Upload image
file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Capture image
capture = st.camera_input("Or, take a photo")

if file_up is not None or capture is not None:
    # Use the uploaded image or captured image
    image = Image.open(file_up) if file_up else Image.open(capture)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Just a second...")

    # Convert the image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # Send the image to the API
    api_url = "http://localhost:8000/upload_image"  # Replace with google cloud?
    response = requests.post(api_url, files={"file": img_byte_arr})

    if response.status_code == 200:
        labels = response.json()

        # Display the recognized style and probability
        st.subheader("Step 2: Recognized Architectural Style")
        st.write(f"**Style Recognized:** {labels['architectural_style']}")
        st.write(f"**Probability:** {labels['probability']*100:.2f}%")

        # # Fetch more information using OpenAI GPT
        # st.subheader("Step 3: Style Information")
        # style_info = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=f"Provide detailed information about the architectural style {labels['architectural_style']}.",
        #     max_tokens=150
        # )

        # st.write(style_info.choices[0].text.strip())

    else:
        st.error("There was an error processing the image. Please try again.")
