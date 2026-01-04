import cv2
import numpy as np

path = "C:\\Users\\SHREEJI\\OneDrive\\Desktop\\fluttericon.png"
img = cv2.imread(path)

(rows, cols) = img.shape[:2]

m = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated_img = cv2.warpAffine(img, m, (cols,rows))

cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()