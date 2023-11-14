import cv2
import numpy as np
from matplotlib import pyplot as plt 
cap = cv2.VideoCapture(0)
while True: 
    _,frame = cap.read()
    cv2.circle(frame,(114,151),5,(0,0,255),-1)
    cv2.circle(frame, (605, 89), 5, (0, 0, 255), -1)
    cv2.circle(frame, (72, 420), 5, (0, 0, 255), -1)
    cv2.circle(frame, (637, 420), 5, (0, 0, 255), -1)
    imgPts = np.float32([[114,151],[605, 89],[72, 420],[637, 420]])

    objPoints = np.float32([[0,0],[420,0],[0,637],[420,637]])
    matrix = cv2.getPerspectiveTransform(imgPts,objPoints)
    result = cv2.warpPerspective(frame,matrix,(400,600))
    cv2.imshow('frame',frame)
    cv2.imshow('Perspective Transformation', result)
    key = cv2.waitKey(1)
    plt.show()
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
