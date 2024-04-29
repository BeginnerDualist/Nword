import torch
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

path = 'c:\\users\\rast1\\downloads\\dataset\\sdf.png'
img = Image.open(path)
plt.imshow(img)
plt.show()
print(np.arange(1, 10, 2))
#git revert делает новый коммит коми
#git reset удаляет историю где в команде указывается hash коммита до которого мы хотим удалить
# Отмена всех изменений:
# Если вы хотите отменить все изменения в рабочей директории и вернуться к последнему коммиту,
# выполните следующую команду:
# css
# Copy code
# git reset --hard HEAD
