from pathlib import Path

import cv2 as cv
import numpy as np
from PIL import Image


def getImageAndLabels(imagePath):
    facesSamples = []
    ids = []

    # 调用人脸分类器（注意自己文件保存的路径，英文名）
    face_detect = cv.CascadeClassifier(
        'C:/CodeEnvironment/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    # 循环读取照片人脸数据
    for imagePath in Path(imagePath).rglob('*.jpg'):
        # 用灰度的方式打开照片
        PIL_image = Image.open(imagePath).convert('L')
        # 将照片转换为计算机能识别的数组OpenCV
        img_numpy = np.array(PIL_image, 'uint8')
        # 提取图像中人脸的特征值
        faces = face_detect.detectMultiScale(img_numpy)
        # 将文件名按"."进行分隔

        id = int(imagePath.stem)
        # 防止无人脸图像
        for (x, y, w, h) in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])

    facesSamples = [cv.resize(img, (200, 200)) for img in facesSamples]

    return facesSamples, ids


faceSamples, ids = getImageAndLabels('train')

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.train(faceSamples, np.array(ids))

recognizer.write('trainer/trainer.yml')
