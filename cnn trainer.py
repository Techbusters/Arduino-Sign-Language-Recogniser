# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 07:39:38 2018

@author: dcdev
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:36:58 2018

@author: dcdev
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 14:27:00 2018

@author: dcdev
"""
import numpy as np

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten


classifier = Sequential()
    
classifier.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(64,64,3)))
    
classifier.add(Conv2D(32, (3, 3), activation='relu'))

classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Dropout(0.25))
 
classifier.add(Conv2D(64, (3, 3), padding='same', activation='relu'))

classifier.add(Conv2D(64, (3, 3), activation='relu'))

classifier.add(MaxPooling2D(pool_size=(2, 2)))

classifier.add(Dropout(0.25))
 
classifier.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
classifier.add(Conv2D(64, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Dropout(0.25))
 
classifier.add(Flatten())
classifier.add(Dense(512, activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(12, activation='softmax'))


classifier.compile(optimizer = 'adam',loss = 'categorical_crossentropy',metrics=['accuracy'])


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255, #So that values are b/w 0 and 1
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        directory = './dataset/training_set',
        target_size=(64 ,64),
        batch_size=32,
        class_mode='categorical')

test_set = test_datagen.flow_from_directory(
        directory = './dataset/test_set',
        target_size=(64 , 64),
        batch_size=32,
        class_mode='categorical')

classifier.fit_generator(training_set,
                        steps_per_epoch=250,
                        epochs=25,
                        validation_data=test_set,
                        validation_steps=63)


import os
os.system('say "your program has finished"')       

classifier.save('myModeldataset1') 