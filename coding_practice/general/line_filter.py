import cv2
import numpy as np


if __name__ == '__main__':
    img = np.zeros((100, 100))

    cv2.line(img, (40, 5), (40, 60), 1, 3)
    cv2.line(img, (65, 20), (65, 75), 1, 3)
    cv2.line(img, (88, 50), (88, 99), 1, 3)
    cv2.line(img, (19, 35), (19, 95), 1, 3)

    cv2.line(img, (20, 20), (80, 20), 1, 3)
    cv2.line(img, (5, 40), (45, 40), 1, 3)
    cv2.line(img, (41, 55), (95, 55), 1, 3)
    cv2.line(img, (45, 75), (78, 75), 1, 3)

    cv2.imshow('foo', img)

    cv2.waitKey()

    kernel = np.ones((15, 3))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow('foo', img)

    cv2.waitKey()