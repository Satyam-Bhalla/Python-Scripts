import tkinter
import os
import cv2
import numpy as np
from PIL import Image
import random
import sqlite3

top = tkinter.Tk()

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
def hello():
    db_filename = 'face.db'
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    vid_cam = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id = random.randint(1,2000)
    name = input('Enter name :')
    cursor.execute('INSERT INTO data(name,Id) VALUES(?, ?)',(name,face_id))
    connection.commit()
    connection.close()
    count = 0

    assure_path_exists("dataset/")
    while(True):
        _, image_frame = vid_cam.read()
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
            count += 1
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('frame', image_frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        elif count<2:
            break

    vid_cam.release()
    cv2.destroyAllWindows()
    exit()


def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)] 
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')
            img_numpy = np.array(PIL_img,'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)
        return faceSamples,ids
    faces,ids = getImagesAndLabels('dataset')
    recognizer.train(faces, np.array(ids))
    assure_path_exists('trainer/')
    recognizer.write('trainer/trainer.yml')


def recognize():
    db_filename = 'face.db'
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    assure_path_exists("trainer/")
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cam = cv2.VideoCapture(0)

    while True:
        ret, im =cam.read()
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2,5)
        # print(len(faces))
        try:
            for(x,y,w,h) in faces:

                cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
                Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                cursor.execute('select status from data where id = {Id}')
                data = cursor.fetchall()
                connection.commit()
                for d, in data:
                    if d == 1:
                        print('Already marked')
                        exit()
                    else:
                        cursor.execute('update data set status =1 where id ={Id}')
                        connection.commit()
                        cursor.execute('select name from data where id ={Id}')
                        f1 = cursor.fetchall()
                        connection.commit()
                        for h, in f1:
                            ll=1
                        with open('a.txt','a') as f:
                            f.write('{h} is present'+'\n')
                            print('Successful')
                            exit()
        except:   
            exit()
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id), (x,y-40), font, 1, (255,255,255), 3)
        cv2.imshow('im',im) 
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    connection.close()
    cam.release()
    cv2.destroyAllWindows()

def absent():
    db_filename = 'face.db'
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    cursor.execute('Select name from data where status = 0')
    ab = cursor.fetchall()
    connection.commit()
    for b, in ab:
        th=1
    with open('absent.txt','a') as f:
        f.write('{b} is absent\n')
        print('Absent done') 
    connection.close()
B1= tkinter.Button(top,text="Trained",command=train)
B = tkinter.Button(top, text ="Register",command= hello)
B2 = tkinter.Button(top, text ="Recognize",command= recognize)
B3 = tkinter.Button(top, text ="Absent",command= absent)
B.pack(side=tkinter.LEFT)
B1.pack(side=tkinter.RIGHT)
B2.pack(side=tkinter.LEFT)
B3.pack()
top.mainloop()
