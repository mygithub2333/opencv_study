#画多边形
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()