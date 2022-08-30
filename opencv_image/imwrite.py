#写入图片
import cv2


img = cv2.imread("resources\image\cat.jpeg",0)
cv2.imshow("img",img)
k = cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('out\catgray.jpeg',img)
    cv2.destroyAllWindows()