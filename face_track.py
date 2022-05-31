# Created by Ram at 12.05.2022

# Enter feature description here

#Scenario: # Enter scenario name here
# Enter steps here
import cv2
import numpy as np
#Adding_DJI_Libraries
from djitellopy import tello
import time

#Calling Drone
me = tello.Tello()
me.connect()
#Getting battery Percentage (Just for Precaution)
print(me.get_battery())

#Starting the VideoStream
me.streamon()
#Takeoff
#me.takeoff()
#taking it to optimal height (Depend on the height of person-mine was 175cm-Ram )
#me.send_rc_control(0, 0, 25, 0)
#Sleep feature for 2.0 sec
time.sleep(2.0)
#face_position_detection
fwd_bwd_range = [6198, 6798]
#PID control -- Incremental PID---- I'm going to integrate the deviation over and over again
pid = [0.4, 0.4, 0]
pError = 0
w, h = 720, 480

def find_my_face(img):
    #creating a face classifier
    faceCascade = cv2.CascadeClassifier("img_stabilizer/haarcascade_frontalface_default.xml")
    #Going to Grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Face_detection
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    #taking containers for storing current values for position and area of the face for position detection
    myFaceList = []
    myFaceListArea = []
    #Framing the face of the image
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        #Face center image_detection
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        #adding both real time values to the
        myFaceList.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceList[i], myFaceListArea[i]]
    else:
        return img, [[0.0], 0]

#PID Control System
def trackF(info, w, pid, pError):
    area = info[1]
    x, y = info[0]
    fb = 0

    error = x - w // 2
    speed = pid[0]*error + pid[1] * (error - pError)
    speed = int(np.clip(speed, -100, 100))

    if area > fwd_bwd_range[0] and area < fwd_bwd_range[1]:
        fb = 0
    elif area > fwd_bwd_range[1]:
        fb = -20
    elif area < fwd_bwd_range[0] and area != 0:
        fb = 20

    #print(speed, fb)
    if x == 0:
        speed = 0
        error = 0
    me.send_rc_control(0, fb, 0, speed)
    return error

#Testing with webcam
#cap = cv2.VideoCapture(0)
while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = find_my_face(img)
    pError = trackF(info, w, pid, pError)
    #print("Area", info[1], "Center", info[0])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break