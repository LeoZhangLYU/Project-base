import cv2

# 加载训练数据
recogizer = cv2.face.LBPHFaceRecognizer_create()
recogizer.read('../code108/trainer/trainer.yml')

names = ['BOSS']
idn = [1]


# 识别图片
def face_detect_demo(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 调用人脸分类器
    face_detect = cv2.CascadeClassifier(
        'C:/CodeEnvironment/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    # 读取人脸特征并返回人脸坐标
    face = face_detect.detectMultiScale(gray, 1.3, 5, 0, (100, 100), (800, 800))
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 识别人脸
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        if confidence > 0.5:
            print("陌生人")
        else:
            print("老板来了，自动关闭游戏")

    cv2.imshow('img', img)


cap = cv2.VideoCapture(0)
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(20):
        break
cv2.destroyAllWindows()
cap.release()
