# 1. 导入所需模块
import cv2
# 2. 使用OpenCV加载视频
# 读取加载视频
cap = cv2.VideoCapture('carMove.mp4')
'''
### 绘制文字 
接口说明： cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

image：要在其上绘制文本的图像
     
text：要绘制的文本字符串
     
org：它是图像中文本字符串左下角的坐标。坐标表示为两个值的元组，即(X坐标值，Y坐标值)
     
font：它表示字体类型  cv2.FONT_HERSHEY_SIMPLEX
     
fontScale：字体相较于最初尺寸的缩放系数。若为1.0f，则字符宽度是最初字符宽度，若为0.5f则为默认字体宽度的一半
     
color：文本字符串的颜色。对于BGR，我们通过一个元组。例如：(255，0，0)为蓝色
     
thickness：它是线的粗细像素
     
lineType：这是一个可选参数，它给出了要使用的行的类型
     
bottomLeftOrigin：这是一个可选参数。如果为true，则图像数据原点位于左下角。否则，它位于左上角
'''
while True:
    status, img = cap.read()
    if status:
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        car_detector = cv2.CascadeClassifier('cars.xml')
        cars = car_detector.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE, (25, 25), (200, 200))
        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 1, cv2.LINE_AA)
        print('实时车流量：', len(cars))

        text = 'car number:' + str(len(cars))
        cv2.putText(img, text, (350, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 2)

        cv2.imshow('output', img)

        key = cv2.waitKey(10)
        if key == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()