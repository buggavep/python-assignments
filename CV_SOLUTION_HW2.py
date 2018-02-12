# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# Homework 2 - ELEC 4727/5727 Computer Vision

# <codecell>

# Standard imports for python
%pylab inline
import numpy as np
import cv2
import cv

# <codecell>

# Define filter structure
filter = array([[0, 0, 1, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 0, 1, 1, 1],
              [0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0]], dtype = uint8)

# Define iterations
num_iterations = array([1, 2, 4, 8, 16, 32])

# Define images
image1 = cv2.imread('/home/CV/CVHW2/Picture1.jpg')
image2 = cv2.imread('/home/CV/CVHW2/Picture2.jpg')
image3 = cv2.imread('/home/CV/CVHW2/Picture3.jpg')
img_list = array([image1, image2, image3])

# Define time variables to hold each iteration of each image
time_erode = np.zeros((size(img_list), size(num_iterations)))
time_dilate = time_erode

# Calculate the time for each iteration of each i
for i in range(size(img_list)):
    for j in range (size(num_iterations)):
        # Time to perform j iteration erosion on image i
        t_start = cv2.getTickCount()
        erosion = cv2.erode(img_list[i], filter, iterations = num_iterations[j])
        t_end = cv2.getTickCount()
        time_erode[i][j] = (t_end - t_start) * 1000 / cv2.getTickFrequency()

        # Time to perform j iteration dilation on image i
        t_start = cv2.getTickCount()
        dilation = cv2.dilate(img_list[i], filter, iterations = num_iterations[j])
        t_end = cv2.getTickCount()
        time_dilate[i][j] = (t_end - t_start) * 1000 / cv2.getTickFrequency() 

# <codecell>

# Plot erosion iterations vs time graph
figure()
plot(num_iterations, time_erode[0], 'r')
plot(num_iterations, time_erode[1], 'b')
plot(num_iterations, time_erode[2], 'g')
xlabel('Iterations')
ylabel('Time')
title('Execution Time')
show()

# Plot dilation iterations vs time graph
figure()
plot(num_iterations, time_dilate[0], 'r')
plot(num_iterations, time_dilate[1], 'b')
plot(num_iterations, time_dilate[2], 'g')
xlabel('Iterations')
ylabel('Time')
title('Execution Time')
show()

# <codecell>


