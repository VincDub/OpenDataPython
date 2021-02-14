import numpy as np
from PIL import Image

arr = np.zeros((3,100,100))
arr = arr.reshape((arr.shape[1],arr.shape[2],arr.shape[0]))
img = Image.fromarray(arr, 'RGB')


from os import environ
environ["OPENCV_IO_ENABLE_JASPER"] = "true"
import cv2

image_path = "F:\\ORTHO_94\\94-2018-0655-6860-LA93-0M20-E080.jp2"
img = cv2.imread(image_path)
cv2.imwrite("test.png", img)




