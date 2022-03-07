# import cv2
# import numpy as np

# # print("Package imported")
# #
# # img = cv2.imread("Resources/deer_horns_moon_164191_1600x1200.jpg")


# # cv2.imshow("Photo",img)
# # cv2.waitKey(0)

# import cv2
# import numpy
# webcam = cv2.VideoCapture(0)
# while True:
#     succes,frame = webcam.read()
#     # blur_frame = cv2.GaussianBlur(frame,(7,7),0)
#     cv2.imshow("Original",frame)
#     # cv2.imshow("Video", blur_frame)
#     if cv2.waitKey(1) & 0xFF ==ord('x'):
#         break
# webcam.release()

# print("Package imported")
#
# img = cv2.imread("Resources/deer_horns_moon_164191_1600x1200.jpg")
# # kernel = np.ones((5,5),np.uint8)
# # blur_img = cv2.GaussianBlur(img,(111,111),0)
# # grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # img_edge = cv2.Canny(img,60,1)
# # imgDialation = cv2.dilate(img_edge,kernel)
#


# width,height = 480,720
# cord_1 = np.float32([[515,147],[698,40],[670,419],[853,313]])
# cord_2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv.getPerspectiveTransform(cord_1, cord_2)
# output=cv.warpPerspective(img,matrix,(width,height))
# cv.imshow("Original photo",img)


# print(img.shape)
# imgRes = cv2.resize(img,(680,480))
# cv2.imshow("Photo",imgRes)
# cv2.waitKey(0)

# import cv2
# import numpy as np
#
# img = np.zeros((512,512,3),np.uint8)
# # print(img.shape)
# # img[:]= 235,134,52
# cv2.line(img,(0,0),(500,100),(52, 134, 235))
#
# cv2.imshow("Photo",img)
# cv2.waitKey(0)



import cv2
import numpy as np


def empty(a):
    pass


webcam = cv2.VideoCapture(0)
# while True:
#     succes,frame = webcam.read()
#     # blur_frame = cv2.GaussianBlur(frame,(7,7),0)
#     cv2.imshow("Original",frame)
#     # cv2.imshow("Video", blur_frame)
#     if cv2.waitKey(1) & 0xFF ==ord('x'):
#         break
# webcam.release()


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
    #     # blur_frame = cv2.GaussianBlur(frame,(7,7),0)
    #     cv2.imshow("Original",frame)
    #     # cv2.imshow("Video", blur_frame)
    #     if cv2.waitKey(1) & 0xFF ==ord('x'):
    #         break
    # webcam.release()
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


    cv2.imshow("Final",imgResult)

    cv2.waitKey(1)


# import cv2 as cv
# import numpy as np
#
# path = 'Resources/WIN_20220227_23_10_19_Pro.jpg'
#
#
# def getContour(img):
#     contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
#     for cnt in contours:
#         area = cv.contourArea(cnt)
#         print(area)
#         if area > 100:
#             cv.drawContours(imgContour, cnt, -1, (0, 0, 0), 0)
#             peri = cv.arcLength(cnt, True)
#             approx = cv.approxPolyDP(cnt, 0.02*peri, True)
#             print(len(approx))
#             objcor = len(approx)
#             x, y, w, h = cv.boundingRect(approx)
#
#             if objcor == 3:
#                 object_type = "Tri"
#             elif objcor == 4:
#                 object_type = "Quad"
#             elif objcor > 5:
#                 object_type = "Circle"
#             else:
#                 object_type = "None"
#
#             cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 0, 150), 2)
#             cv.putText(imgContour, object_type,
#                        (x+(w//2)-20, y+(h//2)-40), cv.FONT_HERSHEY_PLAIN, 0.8,
#                        ( 64, 45, 36), 2)
#
#
# img = cv.imread(path)
# imgContour = img.copy()
#
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(img_gray, (111, 111), 1)
# imgCanny = cv.Canny(blur, 50, 50)
# getContour(imgCanny)
#
# img_hor = np.hstack((img, imgContour))
#
# cv.imshow("Canny",imgCanny)
# cv.imshow("Contour",imgContour)
# # cv.imshow("Original",img)
# # cv.imshow("Blur",blur)
# # cv.imshow("Gray Image", img_gray)
# # cv.imshow("Stack", img_hor)
# cv.waitKey(0)


import cv2
import numpy as np


def empty(a):
    pass



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



