import cv2 as cv  # opencv读取的格式为 BGR


img = cv.imread("1.jpg")
# print(img)

# 图像的显示，也可以创建多个窗口
cv.imshow("image",img)  # ("窗口名称",显示的图片)

# 等待时间，毫秒级，0表示任意键停止
cv.waitKey(0)
cv.destroyAllWindows()

print(img.shape)
print(type(img))
print(img.size)
















