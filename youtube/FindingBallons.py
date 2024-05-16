import cv2
import numpy as np

def findBalloons(img):
    bboxs = []
    img = cropImage(img, 0.3)
    img = preprocess(img)
    imgContours, contours = findContours(img)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:  # Adjust this threshold as needed
            x, y, w, h = cv2.boundingRect(cnt)
            cx = x + w // 12
            cy = y + h // 3
            bboxs.append((cx, cy, w, h))
            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (255, 255, 255), 2)
    return imgContours, bboxs

def cropImage(img, cropVal):
    h, w, c = img.shape
    img = img[int(h * cropVal):h, 0:w]
    return img

def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 5, 0)
    img = cv2.Canny(img, 50, 100)
    kernel = np.ones((5, 5), np.uint8)
    img = cv2.dilate(img, kernel)
    return img

def findContours(img):
    imgContours = np.zeros_like(img)
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours, contours, -1, (255, 255, 255), 2)
    return imgContours, contours

