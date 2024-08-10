import torch
import torchvision.transforms as transforms
from PIL import Image
import cv2
from torchvision import models, transforms

# Define the path to your saved model
MODEL_PATH = '/Users/lorisduray/code/lorisduray/architectural_styles/archi_project/Model/resnet50-architecture-classifier.pth'
model = models.resnet50(pretrained=True)  # Adjust num_classes as needed
model.load_state_dict(torch.load(MODEL_PATH, map_location=torch.device('cpu')))
model.eval()

# Define transformations for input images
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Define the architectural styles (adjust this list based on your model's classes)
styles = [
    'Achaemenid architecture',
    'American craftsman style',
    'American Foursquare architecture',
    'Ancient Egyptian architecture',
    'Art Deco architecture',
    'Art Nouveau architecture',
    'Baroque architecture',
    'Bauhaus architecture',
    'Beaux-Arts architecture',
    'Byzantine architecture',
    'Chicago school architecture',
    'Colonial architecture',
    'Deconstructivism',
    'Edwardian architecture',
    'Georgian architecture',
    'Gothic architecture',
    'Greek Revival architecture',
    'International style',
    'Novelty architecture',
    'Palladian architecture',
    'Postmodern architecture',
    'Queen Anne architecture',
    'Romanesque architecture',
    'Russian Revival architecture',
    'Tudor Revival architecture'
]

def architectural_detection(cv2_img):
    # Convert OpenCV image (BGR) to PIL image (RGB)
    pil_img = Image.fromarray(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))

    # Apply transformations
    img = transform(pil_img).unsqueeze(0)  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(img)

    # Process the output
    _, predicted = torch.max(output, 1)
    class_index = predicted.item()

    # Return the architectural style
    return styles[class_index]
