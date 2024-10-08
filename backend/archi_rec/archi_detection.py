import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
from torchvision import models, transforms
from fastai.vision.all import load_learner, PILImage
import os

# Define the path to your saved model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../model/resnet50_finetune_architecture.pkl')
learn = load_learner(MODEL_PATH)


# # Define transformations for input imagesgit reset HEAD backend/Model/resnet50-architectue-classifier.pth
# transform = transforms.Compose([
#     transforms.Resize((256, 256)),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# ])

# # Define the architectural styles (adjust this list based on your model's classes)
# styles = [
#     'Achaemenid architecture',
#     'American craftsman style',
#     'American Foursquare architecture',
#     'Ancient Egyptian architecture',
#     'Art Nouveau architecture',
#     'Baroque architecture',
#     'Bauhaus architecture',
#     'Beaux-Arts architecture',
#     'Byzantine architecture',
#     'Chicago school architecture',
#     'Colonial architecture',
#     'Deconstructivism',
#     'Edwardian architecture',
#     'Georgian architecture',
#     'Gothic architecture',
#     'Greek Revival architecture',
#     'International style',
#     'Novelty architecture',
#     'Palladian architecture',
#     'Postmodern architecture',
#     'Queen Anne architecture',
#     'Romanesque architecture',
#     'Russian Revival architecture',
#     'Tudor Revival architecture'
# ]

def architectural_detection(cv2_img):
    # Convert OpenCV image (BGR) to PIL image (RGB)
    pil_img = Image.fromarray(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))

    # Convert PIL image to FastAI's PILImage
    fastai_img = PILImage.create(pil_img)

    # # Make prediction
    # pred_class, pred_idx, outputs = learn.predict(fastai_img)

   # Make prediction
    pred, pred_idx, probs = learn.predict(fastai_img)

    # return {"predicted_class": pred, "probability": probs[pred_idx].item()}

    # Return the architectural style
    return pred, probs[pred_idx].item()
