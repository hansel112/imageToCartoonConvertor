#!/usr/bin/env python3

"""python script for converting image to a cartoon.

"""

import cv2
import numpy as np


image = cv2.imread("MyImage.jpg")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)


cv2.imshow("Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)


cv2.waitKey(0)
cv2.destroyAllWindows()

