import numpy as np
import cv2
cam=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(D:\\ANACONDA\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml)
eye_cascade = cv2.CascadeClassifier(D:\\ANACONDA\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml)
while True:
    ret , img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow("img",img)     
    '''for i in range (0,10):
        cv2.waitKey(1000)
        x = str(i)
        x=x+".jpg"
        #print(x)
        cv2.imwrite(x,img)'''
    if cv2.waitKey(3)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()












