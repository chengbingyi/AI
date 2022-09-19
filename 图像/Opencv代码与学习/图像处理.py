
import cv2 as cv

# 截取部分图像
img = cv.imread('1.jpg')
pt = img[50:600,50:600]
cv.imshow('pt',pt)
cv.waitKey(0)

# 颜色通道提取

b,g,r = cv.split(img)

print(b,g,r)

# 组合

img = cv.merge((b,g,r))
print(img.shape)


# 只保留 R 通道   将[1080,1920,3]矩阵中的三个通道中只保留 其中一个即可  序号 BGR ---012
cur_img = img.copy()
cur_img[:,:,0] = 0      # 将矩阵中 0 的部分赋值为 0
cur_img[:,:,1] = 0      # 将矩阵中 1 的部分赋值为 0  就只剩 2 的部分
cv.imshow('cur_img',cur_img)
cv.waitKey(0)
# 只保留 G 通道
# 改为
# cur_img[:,:,0] = 0
# cur_img[:,:,2] = 0
#
# 只保留 B 通道
# 改为
# cur_img[:,:,1] = 0
# cur_img[:,:,2] = 0