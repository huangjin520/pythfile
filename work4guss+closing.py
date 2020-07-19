import cv2#正常，可做副本保存
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('7.jpg', 1)
resize = cv2.resize(src, None, fx=0.4, fy=0.4)  # 图片缩放
grayimg = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)#灰度化
blur = cv2.GaussianBlur(grayimg,(5,5),0)#滤波
ret3,threshimg = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)#二值化
#kernel = np.ones((3,3),np.uint8)
cv2.imshow('GUSSBLURthreshimg',threshimg)
kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(4,3))
closing = cv2.morphologyEx(threshimg, cv2.MORPH_CLOSE, kernel)
#img = cv2.erode(threshimg, kernel, iterations=2)
#img = cv2.dilate(img, kernel, iterations=3)
contours, hierarcy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
x=len(contours )
for i in range(1,x,1):
  drawing=cv2.drawContours(resize, contours,i, (0, 255, 0), -1)#相当于自动赋值
  cv2.imshow('drawing', drawing)
cv2.namedWindow("drawing",cv2.WINDOW_AUTOSIZE)#可以重新命名
# cv2.imshow('drawing', drawing)#放在循环外面就不规范
cv2.imshow('drawing', drawing )#也可以用python返回值自动命名
cv2.imshow('closing ', closing )
#print(threshimg)
cv2.waitKey()
cv2.destroyAllWindows()
# 直接灰度化

