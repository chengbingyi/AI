import  cv2 as cv

vc = cv.VideoCapture('1.mp4')

# 检查是否打开正确

if vc.isOpened():
    open,frame = vc.read()   # frame = vc.read() -- 一帧一帧读取视频
else:
    open = False

while open:
    ret,frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('result',gray)
        if cv.waitKey(1) & 0xFF == 27:  # waitKey(1) 读取速度  27 表示退出键
            break
vc.release()
cv.destroyAllWindows()





















