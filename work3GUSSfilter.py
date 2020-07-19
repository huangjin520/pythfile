import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("10.jpg", 1)
result = cv2.resize(src, None, fx=0.4, fy=0.4)  # 图片缩放
grayimg = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grayimg,(5,5),0)
ret3,threshimg = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(4,3))
closing = cv2.morphologyEx(threshimg, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(closing, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
drawimg = cv2.drawContours(result, contours, -1, (0, 255, 0), 3)

cv2.imshow('result', drawimg)
cv2.imshow('threshimg', threshimg)
#cv2.imshow('grayimg', grayimg)
print(threshimg)
cv2.waitKey()
cv2.destroyAllWindows()
# 直接灰度化