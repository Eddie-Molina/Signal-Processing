"""
    Eddie Molina
    CSE 3313-001
    HW-08
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.feature import match_template 
ERBcolor = plt.imread("ERBwideColorSmall.jpg")
ERBtemplate = plt.imread("ERBwideTemplate.jpg")
gray1 = color.rgb2gray(ERBcolor)
gray2 = color.rgb2gray(ERBtemplate)
plt.figure(1)
plt.imshow(gray1, cmap = plt.get_cmap("gray"))
plt.show()
plt.figure(2)
plt.imshow(gray2, cmap = plt.get_cmap("gray"))
plt.show()
match = match_template(gray1, gray2)
location = np.unravel_index(np.argmax(match), match.shape)
x, y = location[::-1]
x2, y2 = gray2.shape # size of wide image
for row in range(x2):
    for col in range(y2):
        gray1[row+y][col+x] = 0
print(x, y)
plt.figure(3)
plt.imshow(gray1, plt.get_cmap("gray"))
plt.show()