# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

# import OpenCV computer vision library
import cv2

import os
import glob

# import the standard numerical and plotting packages
import numpy as np
import matplotlib.pyplot as plt

# <headingcell level=2>

# Template Match for Angle Calculation

# <codecell>

def ViewScene(scene_file):
   img = cv2.imread(scene_file)
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   imshow(img)

def MatchTemplate(scene_img, template_img, show_scores=False):
   # cv2.matchTemplate: scan a template image through a scene image and get score for match at each position
   # http://docs.opencv.org/modules/imgproc/doc/object_detection.html?highlight=matchtemplate#cv2.matchTemplate
   scores = cv2.matchTemplate(scene_img,                  # scene image  
                           template_img,                  # template image
                           method=cv2.TM_CCORR_NORMED  # see docs for methods
                          )

   if show_scores:
      plt.imshow(scores)
        
   return scores
    
def FindScoreLocations(scores, template_img, show_coordinates=False):
   # cv2.minMaxLoc: get the min, max, argmin, and argmax of a scores array
   # http://docs.opencv.org/modules/core/doc/operations_on_arrays.html?highlight=minmaxloc#cv2.minMaxLoc
   min_score, max_score, (min_x, min_y), (max_x, max_y) = cv2.minMaxLoc(scores)
   corner_topL = (max_x, max_y)
   corner_botR = (corner_topL[0]+template_img.shape[1], corner_topL[1]+template_img.shape[0])
    
   if show_coordinates:
      print corner_topL, corner_botR
   
   return corner_topL, corner_botR
    
def ShowMatch(scene_img, corners):
    corner_topL = corners[0]
    corner_botR = corners[1]
    scene_img_highlighted = scene_img[:,:,[2,1,0]].copy()
    cv2.rectangle(scene_img_highlighted,  # image to add a rectangle to
              corner_topL,            # upper left corner of rectangle
              corner_botR,            # lower right corner of rectangle
              (0,255,0),              # rgb tuple for rectangle color
              10                      # rectangle stroke thickness (in pixels)
             )
    plt.imshow(scene_img_highlighted)
    
def DrawScoredBox(scene_file, template_file):
    template_img = cv2.imread(template_file)
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
    scene_img = cv2.imread(scene_file)
    scene_img = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)
    scores = MatchTemplate(scene_img, template_img, show_scores=True)
    #corners = FindScoreLocations(scores, template_img, show_coordinates=False)
    #ShowMatch(scene_img, corners)
    
def DrawScoredBoxImg(scene_img, template_img):
    scores = MatchTemplate(scene_img, template_img, show_scores=False)
    corners = FindScoreLocations(scores, template_img, show_coordinates=False)
    ShowMatch(scene_img, corners)
    
def DrawTemplateBoxFile(scene_file, template_file):
    template_img = cv2.imread(template_file)
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
    scene_img = cv2.imread(scene_file)
    scene_img = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)
    DrawScoredBoxImg(scene_img, template_img)

# <codecell>

def RunTemplates(scene_file, template_dir, template_list):
    
    # Scene file
    scene_img = cv2.imread(scene_file)
    scene_img = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)
    
    # Template list
    
    scores_list = list()
    corners_list = list()
    for index in range(len(template_list)): 
        template_file = os.path.join(TEMPLATE_DIR,template_list[index])
        template_img = cv2.imread(template_file)
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
        
        scores = MatchTemplate(scene_img, template_img, show_scores=False)
        scores_list.append(scores)
        corners_list.append(FindScoreLocations(scores, template_img, show_coordinates=False))
        
    return scores_list, corners_list

# <codecell>

ViewScene("/home/CV/Templates/0228_000_038.tif")

# <codecell>

# Sample scoring of one scene and one template
scene_file = "/home/chenmia/timeWindowPics/0228/00/038.tiff"
template_file = "/home/CV/Templates/0228_000_038.tif"

DrawScoredBox(scene_file, template_file)

# <codecell>

# Sample scoring of one scene and one template
scene_file = "/home/chenmia/timeWindowPics/0228/00/038.tiff"
template_file = "/home/CV/Templates/0228_000_038.tif"
DrawTemplateBoxFile(scene_file,template_file)

# <codecell>

def GenerateTemplateList(template_dir, file_pattern):
   template_list = [file for file in os.listdir(template_dir) if file.endswith(file_pattern)]
   return template_list

def PlotTemplateCenters(x_list, y_list):
   colors = np.random.rand(len(x_list))
   area = ones(len(x_list))
   plt.scatter(x_list, y_list, s=area, c=colors, alpha=0.5)
   plt.show()

scene_file = "/home/chenmia/timeWindowPics/0228/00/038.tiff"
TEMPLATE_DIR = "/home/CV/Templates"
template_list = GenerateTemplateList(TEMPLATE_DIR, ".tif")

# <codecell>

score_list, corners_list = RunTemplates(scene_file, TEMPLATE_DIR, template_list)
point_list = [(center[0][0],center[0][1]) for center in corners_list]
x_list = [x for x,y in point_list]
y_list = [y for x,y in point_list]

# <codecell>

PlotTemplateCenters(x_list,y_list)

# <headingcell level=2>

# Best width matching

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
        print "resizing to width = %d" % widths[isize]
        
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
    plt.imshow(img_highlighted)

# <codecell>

scene_file = "/home/chenmia/timeWindowPics/0228/00/038.tiff"
template_file = os.path.join(TEMPLATE_DIR,"0228_000_038.tif")

template_img = cv2.imread(template_file)
template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2RGB)
scene_img = cv2.imread(scene_file)
scene_img = cv2.cvtColor(scene_img, cv2.COLOR_BGR2RGB)

corner, wh = best_match(template_img, scene_img, 20, 30)

# <codecell>

imshow_highlighted(scene_img, corner, wh)

# <rawcell>

# Evaluate the following scene files, but drawing the best BOX around the vocal cord structure
# 
# /home/chenmia/timeWindowPics/0228/25/038.tiff
# /home/chenmia/timeWindowPics/0234/25/038.tiff
# /home/chenmia/timeWindowPics/0221/00/038.tiff
# /home/chenmia/timeWindowPics/0228/00/038.tiff
# /home/chenmia/timeWindowPics/0234/00/038.tiff
# /home/chenmia/timeWindowPics/0228/25/038.tiff
# /home/chenmia/timeWindowPics/0234/25/038.tiff
# /home/chenmia/timeWindowPics/0228/50/038.tiff
# /home/chenmia/timeWindowPics/0234/50/038.tiff
# /home/chenmia/timeWindowPics/0228/75/038.tiff
# /home/chenmia/timeWindowPics/0234/75/038.tiff
# /home/chenmia/timeWindowPics/0228/90/038.tiff
# /home/chenmia/timeWindowPics/0234/90/038.tiff
# /home/chenmia/timeWindowPics/0184/100/038.tiff
# /home/chenmia/timeWindowPics/0190/100/038.tiff
# /home/chenmia/timeWindowPics/0197/100/038.tiff
# /home/chenmia/timeWindowPics/0234/100/038.tiff
# /home/chenmia/timeWindowPics/0185/100/038.tiff
# /home/chenmia/timeWindowPics/0191/100/038.tiff

