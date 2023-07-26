import numpy as np
import cv2 as cv

try:
    img = cv.imread('083647_def_MF0.tif', 0)
    print(img)
    img = cv.medianBlur(img,5)
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, dp=100, minDist=100, param1=50, param2=30, minRadius=0, maxRadius=0)
    print(circles)
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        # 绘制外圆
        cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # 绘制圆心
        cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    cv.namedWindow('detected circles', cv.WINDOW_NORMAL)
    cv.imshow('detected circles', cimg)
    cv.waitKey()
    cv.destroyAllWindows()

except Exception as e:
    print("Error:", e)

finally:
    print("hello")