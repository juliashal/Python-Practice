import cv2
import numpy as np
import colorsys

src_img = cv2.imread('test.jpg')
average_color_row = np.average(src_img, axis=0)
average_color = np.average(average_color_row, axis=0)

(r, g, b) = list(average_color/255)
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)

# Adjust brightness if required
v = v*1.05
s = s*1.05

(r, g, b) = colorsys.hsv_to_rgb(h, s, v)

# New colors after adjustments
average_color_new = np.array((r*255, g*255, b*255))

d_img = np.ones((312, 312, 3), dtype=np.uint8)
d_img[:, :] = average_color_new

# Comapre soruce image to the average color
cv2.imshow('Source image', src_img)
cv2.imshow('Average Color', d_img)
cv2.waitKey(0)
