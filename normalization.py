import numpy as np
import cv2
img=cv2.imread('melgy.jpg',-1)
arr=np.array(img)
x1=np.min(img)
y1=np.max(img)
g=((img-x1)/y1-x1)*256
cv2.imshow("Img 1",g)
cv2.waitKey(0)
cv2.destroyAllWindows()