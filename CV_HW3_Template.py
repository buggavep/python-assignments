# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# #ELEC 4727/5727 - Computer Vision
# 
# #Name: praneeth Buggaveeti

# <codecell>

%pylab inline

import cv
import cv2
import os
import pylab as pl
from fnmatch import fnmatch

# Look into homework directory
imageDir = "/home/CV/CVHW3"

# Define filename to match : any .jpg 
imageFilePattern = "*.jpg"
    
# Create an empty list: will hold OpenCV images
imageList = list()   
imageHistogramList = list()

# Automatically descend all directories of imageDir
for path, subwdirs, files in os.walk(imageDir):
    for name in files:
        if fnmatch(name, imageFilePattern):
            # Create file name
            imageFile = os.path.join(path, name)
            
            # Read OpenCV image
            img = cv2.imread(imageFile)
            
            # Convert images to gray scale
            imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Add image to list of OpenCV images
            imageList.append(imgray)
            
            # Create a histogram
            histogram = cv2.calcHist([imgray],[0],None,[256],[0,256])
            
            imageHistogramList.append(histogram)
            pl.plot(histogram) 
            pl.show()
            
numImages = len(imageList)

# <codecell>

%correlation process

histogramResults_correl = numpy.zeros([numImages, numImages])
start_CORREL = cv2.getTickCount()
for i in range(0,numImages):
    for j in range(0,numImages):
        result=cv2.compareHist(imageHistogramList[i], imageHistogramList[j], cv.CV_COMP_CORREL)
        histogramResults_correl[i,j] = result
CORREL_time = cv2.getTickCount() - start_CORREL
print "Correl Time Taken",CORREL_time
pl.pcolor(histogramResults_correl) 
pl.colorbar()   
pl.show()

# <codecell>

%Chi-Square process

histogramResults_CHISQR = numpy.zeros([numImages, numImages])
start_CHISQR = cv2.getTickCount()
for i in range(0,numImages):
    for j in range(0,numImages):
        result=cv2.compareHist(imageHistogramList[i], imageHistogramList[j], cv.CV_COMP_CHISQR)
        histogramResults_CHISQR[i,j] = result
CHISQR_time = cv2.getTickCount() - start_CHISQR
print "Chisqr Time Taken",CHISQR_time
pl.pcolor(histogramResults_CHISQR) 
pl.colorbar()   
pl.show()

# <codecell>

%Intersection Process
histogramResults_INTERSECT = numpy.zeros([numImages, numImages])
start_INTERSECT = cv2.getTickCount()
for i in range(0,numImages):
    for j in range(0,numImages):
        result=cv2.compareHist(imageHistogramList[i], imageHistogramList[j], cv.CV_COMP_INTERSECT)
        histogramResults_INTERSECT[i,j] = result
INTERSECT_time = cv2.getTickCount() - start_INTERSECT
print "INTERSECT Time Taken",INTERSECT_time
pl.pcolor(histogramResults_INTERSECT) 
pl.colorbar()   
pl.show()

# <codecell>

%Bhattacharyya Process

histogramResults_BHATTACHARYYA = numpy.zeros([numImages, numImages])
start_BHATTACHARYYA = cv2.getTickCount()
for i in range(0,numImages):
    for j in range(0,numImages):
        result=cv2.compareHist(imageHistogramList[i], imageHistogramList[j], cv.CV_COMP_BHATTACHARYYA)
        histogramResults_BHATTACHARYYA[i,j] = result
BHATTACHARYYA_time = cv2.getTickCount() - start_BHATTACHARYYA
print "BHATTACHARYYA Time Taken",BHATTACHARYYA_time
pl.pcolor(histogramResults_BHATTACHARYYA) 
pl.colorbar()   
pl.show()

# <codecell>

ET = (CORREL_time, CHISQR_time, INTERSECT_time, BHATTACHARYYA_time)
fig = pl.figure()
ax = pl.subplot(111)
ax.bar(range (0,4), ET, width=0.5)

# <codecell>

%Extrapolation process
e_t = []
t_t = [CORREL_time,CHISQR_time,INTERSECT_time,BHATTACHARYYA_time]
for i in t_t:
 time = i / 10
 exec_time = (time,i,time*100,time*1000,time*10000,time*100000,time*1000000)
 e_t.append(exec_time)

y_series_1 = e_t[0]
y_series_2 = e_t[1]
y_series_3 = e_t[2]
y_series_4 = e_t[3]

plt.title("Extrapolation")
plt.plot(range(0,7), y_series_1,label = "CORREL_time")
plt.plot(range(0,7), y_series_2,label = "CHISQR_time")
plt.plot(range(0,7), y_series_3,label = "INTERSECT_time")
plt.plot(range(0,7), y_series_4,label = "BHATTACHARYYA_time")

plt.legend(loc="upper left")
plt.show()

# <codecell>


