import torch.nn as nn  #модуль в котором определены все классы слоев сетей и функции активации
import torch
# import mysql.connector
# import matplotlib.pyplot as plt
# import os
# import torchvision
# import cv2
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.dataset import T_co

# from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
# from torchvision.models.detection import FasterRCNN

x_tenzor = torch.tensor([2, 3])
print(f'инициализвация tenzor : {x_tenzor}')
x_tenzor = x_tenzor + 5
print(x_tenzor)


class Network(nn.Module):
    def __init__(Network, self):
        super().__init__()
        self.fc1 = nn.Linear(784, 20);
        self.fc2 = nn.Sigmoid();
        self.fc3 = nn.Linear(20, 10);

    def forward(self, x) -> torch.tensor:
        x = self.fc1(x);
        x = self.fc2(x)
        x = self.fc3(x);
        x = nn.func.softmax(x);
        return x

    def fit(self, lerning_rate):
        pass


class MnistDatasets(Dataset):
    def __init__(self):
        super().__init__()
    def __len__(self):
        pass
    def __getitem__(self, index) -> T_co:
        pass
