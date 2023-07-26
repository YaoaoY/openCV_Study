import cv2
import numpy as np
from matplotlib import pyplot as plt
url = '083647_def_MF0.tif'
img = cv2.imread(url, cv2.IMREAD_GRAYSCALE)
img_rgb=cv2.imread(url)
temp = cv2.imread('example.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("result", cv2.WINDOW_NORMAL)
x,y=img.shape
tempHt, tempWd = temp.shape
# 归一化相关系数法
result = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
max_before=0
loc = np.where( result >= 0.954)
for max_loc in zip(*loc[::-1]):
    sum=max_loc[0]+max_loc[1]
    if(sum-max_before<=30 )&(sum-max_before>=-30 ):#判定边框之间距离，使一个对象只能使用一个边框框起
        continue
    else:
        cv2.rectangle(img_rgb, max_loc, (max_loc[0]+tempWd, max_loc[1]+tempHt), (255, 5,44), 3)
        #cv2.circle(img_rgb, (max_loc[0]+tempWd/2, max_loc[1]+tempHt/2), 7, (255, 255, 255), -1)
        print('图像左上坐标:',max_loc)
        max_before=max_loc[0]+max_loc[1]
cv2.imshow("result", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()