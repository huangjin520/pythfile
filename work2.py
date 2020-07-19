import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("7.jpg", 1)
result = cv2.resize(src, None, fx=0.4, fy=0.4)  # 图片缩放
grayimg = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
ret, threshimg = cv2.threshold(grayimg, 130, 255, cv2.THRESH_BINARY_INV)  # 二值化图像
# image, contours, hierarchy = cv2.findContours(threshimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours, hierarchy = cv2.findContours(threshimg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
drawimg = cv2.drawContours(result, contours, -1, (0, 255, 0), 5)

cv2.imshow('result', drawimg)
cv2.imshow('threshimg', threshimg)
#cv2.imshow('grayimg', grayimg)
print(threshimg)
cv2.waitKey()
cv2.destroyAllWindows()
# 直接灰度化
