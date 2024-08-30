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

st.subheader("Upload an Image")

file_up = st.file_uploader("Upload a picture of that architectural marvel! We recommend a panoramic shot of the building's exterior—after all, the more we see, the better we can test our architectural expertise. Let's get those walls talking! 🤩", type=["jpg", "jpeg", "png"])

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

        st.subheader("Architectural Style")
        st.write(f"**Style Recognized:** {labels['architectural_style']}")
        # st.write(f"**Probability:** {labels['probability']*100:.2f}%")

        # st.subheader("Step 3: Style Information")
        with st.spinner("Generating detailed information..."):
            try:
                # Create a completion request using the OpenAI client
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"""Provide a detailed and well-structured description of the architectural style known as {labels['architectural_style']}. Organize the response using the following structure, with section titles in bold, and start a new line after each title:

**1) Overview**:
Start with an overview of the style, including its origins, historical context, and time period.

**2) Key Characteristics**:
Describe the defining features of this architectural style, including common materials, structural elements, and decorative details.

**3) Historical Significance**:
Discuss its historical significance, explaining how it influenced architecture during its era and any lasting impact it has had on modern architecture.

**4) Famous Buildings**:
Mention a few famous buildings that exemplify this style. Organize them by points, and start a new line for each point:

   **4.1) Building 1**:
   Provide the name, location, and key architectural features that make this building a notable example of the style.

   **4.2) Building 2**:
   Provide the name, location, and key architectural features that make this building a notable example of the style.

   **4.3) Building 3**:
   Provide the name, location, and key architectural features that make this building a notable example of the style.

Aim for around 400 tokens.""",
                        }
                    ],
                    model="gpt-3.5-turbo",
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
    st.subheader("Discover Nearby Attractions")
    st.write("Drop in the Area where you're hanging out, and we'll reveal some awesome architectural spots nearby!")

    location = st.text_input("Your Location")

    if location:
        with st.spinner("Fetching nearby attractions..."):
            try:
                # Create a completion request using the OpenAI client
                prompt = (f"Based on the '{location}', suggest three notable buildings and architectural attractions to visit. " "Please follow the following format for the returned results:" "1. Name of the tourist attraction building (format: title)" "Next line: Name of the building architectural style (format: one font size smaller than the title)" "Next line: Introduction to the building (format: small font)")
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="gpt-3.5-turbo",
                )

                # Access and display the generated text
                recommendations = chat_completion.choices[0].message.content
                st.write("**Nearby Attractions:**")
                st.write(recommendations)

            except Exception as e:
                st.error(f"Error generating recommendations: {e}")
