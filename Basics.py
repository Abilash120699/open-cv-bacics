#Read an image
import cv2
print("package imported")

img = cv2.imread("resouces/joker.jpg")

cv2.imshow("output",img)
cv2.waitKey(0)

##opening an web cam
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

#converting img into gray scale and blur image
img = cv2.imread("image/joker.jpg")

imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Blur image",imgBlur)
cv2.imshow("Gray image",imgGray)
cv2.waitKey(0)
