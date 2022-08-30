#画矩形
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()