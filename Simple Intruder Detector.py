import numpy as np
import cv2 
#import os
#from io import *
#from gtts import gTTS
#text1="INTRUDER"
#language='en'
#myobj = gTTS(text=text1, lang=language, slow=False)
#myobj.save('sp.mp3')
cam=cv2.VideoCapture(0)
subtractor=cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=25,detectShadows=True)
count=0
threshold_val=1500
while(True):
    ret,frame=cam.read()
    
    bw=subtractor.apply(frame)
    bw=cv2.GaussianBlur(bw,(5,5),0)
    x,y,ch=frame.shape
    x,y=int(x),int(y)
    #thresh=int(0.23*(x*y))
    ret,bw = cv2.threshold(bw,25,255,cv2.THRESH_BINARY)
    pix=np.count_nonzero(bw)
    if pix > threshold_val:
        print("INTRUDER..")
        
    else:
        print("PASS")
        
    cv2.imshow('mask',bw)
    
    if cv2.waitKey(3)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()