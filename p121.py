import cv2
import numpy as np
import time
import keyboard

capture = cv2.VideoCapture(0)
image = cv2.imread("Background.jpg")
time.sleep(2)

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == False:
        break
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
  
    upper_black = np.array([104, 153, 70])
    lower_black = np.array([30, 30, 0])
  
    mask = cv2.inRange(frame, lower_black, upper_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)
  
    f = frame - res
    f = np.where(f == 0, image, f)
  
    cv2.imshow("Video", frame)
    cv2.imshow("Masked", f)
    if cv2.waitKey(1) and keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
        break

capture.release() 
cv2.destroyAllWindows()