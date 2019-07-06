import numpy as np
import cv2
img=cv2.imread('melgy.jpg')
arr=np.array(img)
rows=len(img)
columns=len(img[0])
for x in range(rows):
    for y in range(columns):
        if img[x][y]<=125 :
            img[x][y]=0
        else :
            img[x][y]=255
cv2.imshow("Img 1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()