#!/usr/bin/env python3
import os
import re
import numpy as np
from PIL import Image
import cv2
import torch
from torchvision import transforms
from models.transformer_net import TransformerNet
import time


# Get paths and set vars
weights_fname = "redcamtile.pth"
script_path = os.path.dirname(os.path.abspath(__file__))
path_to_weights = os.path.join(script_path, "models", weights_fname)
resolution = (640, 480)

# Change to GPU if desired
device = torch.device("cuda")

# Load PyTorch Model
model = TransformerNet()
with torch.no_grad():
   state_dict = torch.load(path_to_weights)
   for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
   model.load_state_dict(state_dict)
   model.to(device)


directory = './input/videos/temp/'

index = 0

for filename in os.listdir(directory):
    print(os.path.join(directory, filename))

    im = Image.open(os.path.join(directory, filename))
    img = im.resize(resolution)

    # Transforms to feed to network
    small_frame_tensor_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    small_frame_tensor = small_frame_tensor_transform(img)
    small_frame_tensor = small_frame_tensor.unsqueeze(0).to(device)
    
    # Run inference and resize
    output = model(small_frame_tensor).cpu()
    styled = output[0]
    styled = styled.clone().clamp(0, 255).detach().numpy()
    styled = styled.transpose(1, 2, 0).astype("uint8")
    styled_resized = cv2.resize(styled ,(640, 480))

    path = './output/images/'
    path += str(index)
    path += '.jpg'

    cv2.imwrite(path, styled)
    index += 1 