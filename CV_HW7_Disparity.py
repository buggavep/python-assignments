# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#NAME : Praneeth Buggaveeti
#STUDENT ID: 104474528

# <codecell>

%pylab inline
import cv2
import cv2.cv as cv
import os
import sys
import numpy as np

def getDisparity(imgLeft, imgRight, b_Size = 9, minDisp = -39, method = "BM"):

    gray_left = cv2.cvtColor(imgLeft, cv.CV_BGR2GRAY)
    gray_right = cv2.cvtColor(imgRight, cv.CV_BGR2GRAY)
    #print gray_left.shape
    c, r = gray_left.shape
    if method == "BM":
        sbm = cv.CreateStereoBMState()
        disparity = cv.CreateMat(c, r, cv.CV_32F)
        #sbm.SADWindowSize = 9
        sbm.SADWindowSize = b_Size
        sbm.preFilterType = 1
        sbm.preFilterSize = 5
        sbm.preFilterCap = 61
        #sbm.minDisparity = -39
        sbm.minDisparity = minDisp
        sbm.numberOfDisparities = 112
        sbm.textureThreshold = 507
        sbm.uniquenessRatio= 0
        sbm.speckleRange = 8
        sbm.speckleWindowSize = 0

        gray_left = cv.fromarray(gray_left)
        gray_right = cv.fromarray(gray_right)

        cv.FindStereoCorrespondenceBM(gray_left, gray_right, disparity, sbm)
        disparity_visual = cv.CreateMat(c, r, cv.CV_8U)
        cv.Normalize(disparity, disparity_visual, 0, 255, cv.CV_MINMAX)
        disparity_visual = np.array(disparity_visual)

    elif method == "SGBM":
        sbm = cv2.StereoSGBM()
        sbm.SADWindowSize = 9;
        sbm.numberOfDisparities = 96;
        sbm.preFilterCap = 63;
        sbm.minDisparity = -21;
        sbm.uniquenessRatio = 7;
        sbm.speckleWindowSize = 0;
        sbm.speckleRange = 8;
        sbm.disp12MaxDiff = 1;
        sbm.fullDP = False;

        disparity = sbm.compute(gray_left, gray_right)
        disparity_visual = cv2.normalize(disparity, alpha=0, beta=255, norm_type=cv2.cv.CV_MINMAX, dtype=cv2.cv.CV_8U)
    return disparity_visual

# <codecell>

b_Size = [9,13,17]
min_Disp = [-5,5,-10,10,-15,15] 
time_bSize = list()
time_minDisp = list()

BaseDir = "/home/CV/Disparity/"

subdirs = ["Art","Baby1","Baby2","Baby3","Books","Bowling1","Bowling2","Cloth1","Cloth2","Cloth3","Cloth4","Computer","Dolls","Drumsticks","Dwarves","Flowerpots","Lampshade1","Lampshade2","Laundry","Midd1","Midd2","Moebius","Monopoly","Plastic","Reindeer","Rocks1","Rocks2","Wood1","Wood2"]
dir = 0
#Enable this for loop for multiple stereo pair
#for dir in subdirs:
imgNameLeft = os.path.join(BaseDir, subdirs[dir], "view0.png")
imgNameRight = os.path.join(BaseDir, subdirs[dir], "view1.png")
 #   imgNameLeft = os.path.join(BaseDir, dir, "view0.png")
  #  imgNameRight = os.path.join(BaseDir, dir, "view1.png")
    
imgLeft = cv2.imread(imgNameLeft)
imgLeft = cv2.cvtColor(imgLeft, cv2.COLOR_BGR2RGB)
    
imgRight = cv2.imread(imgNameRight)
imgRight = cv2.cvtColor(imgRight, cv2.COLOR_BGR2RGB)
    
method = "BM"
for item in b_Size:
 t_start = cv2.getTickCount()
 disparity = getDisparity(imgLeft, imgRight, b_Size=item)
     
 t_end = cv2.getTickCount()
 time_final = (t_end - t_start) * 1000/ cv2.getTickFrequency() 
 time_bSize.append(time_final)
   
 figure(0)
 imshow(disparity)
 title("constant min disparity value to -39")

for item in minDisp:
 t_start = cv2.getTickCount()

 disparity = getDisparity(imgLeft, imgRight, minDisp=item)
     
 t_end = cv2.getTickCount()
 time_final = (t_end - t_start) * 1000/ cv2.getTickFrequency() 
 time_minDisp.append(time_final)
    
 figure(1)
 imshow(disparity)
 title("window size constant to 9")
    
print "Time values keeping min disparity constant to -39 ->", time_bSize
print "Time values keeping window size constant to 9 ->",time_minDisp

# <codecell>

#figure(0)
#imshow(disparity)
#title("disparity")

figure(1)
imshow(imgLeft)
title("left")

figure(2)
imshow(imgRight)
title("right")

# <codecell>

def plotTime(SweepTime, Sweep, name):
  N = len(SweepTime)
  ind = np.arange(N)    
  width = 0.10       # the width of the bars
  p1 = plt.bar(ind, SweepTime, width, color='r')
  plt.ylabel('Time(sec.)')
  plt.title(name)
  plt.xticks(ind+width/2., (Sweep) )
  plt.yticks(np.arange(0,2,4))
  plt.xticks(ind+width, (Sweep) )
  plt.show()

# <codecell>

# Execution Time
%pylab inline
import matplotlib.pyplot as plt
 
Time_blockSize = time_bSize[0:3]
Time_MinDisp = time_minDisp[0:7]

# plot time scale
plotTime(Time_blockSize, b_Size, "Minimum Disparity")
plotTime(Time_MinDisp, min_Disp, "Block Size")

# <codecell>


