# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

# <codecell>

%pylab inline

# import OpenCV computer vision library
import cv2

import os
import glob

# import the standard numerical and plotting packages
import numpy as np
import matplotlib.pyplot as plt

# <codecell>

def best_match(template_img, scene_img, minsize, maxsize):
    """ Get the best match for a template image within a scene image,
        rescaling the template width between minsize and maxsize
        while maintaining the aspect ratio.
        Returns two 2-tuples of ints:
            corner is the (x,y) position of the upper-left corner of the template in the scene
            wh is (width, height)
    """
    # widths is all the widths to try
    widths = np.arange(minsize, maxsize, dtype=int)
    # aspect_ratio is height/width of the template image
    aspect_ratio = template_img.shape[0] / float(template_img.shape[1])
    # heights is all the heights to try
    heights = np.asarray(aspect_ratio*widths, dtype=int)
    
    # best_scores will store the best score for each width
    best_scores = np.zeros(len(widths))
    # best_positions will store the best (x,y) positions of the template for each width
    best_positions = np.zeros([len(widths), 2], dtype=int)
    
    # scan widths
    for isize in range(widths.size):
        # log
        #print "resizing to width = %d" % widths[isize]
        
        # resize
        resized_template_img = cv2.resize(template_img, (widths[isize], heights[isize]))
        
        # match
        scores = cv2.matchTemplate(scene_img, resized_template_img, method=cv2.TM_CCORR_NORMED)
        
        # get best score and position
        min_score, max_score, (min_x, min_y), (max_x, max_y) = cv2.minMaxLoc(scores)
        
        # store best score and position
        best_scores[isize] = max_score
        best_positions[isize] = [max_x, max_y]
        
    # choose best overall match
    best_isize = np.argmax(best_scores)
    best_width = widths[best_isize]
    best_position = best_positions[best_isize]
    
    # plot scores
    plt.plot(widths, best_scores)
    plt.arrow(widths[best_isize], 0, 0, 1, color='r')
    plt.xlabel('template width')
    plt.ylabel('score')
    
    # return
    return tuple(best_positions[best_isize]), (widths[best_isize], heights[best_isize])

def imshow_highlighted(img, corner, wh, rgb=(0,255,0), stroke=5):
    """ Show an image with a highlighted rectangle.
        corner is a (x_upperleft, y_upperleft) tuple of ints,
        wh is a (width, height) tuple of ints,
        rgb is an optional (r,g,b) tuple (default green),
        stroke is an optional number of pixels for rectangle stroke (default 5).
    """
    # copy the image so we don't modify the original
    img_highlighted = img[:,:,[2,1,0]].copy()
    
    # add a rectangle
    cv2.rectangle(img_highlighted, corner, (corner[0]+wh[0], corner[1]+wh[1]), rgb, stroke)
    
    # show
    plt.figure()
    plt.imshow(img_highlighted)

# <codecell>

ROI_Dictionary = dict()
scene_file = ["/home/chenmia/timeWindowPics/0228/25/038.tiff","/home/chenmia/timeWindowPics/0234/25/038.tiff","/home/chenmia/timeWindowPics/0221/00/038.tiff","/home/chenmia/timeWindowPics/0228/00/038.tiff","/home/chenmia/timeWindowPics/0234/00/038.tiff","/home/chenmia/timeWindowPics/0228/25/038.tiff","/home/chenmia/timeWindowPics/0234/25/038.tiff","/home/chenmia/timeWindowPics/0228/50/038.tiff","/home/chenmia/timeWindowPics/0234/50/038.tiff","/home/chenmia/timeWindowPics/0228/75/038.tiff","/home/chenmia/timeWindowPics/0234/75/038.tiff","/home/chenmia/timeWindowPics/0228/90/038.tiff","/home/chenmia/timeWindowPics/0234/90/038.tiff","/home/chenmia/timeWindowPics/0184/100/038.tiff","/home/chenmia/timeWindowPics/0190/100/038.tiff","/home/chenmia/timeWindowPics/0197/100/038.tiff","/home/chenmia/timeWindowPics/0234/100/038.tiff","/home/chenmia/timeWindowPics/0185/100/038.tiff","/home/chenmia/timeWindowPics/0191/100/038.tiff"]
for i in scene_file:
 #print i
 #scene_file = "/home/chenmia/timeWindowPics/0228/00/038.tiff"
 template_file = os.path.join(TEMPLATE_DIR,"0228_000_038.tif")
 template_img = cv2.imread(template_file)
 #scene_img = cv2.imread(scene_file)
 scene_img = cv2.imread(i)
 scene_img = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)
 corner, wh = best_match(template_img, scene_img, 100, 200)
 ROI_Dictionary[i] = corner
 imshow_highlighted(scene_img, corner, wh)  
 
for file in ROI_Dictionary:
 print file

# <codecell>


