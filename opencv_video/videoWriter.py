import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out\output1.avi',fourcc,20.0,(640,480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can`t receive frame (Stream end?). Exiting...")
        break
    #图像进行翻转
    #frame =  cv2.flip(frame,0)
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()