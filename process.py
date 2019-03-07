from imageio import imread
from matplotlib import pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2

filename = 'samples/extradural-haemorrhage-2.jpg'
image = cv2.imread(filename)
print(image)

# hist,bins = np.histogram(image.ravel(),256,[0,256])
