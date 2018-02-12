# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <rawcell>

# ELEC4727/5727 : HW 4 (Face Detection)
# Name:Praneeth Buggaveeti

# <codecell>

%pylab inline

import cv
import cv2
import os
import pylab as pl
from fnmatch import fnmatch

# <codecell>

#def detectFace(path, cascade):
def detectFace(path, cascade, scale_factor, min_neighbours, min_size, max_size):
    # Read image and convert to gray
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)
     
    # Base parameters 
    # Hint: re-write detectFace to pass in changes to parameters
    #rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20),(200,200))
    rects = cascade.detectMultiScale(img, scale_factor,min_neighbours, cv2.cv.CV_HAAR_SCALE_IMAGE,min_size,max_size)

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    
    #Return the location and  original image
    return rects, img

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
        # uncomment next line if you want to view the full training file
        #print imageFileName,val

    return imageDictionary

# <codecell>


# Location of face images 
faceDir = "/home/facedata/2003/01/13/big"
faceDirList = ["/home/facedata/2003/01/13/big", "/home/facedata/2003/02/13/big","/home/facedata/2003/03/13/big","/home/facedata/2003/04/13/big","/home/facedata/2003/05/13/big"]

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
scale = [1.3,1.6,2.0,3.0,4.0]
min_ng = [4,8,16,32]
min_size = [(20,20),(40,40),(80,80),(160,160)]
max_size = [(200,200),(150,150),(100,100),(50,50)]
time_list = []
accuracy = []
# Automatically descend all directories 
# Hint: If you put a new for-loop over the faceDirList, the
# system will visit all 5 of the face database directories
for path, subdirs, files in os.walk(faceDir):
       #for path, subdirs, files in os.walk(faceDirList[iface_dir]):
        for name in files:
            if fnmatch(name, imageFilePattern):
            
            # Create file name
               faceFile = os.path.join(path, name)
            
            # Perform face detection
            # Hint: If you design your experiments properly, you can re-write 
            #  the function detectFace to pass in all parameters and do a loop 
            #  of the function detectFace for all parameter changes
            #rects, img = detectFace(faceFile,cascade)
            for j in range(0,4):
             for i in range(0,4):
               
               t_start = cv2.getTickCount()

               if(j==0):
                rects, img = detectFace(faceFile, cascade, scale[i],min_ng[0],min_size[0], max_size[0])
                b = faceTable[name]
                a = len(rects)
                if(a==0 and b==0):
                    accuracy.append(100)
                elif(a!=0 and b ==0):
                    accuracy.append(25)
                elif(a==0 and b!=0):
                    accuracy.append(0)
                else:
                    accuracy.append(100-((abs(a-b))/b)*100)
               if(j==1):
                rects, img = detectFace(faceFile, cascade, scale[0],min_ng[i],min_size[0], max_size[0])
                b = faceTable[name]
                a = len(rects)
                if(a==0 and b==0):
                    accuracy.append(100)
                elif(a!=0 and b ==0):
                    accuracy.append(25)
                elif(a==0 and b!=0):
                    accuracy.append(0)
                else:
                    accuracy.append(100-((abs(a-b))/b)*100)
               if(j==2):
                rects, img = detectFace(faceFile, cascade, scale[0],min_ng[0],min_size[i], max_size[0])
                b = faceTable[name]
                a = len(rects)
                if(a==0 and b==0):
                    accuracy.append(100)
                elif(a!=0 and b ==0):
                    accuracy.append(25)
                elif(a==0 and b!=0):
                    accuracy.append(0)
                else:
                    accuracy.append(100-((abs(a-b))/b)*100)
               if(j==3):
                rects, img = detectFace(faceFile, cascade, scale[0],min_ng[0],min_size[0], max_size[i])
                b = faceTable[name]
                a = len(rects)
                if(a==0 and b==0):
                    accuracy.append(100)
                elif(a!=0 and b ==0):
                    accuracy.append(25)
                elif(a==0 and b!=0):
                    accuracy.append(0)
                else:
                    accuracy.append(100-((abs(a-b))/b)*100)
                    
            t_end = cv2.getTickCount()
            time_final = t_end - t_start
                          # time_res.append(t_end-t_start)
                          # rects_res.append(len(rects))   
            time_list.append(time_final)             
            
            # Add image to list of OpenCV images
            #imageList.append(img)
            #print name, ":", len(rects)
            
print "time values =",time_list
#print "accuracy values =",accuracy


# <codecell>

#for 1
fig = pl.figure(figsize=(10,4),dpi=300)
pl.subplot(1,1,1)
title('scale_factor')
plot(range(0,4),time_list[0:4],'g*-')

fig = pl.figure(figsize=(10,4),dpi=300)
pl.subplot(1,1,1)
title('min_ng')
plot(range(0,4),time_list[0:4],'r*-')

fig = pl.figure(figsize=(10,4),dpi=300)
pl.subplot(1,1,1)
title('min_size')
plot(range(0,4),time_list[0:4],'b*-')

fig = pl.figure(figsize=(10,4),dpi=300)
pl.subplot(1,1,1)
title('max_size')
plot(range(0,4),time_list[0:4],'y*-')


# <codecell>

n_groups = 90
scale1=accuracy[0:90]
scale2=accuracy[90:180]
scale3=accuracy[180:270]
scale4=accuracy[270:360]
fig, ax=plt.subplots()

index = np.arange(n_groups)
bar_width = 1.5
opacity = 0.4
error_config = {'ecolor':'0.3'}

rects1 = plt.bar(index, scale1,bar_width,alpha = opacity,color='b',
                 error_kw = error_config, label = '1.3')
rects2 = plt.bar(index, scale2,bar_width,alpha = opacity,color='r',
                 error_kw = error_config, label = '1.6')
rects3 = plt.bar(index, scale3,bar_width,alpha = opacity,color='g',
                 error_kw = error_config, label = '2.0')
rects4 = plt.bar(index, scale4,bar_width,alpha = opacity,color='c',
                 error_kw = error_config, label = '3.0')
plt.xlabel('Images')
plt.ylabel('Accuracy')
plt.title('scale')
plt.xticks(index+bar_width,(range(1,91)))
plt.legend()
plt.tight_layout()
plt.show()

# <codecell>

min_ng1=accuracy[0:90]
min_ng2=accuracy[90:180]
min_ng3=accuracy[180:270]
min_ng4=accuracy[270:360]
fig, ax=plt.subplots()

index = np.arange(n_groups)
bar_width = 1.5
opacity = 0.4
error_config = {'ecolor':'0.3'}

rects1 = plt.bar(index, min_ng1,bar_width,alpha = opacity,color='b',
                 error_kw = error_config, label = '4')
rects2 = plt.bar(index, min_ng2,bar_width,alpha = opacity,color='r',
                 error_kw = error_config, label = '8')
rects3 = plt.bar(index, min_ng3,bar_width,alpha = opacity,color='g',
                 error_kw = error_config, label = '16')
rects4 = plt.bar(index, min_ng4,bar_width,alpha = opacity,color='c',
                 error_kw = error_config, label = '32')
plt.xlabel('Images')
plt.ylabel('Accuracy')
plt.title('min_neighbours')
plt.xticks(index+bar_width,(range(1,91)))
plt.legend()
plt.tight_layout()
plt.show()

# <codecell>

min_size1=accuracy[0:90]
min_size2=accuracy[90:180]
min_size3=accuracy[180:270]
min_size4=accuracy[270:360]
fig, ax=plt.subplots()

index = np.arange(n_groups)
bar_width = 1.5
opacity = 0.4
error_config = {'ecolor':'0.3'}

rects1 = plt.bar(index, min_size1,bar_width,alpha = opacity,color='b',
                 error_kw = error_config, label = '20,20')
rects2 = plt.bar(index, min_size2,bar_width,alpha = opacity,color='r',
                 error_kw = error_config, label = '40,40')
rects3 = plt.bar(index, min_size3,bar_width,alpha = opacity,color='g',
                 error_kw = error_config, label = '80,80')
rects4 = plt.bar(index, min_size4,bar_width,alpha = opacity,color='c',
                 error_kw = error_config, label = '160,160')
plt.xlabel('Images')
plt.ylabel('Accuracy')
plt.title('min_size')
plt.xticks(index+bar_width,(range(1,91)))
plt.legend()
plt.tight_layout()
plt.show()

# <codecell>

max_sz1=accuracy[0:90]
max_sz2=accuracy[90:180]
max_sz3=accuracy[180:270]
max_sz4=accuracy[270:360]
fig, ax=plt.subplots()

index = np.arange(n_groups)
bar_width = 1.5
opacity = 0.4
error_config = {'ecolor':'0.3'}

rects1 = plt.bar(index, max_sz1,bar_width,alpha = opacity,color='b',
                 error_kw = error_config, label = '200,200')
rects2 = plt.bar(index, max_sz2,bar_width,alpha = opacity,color='r',
                 error_kw = error_config, label = '150,150')
rects3 = plt.bar(index, max_sz3,bar_width,alpha = opacity,color='g',
                 error_kw = error_config, label = '100,100')
rects4 = plt.bar(index, max_sz4,bar_width,alpha = opacity,color='c',
                 error_kw = error_config, label = '50,50')
plt.xlabel('Images')
plt.ylabel('Accuracy')
plt.title('Max_size')
plt.xticks(index+bar_width,(range(1,91)))
plt.legend()
plt.tight_layout()
plt.show()

# <codecell>

#Time Vs Accuracy
scalex = time_final[0:5]
scaley = accuracy[0:5]
title('time vs accuracy:scale')
xlabel('Execution time')
ylabel('Accuracy')

pl.plot(scalex,scaley)
pl.show()

# <codecell>

scalex = time_final[5:11]
scaley = accuracy[5:11]
title('time vs accuracy:min_neighbours')
xlabel('Execution time')
ylabel('Accuracy')

pl.plot(scalex,scaley)
pl.show()

# <codecell>

scalex = time_final[11:16]
scaley = accuracy[11:16]
title('time vs accuracy:min_size')
xlabel('Execution time')
ylabel('Accuracy')

pl.plot(scalex,scaley)
pl.show()

# <codecell>

scalex = time_final[16:21]
scaley = accuracy[16:21]
title('time vs accuracy:max_size')
xlabel('Execution time')
ylabel('Accuracy')

pl.plot(scalex,scaley)
pl.show()

