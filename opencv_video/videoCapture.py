
import cv2

#读取摄像头
#cap = cv2.VideoCapture(0)
#从文件读取视频
cap = cv2.VideoCapture("resources\\video\\11.mp4")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret,frame = cap.read()
    #如果正确读取帧，ret为True
    if not ret:
        print("Can`t receive frame(stream end?).Exiting...")
        break
    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",gray)
    if cv2.waitKey(40) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()