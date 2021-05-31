import cv2
import numpy as np
import sqlite3
import os

def insert0rUpdate(id, name):

    conn = sqlite3.connect('C:/Users/Administrator/Desktop/data.db')

    query = "SELECT * FROM people WHERE ID=" + str(id)
    cusror = conn.execute(query)

    isRecordExist = 0

    for row in cusror:
        isRecordExist = 1

    if(isRecordExist == 0):
        query = "INSERT INTO people(ID, Name) VALUES("+str(id)+",'"+str(name)+ "')"
    else:
        query = "UPDATE people SET Name='"+str(name)+"' WHERE ID="+ str(id)

    conn.execute(query)
    conn.commit()
    conn.close()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
id = input("Enter your ID: ")
name = input("Enter your Naem: ")
insert0rUpdate(id, name)
sampleNum = 0
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        if not os.path.exists('dataSet'):
            os.makedirs('dataSet')
        sampleNum +=1
        cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+ '.jpg', gray[y: y+h, x: x+w])
    cv2.imshow('nhan dien',img)
    cv2.waitKey(1)
    if sampleNum >100:
        break;
cap.release()
cv2.destroyAllWindows()


