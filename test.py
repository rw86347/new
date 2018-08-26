#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:53:15 2018

@author: rwilson
"""
import importPictures as myModule


	

t = myModule.importPictures()

img = t.getImageNamed('images/01.png', 50)
imgplot = plt.imshow(img)
