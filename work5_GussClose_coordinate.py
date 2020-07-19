import cv2#正常，可做副本保存
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('10.jpg', 1)
resize = cv2.resize(src, None, fx=0.4, fy=0.4)  # 图片缩放
grayimg = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)#灰度化

blur = cv2.GaussianBlur(grayimg,(5,5),0)#滤波
#blur = cv2.bilateralFilter(grayimg,9,75,75)
ret3,threshimg = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)#二值化
plt.hist(blur.ravel(),16,[0,200]); plt.show()
#kernel = np.ones((3,3),np.uint8)
kernel =cv2.getStructuringElement(cv2.MORPH_RECT,(4,3))
closing = cv2.morphologyEx(threshimg, cv2.MORPH_CLOSE, kernel)
#img = cv2.erode(threshimg, kernel, iterations=2)
#img = cv2.dilate(img, kernel, iterations=3)
contours, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(resize, contours, -1, (0, 255, 0), 3)
x=len(contours )
for i in range(1,x,1):
    cnt=contours[i]
    M = cv2.moments(cnt)
    #print(M)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print(i,'芽点的坐标：',(cx,cy))
    drawing = cv2.drawContours(resize, contours, i, (0, 255, 0), -1)

print('芽点数量：',x-1 )
cv2.namedWindow("drawing",cv2.WINDOW_AUTOSIZE)

cv2.imshow('drawing', resize )
#cv2.imshow('closing ', closing )
#cv2.imshow('grayimg', grayimg)
#cv2.imshow('blur', blur)
#cv2.imshow('threshimg ', threshimg)
#cv2.imshow('closing ', closing)
#print(threshimg)

#plt.subplot(121)
#plt.imshow(threshimg,'gray')
#plt.title('threshimg')
#plt.xticks([]),plt.yticks([])
#plt.subplot(122)
#plt.imshow(closing,'gray')
#plt.title('closing')
#plt.xticks([]),plt.yticks([])
#plt.show()
titles = [ 'grayimg', 'blur', 'threshimg', 'closing']
images = [ grayimg, blur, threshimg, closing]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
# 直接灰度化