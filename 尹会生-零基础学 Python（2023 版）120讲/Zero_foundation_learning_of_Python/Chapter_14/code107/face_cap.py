import cv2 as cv

cap = cv.VideoCapture()
num = 1
while cap.isOpened():
    # 捕获摄像头图像
    ret, frame = cap.read()
    # 显示捕获的照片
    cv.imshow("capture_test", frame)
    # 图像刷新的频率
    k = cv.waitKey(1) & 0xFF
    # 设置按键保存照片
    if k == ord('s'):
        # 保存图片
        cv.imencode('.jpg', frame)[1].tofile(f'./train/{str(num)}.jpg')
        num += 1
        print(f"成功保存第{str(num)}张照片")
    elif k == ord(' '):
        break

cap.release()
