from cgitb import grey
import cv2
img = cv2.imread("poster.jpg")

rocketthatisverycool = img[120:360,400:500]
img[0:240,500:600]=rocketthatisverycool

cv2.imshow("display poster",img)
cv2.waitKey(0)