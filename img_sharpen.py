import cv2
import numpy as np
import matplotlib.pyplot as plt

path = "C:\\Users\\SHREEJI\\OneDrive\\Desktop\\fluttericon.png"
# Read the image in grayscale
img = cv2.imread(path,0)
# Apply Histogram Equalization
eqimg = cv2.equalizeHist(img)
# Stack the original and equalized images side by side
final_img = np.hstack((img,eqimg))

# Set up the plot
plt.figure(figsize=(10,5))
# Display the original and equalized images
plt.imshow(final_img, cmap='gray')
plt.title("original vs Equalized img")
plt.axis("off")
plt.show()