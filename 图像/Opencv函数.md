# Opencv函数
## 1. 创建和显示窗口
* namedWindow()		创建命名窗口
* imshow()	显示窗口
* destroyAllwindows()	关闭窗口
* resizeWindow()	改变窗口大小
* waitKey()		等待用户键入
```python
import cv2 as cv

# cv.namedWindow('new',cv.WINDOW_AUTOSIZE)
# WINDOW_NORMAL 可以让窗口大小变得可以调节
cv.namedWindow('new',WINDOW_NORMAL)
# 修改窗口大小
cv.resizeWindow('new',1920,1080)
cv.imshow('new',0)
# waitKey 方法表示等待按键，0表示任何按键，其他整数表示等待按键的时间，单位是毫秒，超过时间没有发生按键操作窗口会自动关闭
# 会返回ASCLL的值
key = cv.waitKey(0)
if key == ord('q'):
	exit()

cv.destroyAllwindows()
```
## 2. 加载显示图片
* imread(path,flag)：使用imread可以读取图片，默认读取的是彩色图片
```python
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 读取图片
img = cv.imread()
```
使用Opencv读取图片和使用matplotlib读取图片后，显示的结果不一样，原因是Opencv读取的颜色通道是按照BGR(蓝绿红)排列的，一般颜色通道是按照RGB来排列的
```python
cv.imshow('cat',img)
cv.waitKey(0)
cv.destroyAllwindows()
```
可以把显示图片的方法封装为一个函数：
```python
def cv_show(name,img):
	cv.imshow(name,img)
	cv.waitKey(0)
	cv.destroyAllwindows()
```
## 3. 修改图片尺寸
cv.resize()

















