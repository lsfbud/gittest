from cv2 import cv2
import numpy 
from PIL import Image
import pytesseract
#、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
#西门子PLC连接
'''
import snap7
plc=snap7.client.Client()
plc.connect('192.168.1.11',0,1)
'''
#西门子PLC连接
#、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、、
# 从摄像头中取得视频
cap = cv2.VideoCapture(0) # 从摄像头中取得视频
# 获取视频播放界面长宽
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
 
# 定义编码器 创建 VideoWriter 对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
 
while(cap.isOpened()):

    #读取帧摄像头
    ret, frame = cap.read()
    if ret == True:
        #输出当前帧
        out.write(frame)
 
        cv2.imshow('My Camera',frame)
 
        #键盘按 Q 退出
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break
    # 释放资源
out.release()
cap.release()
cv2.destroyAllWindows()
