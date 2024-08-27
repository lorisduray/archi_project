import streamlit as st
from PIL import Image
import requests
import io
from openai import OpenAI

# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# Initialize OpenAI client
client = OpenAI(
    # This is the default and can be omitted
    api_key= st.secrets["OPENAI_API_KEY"]
)

# Load the logo image
logo = Image.open('Logo/ArchiVoyage.png')

# Display the logo at the top
logo = logo.resize((700, 500))
st.image(logo)

st.write("Upload an image of an architectural style, and the app will identify the style and provide detailed information.")

st.subheader("Step 1: Upload an Image")

file_up = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Variable to control the display of Step 4
show_step_4 = False

if file_up:
    image = Image.open(file_up)
    st.image(image, caption='Uploaded Image.', width=300)

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()

    # Replace with the appropriate API URL
    api_url = "https://archi-project-zogvv4tasa-no.a.run.app/upload_image"
    response = requests.post(api_url, files={"img": img_byte_arr})

    if response.status_code == 200:
        labels = response.json()

        st.subheader("Step 2: Recognized Architectural Style")
        st.write(f"**Style Recognized:** {labels['architectural_style']}")
        st.write(f"**Probability:** {labels['probability']*100:.2f}%")

        st.subheader("Step 3: Style Information")
        with st.spinner("Generating detailed information..."):
            try:
                # Create a completion request using the OpenAI client
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"Provide detailed information about the architectural style {labels['architectural_style']}.",
                        }
                    ],
                    model="gpt-3.5-turbo",
                    max_tokens=200
                )

                # Access the generated text
                generated_text = chat_completion.choices[0].message.content
                st.write(generated_text)

                # If everything is successful, show Step 4
                show_step_4 = True

            except Exception as e:
                st.error(f"Error generating information: {e}")

    else:
        st.error("There was an error processing the image. Please try again.")

# Step 4: Discover Nearby Attractions (Shown only after successful prediction)
if show_step_4:
    st.subheader("Step 4: Discover Nearby Attractions")
    st.write("Enter your location to find more buildings and attractions of architectural interest near you.")

    location = st.text_input("Your Location")

    if location:
        with st.spinner("Fetching nearby attractions..."):
            try:
                # Create a completion request using the OpenAI client
                prompt = (f"Based on the location '{location}', suggest some notable buildings and architectural attractions to visit. "
                          "Include any interesting landmarks or places of architectural significance.")
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="gpt-3.5-turbo",
                    max_tokens=200
                )

                # Access and display the generated text
                recommendations = chat_completion.choices[0].message.content
                st.write("**Nearby Attractions:**")
                st.write(recommendations)

            except Exception as e:
                st.error(f"Error generating recommendations: {e}")
