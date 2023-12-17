from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset , DataLoader
import numpy as np
import os
import torch

folder_path = "./Dataset_png"
for file_name in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file_name)
    image=Image.open(file_path)
    image_tensor=transforms.ToTensor(image)
    if file_name.startswith("front"):
        