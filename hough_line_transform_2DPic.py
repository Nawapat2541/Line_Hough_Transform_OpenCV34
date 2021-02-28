import cv2 as cv
import numpy as np

img = cv.imread('C:/Users/ASUS/Desktop/Desktop_pics/pears/Pear1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
edges = cv.Canny(gray, 75, 150)

lines = cv.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=150)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

cv.imshow("Edges", edges)
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
