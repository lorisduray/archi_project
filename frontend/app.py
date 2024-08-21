import streamlit as st
from PIL import Image
import requests
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # You can omit this if it's set in the environment
)

st.title("Architectural Styles Recognition App")
st.write("Upload an image of an architectural style, and the app will identify the style and provide detailed information.")

st.subheader("Step 1: Upload an Image")

file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if file_up:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # Replace with the appropriate API URL
    api_url = "https://archi-project-tajtjxqq6a-uc.a.run.app/upload_image"
    response = requests.post(api_url, files={"img": img_byte_arr})

    if response.status_code == 200:
        labels = response.json()

        st.subheader("Step 2: Recognized Architectural Style")
        st.write(f"**Style Recognized:** {labels['architectural_style']}")
        st.write(f"**Probability:** {labels['probability']*100:.2f}%")

        st.subheader("Step 3: Style Information")
        with st.spinner("Generating detailed information..."):
            try:
                # Create a completion request using the new OpenAI client
                completion = client.completions.create(
                    model="gpt-3.5-turbo",
                    prompt=f"Provide detailed information about the architectural style {labels['architectural_style']}.",
                    max_tokens=150
                )

                # Access the generated text
                generated_text = completion.choices[0].text.strip()
                st.write(generated_text)

            except Exception as e:
                st.error(f"Error generating information: {e}")

    else:
        st.error("There was an error processing the image. Please try again.")


# Step to add location for additional recommendations
st.subheader("Step 4: Discover Nearby Attractions")
st.write("Enter your location to find more buildings and attractions of architectural interest near you.")

location = st.text_input("Your Location")

if location:
    with st.spinner("Fetching nearby attractions..."):
        try:
            # Create a completion request using the new OpenAI client
            prompt = (f"Based on the location '{location}', suggest some notable buildings and architectural attractions to visit. "
                      "Include any interesting landmarks or places of architectural significance.")
            completion = client.completions.create(
                model="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=200
            )

            # Access and display the generated text
            recommendations = completion.choices[0].text.strip()
            st.write("**Nearby Attractions:**")
            st.write(recommendations)

        except Exception as e:
            st.error(f"Error generating recommendations: {e}")
