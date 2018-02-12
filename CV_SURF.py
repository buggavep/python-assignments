# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


# <codecell>

%pylab inline

import cv2
import numpy as np

img = cv2.imread('/home/CV/HW7Images/home.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show the original image
imshow(img)

# <codecell>

detector = cv2.FeatureDetector_create("SURF")
descriptor = cv2.DescriptorExtractor_create("SURF")

# Scene Keypoints are the descriptor location (x,y),magnitude,angle
skp = detector.detect(img)

# You can get the location of the keypoint descriptor
# Note: casting fields to INT
point = (int(skp[0].pt[0]), int(skp[0].pt[1]))
print point, skp[0].angle, skp[0].size

# <codecell>

# Scene Descriptors (in SIFT cases 128 values) as a numpy array
skp, sd = descriptor.compute(img, skp)

# the 128 values of the first keypoint
print len(sd[0])
print sd[0]

# <codecell>

img=cv2.drawKeypoints(gray,skp)
imshow(img)

# <codecell>

img=cv2.drawKeypoints(gray,skp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
imshow(img)

# <codecell>


