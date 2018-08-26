# 'Vladislava Evtushenko.png'
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from skimage.color import rgb2gray
from PIL import Image
import os


class importPics:
    
    def resize(self,img, max_px_size):
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
    
    def getImageNamed(self,filename, ofSize):
        img=Image.open(filename)
        gray = img.convert('LA') 
        newImage = resize(gray, ofSize)
        return newImage
    
    def getImagesInDirectory(self,dirName):
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
    

getter = importPics()
footballs = getter.getImagesInDirectory("/Users/rwilson/Desktop/football/")

#img = getImageNamed('/Users/rwilson/Pictures/Vladislava Evtushenko.png', 50)
#imgplot = plt.imshow(img)



##########################################3
'''
import tensorflow as tf
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)
'''
