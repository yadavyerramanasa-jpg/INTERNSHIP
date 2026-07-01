import torch
import clip
from PIL import Image

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load CLIP Model
model, preprocess = clip.load("ViT-B/32", device=device)


# ---------------------------------
# Text Embedding
# ---------------------------------
def get_text_embedding(text):

    with torch.no_grad():

        text_input = clip.tokenize([text]).to(device)

        text_features = model.encode_text(text_input)

        text_features /= text_features.norm(dim=-1, keepdim=True)

    return text_features


# ---------------------------------
# Image Embedding
# ---------------------------------
def get_image_embedding(image_path):

    image = preprocess(
        Image.open(image_path)
    ).unsqueeze(0).to(device)

    with torch.no_grad():

        image_features = model.encode_image(image)

        image_features /= image_features.norm(dim=-1, keepdim=True)

    return image_features