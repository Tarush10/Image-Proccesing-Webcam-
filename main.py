import cv2
import numpy as np



cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,311)
cv2.createTrackbar("Hue Min", "Trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbar", 255, 255, empty)


while True:
    succes, img = webcam.read()
    #blur_frame = cv2.GaussianBlur(img,(7,7),0)
    # cv2.imshow("Original",img)
    #cv2.imshow("Video", blur_frame)


    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbar")
    # print(h_min)
    lower = np.array([h_min, s_min, v_min])                 # lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])                 # upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img, lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original",img)
    cv2.imshow("Final",imgResult)

    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

webcam.release()



