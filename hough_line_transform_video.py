import cv2 as cv
import numpy as np

video = cv.VideoCapture("C:/Users/ASUS/Desktop/Desktop_video/road_car_view6.mp4")

while True:
    ret, frame = video.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])
    mask = cv.inRange(hsv, low_yellow, up_yellow)
    edges = cv.Canny(mask, 75, 150)

    lines = cv.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    if not ret:
        video = cv.VideoCapture("C:/Users/ASUS/Desktop/Desktop_video/road_car_view6.mp4")
        continue

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("edges", edges)
    
    key = cv.waitKey(25)
    if key == 27:
        break

video.release()
cv.destroyAllWindows()
