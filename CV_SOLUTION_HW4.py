# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# # Solution to face detect

# <codecell>

%pylab inline

import os
import cv
import cv2
import numpy as np
import re
import pylab as pl
from fnmatch import fnmatch
from IPython.core.display import Image

# <codecell>

#Original: call def detectFace(path, cascade):

# new call : now passes in four new parameters : scaleFactor, minNeighbors, minSize, maxSize
def detectFace(path, cascade, scaleFactor=1.3, minNeighbors=4, minSize=(20,20), maxSize=(200,200)):   
 
    # Read image and convert to gray
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
    img = cv2.equalizeHist(img)
     
    # Base parameters 
    # Hint: re-write detectFace to pass in changes to parameters
    # Original rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20),(200,200))
    rects = cascade.detectMultiScale(img, scaleFactor, minNeighbors, cv2.cv.CV_HAAR_SCALE_IMAGE, minSize, maxSize)

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    
    #Return the location and  original image
    return rects, img

def ComputeFaceAccuracy(faceMatches, faceGroup, faceTable):
    correct = 0
    for i in range(len(faceGroup)):
        faceimagePath = faceGroup[i]
        faceimageFile = faceimagePath.split('/')[-1]
        foundFaces = faceMatches[i]
        refFaces = faceTable[faceimageFile]
        
        # Check that the faces are correct
        if (refFaces == foundFaces):
            correct = correct + 1
    return float(correct)/float(len(faceGroup))

def readTrainingFile(trainingFile):
    try:
        file_in = open(trainingFile, 'r')   #check if file exists
    except IOError:
        print 'Can\'t open file ', trainingFile, ', exiting...'
        sys.exit()
    
    imageDictionary = {}
    for line in file_in:
        columns = line.split(":")
        imageFileName = str(columns[0])
        val = int(columns[1])
        imageDictionary[imageFileName] = val
        #uncomment next line if you want to view the full training file
        #print imageFileName,val

    return imageDictionary

# <codecell>

# Sweep parameter lists
scale_factor = [1.3, 1.6, 2.0, 3.0]
min_neighbors = [4, 8, 16, 32]
min_size = [(20,20), (40,40), (80,80), (160,160)]
max_size = [(200,200), (150,150), (100,100), (50,50)]

# Location of face images : running all
faceDirList = ["/home/facedata/2003/01/13/big", "/home/facedata/2003/02/13/big",
               "/home/facedata/2003/03/13/big","/home/facedata/2003/04/13/big","/home/facedata/2003/05/13/big"]
faceGroupList = ["A","B","C","D","E"]
groupList = ["A","B","C","D","E"]

# Only do one directory at a time faces, group "A"
faceDirList = ["/home/facedata/2003/01/13/big"]
groupList = ["A"]
faceGroupList = ["A"]


# Location of AdaBoost Haar Cascade
OPENCV_PATH = "/usr/share/opencv"
HAAR_CASCADE_PATH = OPENCV_PATH + "/haarcascades"
face_cascade = HAAR_CASCADE_PATH + '/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(face_cascade)

# Define filename to match : any .jpg 
imageFilePattern = "*.jpg"
    
# Create an empty list: will hold OpenCV images
imageList = list()   

# Get the known results of number of faces
faceTable = readTrainingFile("/home/facedata/training.txt")

# <codecell>

# faceGroup
faceGroup = {}
for iface_dir in arange(len(faceDirList)):
    group = faceGroupList[iface_dir]
    faceGroup[group] = []
    
    for path, subdirs, files in os.walk(faceDirList[iface_dir]):
        for name in files:
            if fnmatch(name, imageFilePattern): # check "*.jpg"
                # Create file name
                faceFile = os.path.join(path, name)
                faceGroup[group].append(faceFile)

# <codecell>

# Use 4 lists for execution time: one for each parameter being swept
SweepTimeMinSize = []
SweepTimeMaxSize = []
SweepTimeScale = []
SweepTimeNeighbors = []

# Use 4 lists for accuracy: one for each parameter being swept
SweepAccuracyMinSize = []
SweepAccuracyMaxSize = []
SweepAccuracyScale = []
SweepAccuracyNeighbors = []

# one group, "A"
#groupList ["A","B"]
for group in groupList:
    
   print "Working on group", group   
   # Sweep one parameter at a time
    
   # Sweep the "scale factor" variable
   print "Sweep scale factor start." 
   for item in scale_factor:
      faceMatches = []
        
      # Start timer
      t_start = cv2.getTickCount()
      for index in range(len(faceGroup[group])):
          rects, img = detectFace(faceGroup[group][index], cascade, scaleFactor=item)
          faceMatches.append(len(rects))
      
      # Stop timer
      t_stop = cv2.getTickCount()
      t_total = (t_stop - t_start) / cv2.getTickFrequency()
            
      # Append time to track
      SweepTimeScale.append(t_total)
            
      # Compare accuracy
      accuracy = ComputeFaceAccuracy(faceMatches, faceGroup[group], faceTable)
      SweepAccuracyScale.append(accuracy)
   print "Sweep scale factor complete."
            
   # Sweep the "neighbor variable"
   print "Sweep min neighbor start."          
   for item in min_neighbors:
      faceMatches = []
      t_start = cv2.getTickCount()
      for index in range(len(faceGroup[group])):
          rects, img = detectFace(faceGroup[group][index], cascade, minNeighbors=item)
          faceMatches.append(len(rects))
      t_stop = cv2.getTickCount()
      t_total = (t_stop - t_start) / cv2.getTickFrequency()
      SweepTimeNeighbors.append(t_total)
                    
      # Compare accuracy
      accuracy = ComputeFaceAccuracy(faceMatches, faceGroup[group], faceTable)
      SweepAccuracyNeighbors.append(accuracy)
   print "Sweep min neighbor complete."                          
            
   # Sweep the "min size" variable
   print "Sweep min size start."               
   for item in min_size:
      faceMatches = []
      t_start = cv2.getTickCount()
      for index in range(len(faceGroup[group])):
          rects, img = detectFace(faceGroup[group][index], cascade, minSize=item)
          faceMatches.append(len(rects))
      t_stop = cv2.getTickCount()
      t_total = (t_stop - t_start) / cv2.getTickFrequency()
      SweepTimeMinSize.append(t_total)
                    
      # Compare accuracy
      accuracy = ComputeFaceAccuracy(faceMatches, faceGroup[group], faceTable)
      SweepAccuracyMinSize.append(accuracy)
   print "Sweep min size complete."   
            
    
   # Sweep the "max size" variable
   print "Sweep max size start."       
   for item in max_size:
      faceMatches = []
      t_start = cv2.getTickCount()
      for index in range(len(faceGroup[group])):
          rects, img = detectFace(faceGroup[group][index], cascade, maxSize=item)
          faceMatches.append(len(rects))
      t_stop = cv2.getTickCount()
      t_total = (t_stop - t_start) / cv2.getTickFrequency()
      SweepTimeMaxSize.append(t_total)
      accuracy = ComputeFaceAccuracy(faceMatches, faceGroup[group], faceTable)
      SweepAccuracyMaxSize.append(accuracy)
   print "Sweep max size complete."   
            
# Print the accuracy
print "Accuracy [Scale, minNeighbors, minSize, maxSize]"
print SweepAccuracyScale
print SweepAccuracyNeighbors
print SweepAccuracyMinSize
print SweepAccuracyMaxSize

# Print the execution time
print "Execution time [Scale, minNeighbors, minSize, maxSize]"
print SweepTimeScale
print SweepTimeNeighbors
print SweepTimeMinSize
print SweepTimeMaxSize

# <codecell>

def plotTime(SweepTime, Sweep, name):
  N = len(SweepTime)
  ind = np.arange(N)    
  width = 0.35       # the width of the bars
  p1 = plt.bar(ind, SweepTime, width, color='b')
  plt.ylabel('Time(sec.)')
  plt.title(name)
  plt.xticks(ind+width/2., (Sweep) )
  plt.yticks(np.arange(0,8,2))
  plt.xticks(ind+width, (Sweep) )
  plt.show()

# <codecell>

# [Task] Plot Execution Time
%pylab inline
import matplotlib.pyplot as plt
 
# slice the SweepTime list: A - [0:4], B - [4:8], C - [8:12], D - [12:16], E - [16:20]
SweepTimeScale_A = SweepTimeScale[0:4]
SweepTimeNeighbors_A = SweepTimeNeighbors[0:4]
SweepTimeMinSize_A = SweepTimeMinSize[0:4]
SweepTimeMaxSize_A = SweepTimeMaxSize[0:4]
    
# group A - Execution time
# plot time scale
plotTime(SweepTimeScale_A, scale_factor, "Scale")
plotTime(SweepTimeNeighbors_A, min_neighbors, "Min Neighbors")
plotTime(SweepTimeMinSize_A, min_size, "Min Size")
plotTime(SweepTimeMaxSize_A, max_size, "Max Size")


    

# <codecell>

def plotAccuracy(SweepAccuracy, Sweep, name):
  N = len(SweepAccuracy)
  ind = np.arange(N)    
  width = 0.35       # the width of the bars
  p1 = plt.bar(ind, SweepAccuracy, width, color='r')
  plt.ylabel('Accuracy(%)')
  plt.title(name)
  plt.xticks(ind+width/2., (Sweep) ) 
  plt.yticks(np.arange(0,1.2,0.2))
  plt.xticks(ind+width, (Sweep) )
  plt.show()

# <codecell>

# [Task] plot accuracy
%pylab inline
import matplotlib.pyplot as plt

# slice the SweepAccuracy list: A - [0:4], B - [4:8], C - [8:12], D - [12:16], E - [16:20]
SweepAccuracyScale_A = SweepAccuracyScale[0:4]
SweepAccuracyNeighbors_A = SweepAccuracyNeighbors[0:4]
SweepAccuracyMinSize_A = SweepAccuracyMinSize[0:4]
SweepAccuracyMaxSize_A = SweepAccuracyMaxSize[0:4]

plotAccuracy(SweepAccuracyScale_A, scale_factor, "Scale")
plotAccuracy(SweepAccuracyNeighbors_A, min_neighbors, "Min Neighbors")
plotAccuracy(SweepAccuracyMinSize_A, min_size, "Min Size")
plotAccuracy(SweepAccuracyMaxSize_A, max_size, "Max Size")

# <codecell>

def plotTimeAccuracy(SweepTime, SweepAccuracy, Sweep, name):
  N = len(SweepTime)
  ind = np.arange(N)    
  width = 0.35       # the width of the bars
  p1 = plt.bar(ind, SweepTime, width, color='b')
  p2 = plt.bar(ind+width, SweepAccuracy, width, color='r')
  plt.ylabel('Time(sec.)/Accuracy')
  plt.title(name + ' - Execution time vs Accuracy')
  plt.xticks(ind+width, (Sweep) )
  plt.yticks(np.arange(0,8,2))
  plt.legend( (p1[0], p2[0]), ('Exec. time', 'Accuracy') )
  plt.show()
    

# <codecell>

%pylab inline
import matplotlib.pyplot as plt

scale_factor = [1.3, 1.6, 2.0, 3.0]
min_neighbors = [4, 8, 16, 32]
min_size = [(20,20), (40,40), (80,80), (160,160)]
max_size = [(200,200), (150,150), (100,100), (50,50)]

plotTimeAccuracy(SweepTimeScale_A, SweepAccuracyScale_A, scale_factor, "Scale")
plotTimeAccuracy(SweepTimeNeighbors_A, SweepAccuracyNeighbors_A, min_neighbors, "Min Neighbors")
plotTimeAccuracy(SweepTimeMinSize_A, SweepAccuracyMinSize_A, min_size, "Min Size")
plotTimeAccuracy(SweepTimeMaxSize_A, SweepAccuracyMaxSize_A, max_size, "Max Size")

# <codecell>

# Get the different groups
SweepAccuracyScale_A = SweepAccuracyScale[0:4]
SweepAccuracyNeighbors_A = SweepAccuracyNeighbors[0:4]
SweepAccuracyMinSize_A = SweepAccuracyMinSize[0:4]
SweepAccuracyMaxSize_A = SweepAccuracyMaxSize[0:4]

SweepAccuracyScale_B = SweepAccuracyScale[4:8]
SweepAccuracyNeighbors_B = SweepAccuracyNeighbors[4:8]
SweepAccuracyMinSize_B = SweepAccuracyMinSize[4:8]
SweepAccuracyMaxSize_B = SweepAccuracyMaxSize[4:8]

SweepAccuracyScale_C = SweepAccuracyScale[8:12]
SweepAccuracyNeighbors_C = SweepAccuracyNeighbors[8:12]
SweepAccuracyMinSize_C = SweepAccuracyMinSize[8:12]
SweepAccuracyMaxSize_C = SweepAccuracyMaxSize[8:12]

SweepAccuracyScale_D = SweepAccuracyScale[12:16]
SweepAccuracyNeighbors_D = SweepAccuracyNeighbors[12:16]
SweepAccuracyMinSize_D = SweepAccuracyMinSize[12:16]
SweepAccuracyMaxSize_D = SweepAccuracyMaxSize[12:16]

SweepAccuracyScale_E = SweepAccuracyScale[16:20]
SweepAccuracyNeighbors_E = SweepAccuracyNeighbors[16:20]
SweepAccuracyMinSize_E = SweepAccuracyMinSize[16:20]
SweepAccuracyMaxSize_E = SweepAccuracyMaxSize[16:20]

# <codecell>

def plotAccuracyAcrossSet(Sweep, xlabel, ylabel, labels, SweepAccuracyA, SweepAccuracyB, SweepAccuracyC, SweepAccuracyD, SweepAccuracyE):
   plt.plot(Sweep, SweepAccuracyA)
   plt.plot(Sweep, SweepAccuracyB)
   plt.plot(Sweep, SweepAccuracyC)
   plt.plot(Sweep, SweepAccuracyD)
   plt.plot(Sweep, SweepAccuracyE)
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.legend((labels[0],labels[1],labels[2],labels[3],labels[4]))
   plt.title(xlabel)
   plt.show()
    

# <codecell>

scale_factor = [1.3, 1.6, 2.0, 3.0]
min_neighbors = [4, 8, 16, 32]
min_size = [(20,20), (40,40), (80,80), (160,160)]
max_size = [(200,200), (150,150), (100,100), (50,50)]

plotAccuracyAcrossSet(scale_factor, "Scale", "Accuracy", ["A","B","C","D","E"], SweepAccuracyScale_A,SweepAccuracyScale_B, SweepAccuracyScale_C, SweepAccuracyScale_D,SweepAccuracyScale_E)


# <codecell>

plotAccuracyAcrossSet(min_neighbors, "Min Neighbors", "Accuracy", ["A","B","C","D","E"], SweepAccuracyNeighbors_A,SweepAccuracyNeighbors_B, SweepAccuracyNeighbors_C, SweepAccuracyNeighbors_D,SweepAccuracyNeighbors_E)

# <codecell>

plotAccuracyAcrossSet(min_size, "Min Size", "Accuracy", ["A","B","C","D","E"], SweepAccuracyMinSize_A,SweepAccuracyMinSize_B, SweepAccuracyMinSize_C, SweepAccuracyMinSize_D,SweepAccuracyMinSize_E)

# <codecell>

plotAccuracyAcrossSet(max_size, "Max Size", "Accuracy", ["A","B","C","D","E"], SweepAccuracyMaxSize_A,SweepAccuracyMaxSize_B, SweepAccuracyMaxSize_C, SweepAccuracyMaxSize_D,SweepAccuracyMaxSize_E)

# <codecell>

# calculate change reate for each group
def cal_change(a):
    ind = 0
    change_list = list()
    groupList = ["A","B","C","D","E"]
    for i in range(len(groupList)):
        change_rate = (a[ind] - a[ind + 3])/a[ind]
        change_list.append(change_rate)
        print "%s: %f" %(groupList[i], change_list[i])
        ind = ind + 4
        
    return max(change_list)

print 'scale_factor'
scale_max = cal_change(SweepAccuracyScale)
print scale_max

print 'min_neighbor'
neighbor_max = cal_change(SweepAccuracyNeighbors)
print neighbor_max

print 'min_size'
min_max = cal_change(SweepAccuracyMinSize)
print min_max

print 'max_size'
max_max = cal_change(SweepAccuracyMaxSize)
print max_max

# <rawcell>

# [Question]
# Which database is impacted the most (as the highest percentage change from the base run) based on the parameter changes: (ScaleFactor, MinNeighbors, minSize, maxSize).
# 
# [Answer]
# scale_factor
# B: %67.2727
# 
# min_neighbors
# E: %89.7727
# 
# min_size
# A: %71.0526315789
# max_size
# 
# E: %93.1818
# 
# [Question]
# What range of setting of the (ScaleFactor, MinNeighbors, minSize, maxSize) parameters can be set without losing ANY accuracy from the base run.
# 
# [Answer]
# scale_factor: 1.3
# min_neighbors: 4
# min_size:(20,20), (40,40), (80,80)
# max_size: (200,200)

