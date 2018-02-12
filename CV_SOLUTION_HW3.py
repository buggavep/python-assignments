# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>


# <codecell>

%pylab inline

import cv
import cv2
import os
import pylab as plt
from fnmatch import fnmatch

# <codecell>

# Initialize OpenCV methods for histogram comparison
# * To add more methods, just add (name, method) here. The plot views may be affected.
OPENCV_METHODS = (("Correlation", cv2.cv.CV_COMP_CORREL),
                  ("Chi-Squared", cv2.cv.CV_COMP_CHISQR),
                  ("Intersection", cv2.cv.CV_COMP_INTERSECT), 
                  ("Bhattacharyya", cv2.cv.CV_COMP_BHATTACHARYYA))

# <codecell>

# Create a histogram for images (grayscale)
def createHist(image):
    histogram = cv2.calcHist([image],[0],None,[256],[0,256])
    return histogram

# <codecell>

# Histogram comparison using OpenCV methods
def compareHist(h1, h2):
    # Initialize number of methods
    numMethods = len(OPENCV_METHODS)
    # Initialize the results (comparisons/time)
    results = [0] * 2 * numMethods
    # Loop over the comparison methods
    for (i, (name, method)) in enumerate(OPENCV_METHODS):
        # Time to perform method i
        t_start = cv2.getTickCount()
        # Compute the distance between the two histograms
        # using the method and update the results dictionary
        results[2*i] = cv2.compareHist(h1, h2, method)
        t_end = cv2.getTickCount()
        results[2*i+1] = (t_end - t_start) * 1000 / cv2.getTickFrequency()
    # Return a list with [comparion, time, comparison, time, ...]
    return results

# <codecell>

# Look into homework directory
imageDir = "/home/CV/CVHW3"

# Define filename to match : any .jpg 
imageFilePattern = "*.jpg"
    
# Create an empty list: will hold OpenCV images
imageList = list()   
imageHistogramList = list()

# Automatically descend all directories of imageDir
for path, subdirs, files in os.walk(imageDir):
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
            histogram = createHist(imgray)
            imageHistogramList.append(histogram)

# Number of images and methods
numImages = len(imageList)
numMethods = len(OPENCV_METHODS)

histogramResults = numpy.zeros([numMethods, numImages, numImages])
timeResults = numpy.zeros([numMethods])

for i in range(0, numImages):
    for j in range(0, numImages):
        results = compareHist(imageHistogramList[i], imageHistogramList[j])
        for k in range(0, numMethods):
            histogramResults[k, i, j] = results[2*k]
            timeResults[k] += results[2*k+1]

# <codecell>

# Plot histogram heatmaps comparison for each 10 image comparisons.
fig, ax = plt.subplots(1, numMethods, figsize=(25, 4))
for (i, (name, method)) in enumerate(OPENCV_METHODS):
    # Plot image
    im = ax[i].pcolor(histogramResults[i])
    # Add title and font size
    ax[i].set_title(name).set_fontsize(15)
    # Add a colorbar
    fig.colorbar(im, ax=ax[i])

# <codecell>

# Plot the performance of histogram comparions (sum of time for each method)
y_pos = np.arange(numMethods)
plt.barh(y_pos, timeResults, align='center')
plt.yticks(y_pos, [y[0] for y in OPENCV_METHODS])
plt.xlabel('Time (milliseconds)')
plt.title('Execution Time Compare')
plt.show()

# <codecell>

# Evaluate time for different database sizes
db_size = [100, 1000, 10000, 100000, 1000000]
db_times = numpy.zeros([numMethods, len(db_size)])

for i in range(0, numMethods):
    for j in range(0, len(db_size)):
        # timeResults were compute for 10 images, so divide by 10
        # Change from milliseconds to seconds, so divide by 1000
        db_times[i][j] = db_size[j] * timeResults[i] / 10 / 1000

# <codecell>

# Plot time analysis for different database sizes
fig = plt.figure(1, figsize=(20,5)) 
line_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

for (i, (name, method)) in enumerate(OPENCV_METHODS):
    plt.plot(db_size, db_times[i], line_color[i % 8], label = name)

plt.xlabel('Number of Images')
plt.ylabel('Time (seconds)')
plt.title('Extrapolation of Time ')
plt.legend(loc="upper left")
plt.show()

# <codecell>


