import torch
import matplotlib.pyplot as plt
import os
path='C:\\Users\\rast1\\Downloads\\dataset\\sdf.png'
from PIL import Image
img=Image.open(path)
plt.imshow(img)
plt.show()
import numpy as np
print(np.arange(1,10,2))