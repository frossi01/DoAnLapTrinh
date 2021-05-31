import cv2
import numpy as np
import sqlite3
import os
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('E:/New folder/recoginzer/trainningData.yml')
def getProfile(id):

    conn = sqlite3.connect('C:/Users/Administrator/Desktop/data.db')
    query = "SELECT * FROM People WHERE ID=" +str(id)
    cursor = conn.execute(query)

    profile = None

    for row in cursor:
        profile = row
    conn.close()
    return profile
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fontface = cv2.FONT_HERSHEY_SIMPLEX
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        id,confidence = recognizer.predict(roi_gray)
        if confidence < 40:
            profile = getProfile(id)

            if(profile !=None):
                cv2.putText(img, ""+str(profile[1]), (x+10,y+h+30) , fontface, 1, (0,255,0), 2)
        else:
            cv2.putText(img, "Unknow", (x+ 10, y+h+30) , fontface, 1, (0,0,255), 2)
    cv2.imshow('nhan dien',img)
    if(cv2.waitKey(1) == ord('q')):
        break;
cap.release()
cv2.destroyAllWindows()