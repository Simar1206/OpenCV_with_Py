import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

while True:
    rect,frame = cap.read()
    if not rect:
        print("failed to capture a frame")
        break
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)
    
    if result.multi_face_landmarks:
        h,w,_ = frame.shape
        for lm in result.multi_face_landmarks[0].landmark:
            x = int(lm.x * w)
            y = int(lm.y * h)
            cv2.circle(frame, (x,y), (0,255,0), -1)
            
    cv2.imshow("landmarks", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()            
