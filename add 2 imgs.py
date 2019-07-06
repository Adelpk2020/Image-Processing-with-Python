import numpy as np
import cv2
img1=cv2.imread('melgy.jpg')
img2=cv2.imread('melgy.jpg')
#img=img1*(1)+img2*(1)
img=cv2.addWeighted(img1,0.2,img2,0.6,1)
arr=np.array(img)
cv2.imshow("Img ",img)
cv2.waitKey(0)
cv2.destroyAllWindows()