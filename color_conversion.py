import cv2
import numpy as np

path = "C:\\Users\\SHREEJI\\OneDrive\\Desktop\\fluttericon.png"
src = cv2.imread(path)

grey_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

cv2.imshow("color to grey Img" , grey_img)
cv2.waitKey(0)
cv2.destroyAllWindows()