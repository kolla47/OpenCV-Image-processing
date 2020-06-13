import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    difference = cv2.absdiff(first_gray, gray_frame)
    b_frame = cv2.absdiff(first_gray, first_gray)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    _, contours, _ = cv2.findContours(difference, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        cv2.drawContours(b_frame, contour, -1, (255, 255, 255), 3)
    cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
    cv2.imshow("contour", b_frame)

    key = cv2.waitKey(30)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
