import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\SHREEJI\\OneDrive\\Desktop\\fluttericon.png"
img = cv2.imread(path)

half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
bigger = cv2.resize(img, (0,0), fx=2,fy=2)
stretch_near = cv2.resize(img, (780,500), interpolation=cv2.INTER_NEAREST)


Titles = ['original', 'half', 'bigger', 'stretched_near']
images = [img, half,bigger,stretch_near]

for i in range(0,4):
    plt.subplot(2,3,i+1)
    plt.title(Titles[i])
    plt.imshow(images[i])
    
