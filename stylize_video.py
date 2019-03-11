#!/usr/bin/env python3
import os
import re
import sys
import subprocess
import shutil
import numpy as np
from PIL import Image
import cv2
import torch
from torchvision import transforms
from models.transformer_net import TransformerNet
import time

"""
    This file takes a video (mp4) as input and runs it through the style transfer model defined by weights_fname.

    It takes one command line argument; the name of the video you would like to stylize. The file should be placed directly in videos/input.
    (In the future we will just take the entire path including the video name as a command line argument so we can put it wherever we want)
"""

# Get paths and set vars
weights_fname = "4x4.model"
script_path = os.path.dirname(os.path.abspath(__file__))
path_to_weights = os.path.join(script_path, "models", weights_fname)
resolution = (640, 480)

# Path to video input
video_path = './input/videos/'
video_name = sys.argv[1]
frame_path = './input/videos/temp'

# Did we find our file?
found = False

# Cut video into frames
for filename in os.listdir(video_path):
    if (filename.endswith(".mp4") and filename == sys.argv[1]): #or .avi, .mpeg, whatever.
        os.system("ffmpeg -i " + os.path.join(video_path, video_name) + " " +  os.path.join(frame_path, "%d.jpg"))
        found = True

# Exit if video doesn't exist
if(not found):
    print("No file named " + sys.argv[1] + " in directory " + video_path)
    exit()

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

#Iterate over frames and stylize them
index = 0

for filename in os.listdir(frame_path):
    if (filename.endswith(".jpg")):
        print(os.path.join(frame_path, filename))

        im = Image.open(os.path.join(frame_path, filename))
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

        path = './output/videos/temp/'
        path += str(index)
        path += '.jpg'

        cv2.imwrite(path, styled)
    index += 1 

# Convert jpg frames into mp4 
subprocess.call('ffmpeg -f image2 -i output/videos/temp/%d.jpg output/videos/test.mp4', shell=True)

# Remove temporary files
temp1 = 'input/videos/temp'
temp2 = 'output/videos/temp'

for filename in os.listdir(temp1):
    if (filename.endswith(".jpg")):
        os.remove(os.path.join(temp1, filename))

for filename in os.listdir(temp2):
    if (filename.endswith(".jpg")):
        os.remove(os.path.join(temp2, filename))
