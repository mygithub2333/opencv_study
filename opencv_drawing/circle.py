#画圆
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()