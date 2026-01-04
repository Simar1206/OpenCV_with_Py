import cv2
import numpy as np

path = "C:\\Users\\SHREEJI\\OneDrive\\Desktop\\fluttericon.png"
src = cv2.imread(path)
window_name = "flutterIMAGE"

if src is None:
    print("Could not open or find the image:", path)
    exit(0)
    
img = cv2.rotate(src, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
