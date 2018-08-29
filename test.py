#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:53:15 2018

@author: rwilson
"""
import importPictures as myModule
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

t = myModule.importPictures()
t.firstMethod()

array = t.getImagesInDirectory('images/football/')
img = array[2]
imgplot = plt.imshow(img)
plt.show()
