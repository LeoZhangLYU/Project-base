import cv2

pic = cv2.imread('cat.jpg')
cv2.rectangle(pic, (100, 100), (200, 200), (0, 0, 255), 2)
cv2.imshow('pic', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()

# NOTE: 总结
#  OpenCV是实现人脸识别的常用库，它比基于深度学习的库更易验证和学习
#  OpenCV能够进行图片的读取、显示、写入以及使用矩形框标注特定区域，在使用其他库进行人脸识别时，也经常配合OpenCV进行图像的标注工作
