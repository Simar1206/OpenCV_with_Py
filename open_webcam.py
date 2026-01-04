import cv2
import numpy as np
# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow("Webcam", frame)
    
    #press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()