import streamlit as st
from PIL import Image
import requests
import io
# import openai

# openai.api_key ='key_here'

st.title("Architectural Styles Recognition App")
st.write("Upload an image of an architectural style, and the app will identify the style and provide detailed information.")

st.subheader("Step 1: Upload an Image")

file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Loris here this is another options to take a photo, because by default it is better to keep it as button from GUI perspective
# with st.expander("Or, capture an image using your camera"):
#     capture = st.camera_input("Take a photo")

if file_up : # or capture
    image = Image.open(file_up)
    # if file_up else Image.open(capture)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    # st.write("Just a second...") # I have commented this because it does not make scene this message when we get prediction is showing that it is loading

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    api_url = "http://localhost:8000/upload_image" # Replace with google cloud?
    response = requests.post(api_url, files={"img": img_byte_arr})

    if response.status_code == 200:
        labels = response.json()

        # st.subheader("Step 2: Recognized Architectural Style")
        st.write(f"**Style Recognized:** {labels['architectural_style']}")
        st.write(f"**Probability:** {labels['probability']*100:.2f}%")

        # st.subheader("Step 3: Style Information")
        # style_info = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt=f"Provide detailed information about the architectural style {labels['architectural_style']}.",
        #     max_tokens=150
        # )

        # st.write(style_info.choices[0].text.strip())


    else:
        st.error("There was an error processing the image. Please try again.")
