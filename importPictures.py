#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:53:53 2018

@author: rwilson
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#from skimage.color import rgb2gray
from PIL import Image
import os

class importPictures:

    imageSize = 100
    imageGrayScale = 0


    def __init__(self):
        self.imageSize = 100
        self.imageGrayScale = 0

    def setSizeTo(self, size):
        self.imageSize = size

    def setWantGrayScale(self, wantGrayScale):
        self.imageGrayScale = wantGrayScale

    def firstMethod(self):
        print ("first method")
        
    def resize(self, img, max_px_size):
        width_0, height_0 = img.size
    
        if width_0 > height_0:
            new_size = (width_0, width_0)
            new_im = Image.new("RGB", new_size)
            new_im.paste(img, ((new_size[0]-width_0)/2,(new_size[1]-height_0)/2))
            wpercent = max_px_size / float(width_0)
            wsize = int(float(width_0) * float(wpercent))
            img = new_im.resize((wsize, max_px_size), Image.ANTIALIAS)
    
        if width_0 < height_0:
            new_size = (height_0, height_0)
            new_im = Image.new("RGB", new_size)
            new_im.paste(img, ((new_size[0]-width_0)/2,(new_size[1]-height_0)/2))
            hpercent = max_px_size / float(width_0)
            hsize = int(float(height_0) * float(hpercent))
            img = new_im.resize((hsize, max_px_size), Image.ANTIALIAS)
    
        return img
    
    def getImageNamed(self, filename, ofSize):
        img=Image.open(filename)
        gray = img.convert('LA') 
        newImage = self.resize(gray, ofSize)
        return newImage
    
    def getImagesInDirectory(self, dirName):
        print("getImagesInDirectory dirName: "+dirName)
        images = []
        files = os.listdir(dirName)
        for file in files:
            print("inspecting: "+file)
            if file.endswith("jpg"):
                print("adding "+file)
                cursor = self.getImageNamed(dirName+file, 100)
                images.append(cursor)
                cursor.show()
        return images
        
