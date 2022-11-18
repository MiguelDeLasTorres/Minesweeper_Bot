import math

import cv2 as cv
import numpy as np
from PIL import ImageGrab

def LoadImage(x, y, i, j):
    bbox = (x, y, i, j)
    im = ImageGrab.grab(bbox)
    return im

def getImageGray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray

def setupTemplates(images):
    templates = []
    for image in images:
        template = cv.imread(image,0)
        w, h = template.shape[::-1]
        templates.append(template)
    return templates

def matching_templates(templates , img_gray, threshold=0.9):
    locs = []
    i = 0
    for template in templates:
        if i==10:
            threshold = 0.96
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        locs.append(loc)
        i+=1
    return locs

def locsToGrid(locs, w, h, gridW, gridH):
    grid = [0] * (gridW*gridH)
    i = 0
    for loc in locs:
        for pt in zip(*loc[::-1]):
            x = math.floor(pt[0]/w*gridW)
            y = math.floor(pt[1]/h*gridH)
            grid[x+y*9] = i
        i+=1
    return grid