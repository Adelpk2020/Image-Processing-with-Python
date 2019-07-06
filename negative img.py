import numpy as np
import cv2
img = cv2.imread('melgy.jpg',0)
#cv2.resizeWindow('Chalie',500,500)
a=np.array(img)
x=img-255
rows=len(img)
cv2.imshow('M Elmlgy',x)
cv2.waitKey(0)
cv2.destroyAllWindows()
