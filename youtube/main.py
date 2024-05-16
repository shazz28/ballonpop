#main pipeline

import cv2
from FindingBallons import*
from dtectHit import*

img =cv2.imread("img.png")

imgBalloons, bboxs = findBalloons(img)
img = detectHit(img, bboxs)

img = cv2.resize(img,(0,0),None, 0.6, 0.8)
#cv2.imshow("output",img)
cv2.imshow("imballons",imgBalloons)
cv2.waitKey(0)