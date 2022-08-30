#读取图片
import cv2

#imread(filename,flags)
    #flags:
        #cv2.IMREAD_COLOR 1 加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
        #cv2.IMREAD_GRAYSCALE 0 以灰度模式加载图像
        #cv2.IMREAD_UNCHANGED -1 加载图像，包括alpha通道
img = cv2.imread("resources\image\cat.jpeg",cv2.IMREAD_UNCHANGED)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows