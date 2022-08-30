import cv2
from matplotlib import pyplot as plt
#练习
#尝试在OpenCV中加载彩色图像并将其显示在Matplotlib中,
#OpenCV 和 Matplotlib 中的像素排序略有不同。
#OpenCV 遵循 BGR 顺序，而 matplotlib 遵循 RGB 顺序

img1 = cv2.imread("resources\image\cat.jpeg")
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#plt显示
plt.subplot(121).imshow(img1)
plt.subplot(122).imshow(img2)
plt.show()

#opencv显示
cv2.imshow('bgr image',img1)
cv2.imshow('rgb image',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()