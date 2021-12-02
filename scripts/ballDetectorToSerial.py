from __future__ import division
import cv2
import numpy as np
import time
import serial #for Serial communication
import struct

from serial.serialutil import Timeout

arduino = serial.Serial('/dev/ttyACM0',115200) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

def nothing(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
counter=0
separator = ","
start = "<"
end = ">"
while True:
    timeCheck = time.time()
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

#    l_b = np.array([l_h, l_s, l_v])
#    l_b = np.array([0, 90, 113])
    l_b = np.array([0, 0, 0]) #v=0 means black
#    u_b = np.array([u_h, u_s, u_v])
#    u_b = np.array([90, 255, 255])
    u_b = np.array([180, 255, 50])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    #cv2.imshow("frame", frame)
    #cv2.imshow("mask", mask)
    #cv2.imshow("res", res)
    #print(res)
   # print(res.shape)
    #print(res.dtype)
    #print(mask[240,320])

    #key = cv2.waitKey(1)
    #if key == 27:
     #   break



    mask, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    if counter==0:
        default=max(contour_sizes, key=lambda x: x[0])[1]
        counter=counter+1
    if (max(contour_sizes, key=lambda x: x[0])[1]).any :
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    else:
        biggest_contour=default

    
    #cv2.drawContours(frame, biggest_contour, -1, (0,255,0), 3)

    x,y,w,h = cv2.boundingRect(biggest_contour)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    if arduino.isOpen():
        xcor=str(((x+(w/2))))
        ycor=str(((y+(h/2))))
        pos = start + xcor + separator + ycor + end
#        print("x =",xcor)
#        print("y =",ycor)
#        print("pos =",pos)
        
#       arduino.write(bytes(xcor,'utf-8')) for python3
        arduino.write(bytes(pos.encode('utf-8')))
#        time.sleep(0.5) #try to make work with lower sleep time

    #cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    #cv2.drawContours(frame, contours, 3, (0,255,0), 3)
    #cnt = contours[1]
    #cv2.drawContours(frame, [cnt], 0, (0,255,0), 3)

    # Show final output image
    cv2.imshow('colorTest', frame)
	
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
   # print('fps - ', 1/(time.time() - timeCheck))
cap.release()
cv2.destroyAllWindows()
