# **ArchiVoyage - Architectural Style Detection**

![ArchiVoyage Logo](Logo/ArchiVoyage.png)

## **Overview**

**ArchiVoyage** is a Deep learning application that detects architectural styles from images of buildings. Leveraging a fine-tuned ResNet50 model, it identifies architectural styles and provides detailed information about the recognized style. Additionally, users can explore nearby architectural landmarks based on their location. The project is built with a deep learning model, FastAPI for backend services, and Streamlit for the frontend.

## **Features**

- **Style Detection**: Upload an image of a building, and the model predicts the architectural style with confidence scores.
- **Style Information**: After detecting the style, the app provides detailed information about the architectural style using OpenAI's GPT-3.5 model.
- **Discover Nearby Attractions**: Based on your location, the app suggests nearby architectural landmarks of interest.

## **Project Structure**

```bash
.
├── backend
│   ├── archi_rec
│   │   ├── archi_detection.py  # Core model for style detection
│   └── archi_style
│       └── API
│           └── fast.py  # FastAPI backend service for image processing
├── frontend
│   └── app.py  # Streamlit frontend application
├── model
│   └── resnet50_finetune_architecture.pkl  # Trained model
├── notebook
│   └── Streamlit-app.ipynb  # Jupyter notebook for model development
├── raw_data
│   └── architectural-styles-dataset  # Dataset used for training
├── Dockerfile  # Docker configuration
├── requirements.txt  # Python dependencies
└── README.md  # Project documentation
```

## Usage

### Upload Image
Upload an image of a building via the frontend.

### Style Detection
The app will predict the architectural style and display the result along with the confidence score.

### Style Information
The app provides additional details about the detected architectural style using GPT-3.5.

### Discover Nearby Attractions
Enter your location, and the app will suggest nearby architectural landmarks to explore.

## Model Details
The architectural style detection model is based on ResNet50, a deep convolutional neural network. The model has been fine-tuned on a custom dataset containing various architectural styles.

### Key Styles Detected
- Art Deco
- Baroque
- Gothic
- Byzantine
- Postmodern
- And many more.

## Workflows

### Image Preprocessing
1. **Load Image**: Accept an image input from the user.
2. **Resize**: Resize the image to 256x256 pixels.
3. **Normalize**: Normalize the image using ImageNet mean and standard deviation.

### Style Detection
The processed image is passed through the ResNet50 model to predict the architectural style.

### Information Retrieval
Once the style is detected, the app fetches relevant information about the style using GPT-3.5.

### Nearby Attractions
Based on user location input, nearby architectural landmarks are suggested.

## Acknowledgements

- The ResNet50 model is pre-trained on ImageNet.
- The architectural dataset for training was curated from various sources.

## Contact

For any inquiries, please contact:

**Loris Duray**  
Email: lorisduray@gmail.com.com  
LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/loris-duray/)

**Abby Wang**  
Email: your.email@example.com  
LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com)


