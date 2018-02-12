# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Homework 2 Template - ELEC 4727/5727 Computer Vision 
# Name:praneeth Buggaveeti
#student Id:104474528

# <codecell>

# Standard imports for python
%pylab inline
import numpy as np
import cv2
import cv
#import glob
import matplotlib.pyplot as plt

# <codecell>

#Starting template code
te = []
td = []
filter = array([[0, 0, 1, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 0, 1, 1, 1],
              [0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0]], dtype = uint8)

arr = [[]]


num_iterations = array([1, 2, 4, 8, 16, 32])
image1 = cv2.imread('/home/CV/CVHW2/Picture1.jpg')
image2 = cv2.imread('/home/CV/CVHW2/Picture2.jpg')
image3 = cv2.imread('/home/CV/CVHW2/Picture3.jpg')

image_list = [image1,image2,image3] 

#path = '/home/CV/CVHW2/*.jpg'
#dir = glob.glob(path) 

for i in xrange(3):
 image = image_list[i]
 for j in num_iterations:  
  # Time to perform multiple iterations erosion on three images 
  t_start = cv2.getTickCount()
  erosion = cv2.erode(image, filter, iterations = j)
  t_end = cv2.getTickCount()
  time_erode = (t_end - t_start) * 1000 / cv2.getTickFrequency()
  #te.append(time_erode)
  
  # Time to perform multiple iterations dilation on three images 
  t_start = cv2.getTickCount()
  dilation = cv2.dilate(image, filter, iterations = j)
  t_end = cv2.getTickCount()
  time_dilate = (t_end - t_start) * 1000 / cv2.getTickFrequency() 
  
  #creating list of execution times for for both erosion and dilation
  te.append(time_erode)
  td.append(time_dilate)
  #print te
  #print td

# <codecell>

#ploting graph for erode
x_series = num_iterations
y_series_1 = te[0:6]
y_series_2 = te[6:12]
y_series_3 = te[12:18]
plt.title("EROSION")
plt.xlabel("Iterations----->")
plt.ylabel("Time---->")
plt.plot(x_series, y_series_1,label = "Image 1")
plt.plot(x_series, y_series_2,label = "Image 2")
plt.plot(x_series, y_series_3,label = "Image 3")
plt.xlim(0,30)
plt.ylim(0,15)
plt.legend(loc="upper center")
plt.show()

# <codecell>

#ploting graph for erode
x_series = num_iterations
y_series_1 = td[0:6]
y_series_2 = td[6:12]
y_series_3 = td[12:18]
plt.title("Dilation")
plt.xlabel("Iterations----->")
plt.ylabel("Time---->")
plt.plot(x_series, y_series_1,label = "Image 1")
plt.plot(x_series, y_series_2,label = "Image 2")
plt.plot(x_series, y_series_3,label = "Image 3")
plt.xlim(0,30)
plt.ylim(0,15)
plt.legend(loc="upper center")
plt.show()

# <codecell>

imshow(erosion)

# <codecell>

imshow(dilation)

