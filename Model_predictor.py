# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:19:58 2018

@author: dcdev
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 08:07:47 2018

@author: dcdev
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:37:27 2018

@author: dcdev
"""
import keras.models

classifierLoaded = keras.models.load_model('myModeldataset1') 

alpha = [ ' ','C','D','E','H','I','L','O','R','U','W','Y']

import tkinter

classifierLoaded = keras.models.load_model('myModeldataset1') 
from skimage.io import imread
from skimage.transform import resize
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
import time

count = 0

window = tkinter.Tk()
f = tkinter.Text(window, height=50, width=50)
f.pack()
itr = 0


while(1):
    x, y, w, h = 300, 100, 300, 300    
    try:  
        
        itr = itr+1
        
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
        
        roi=frame[100:340, 100:420]
        
        
        rect = cv2.rectangle(frame,(100,100),(420,340),(0,255,0),0)  
        img = cap.read()[1]
        
        cv2.imwrite("roi1.jpg", roi)
        img = imread('roi1.jpg')
        #img = roi
        img = resize(img,(64,64))
        img = np.expand_dims(img,axis=0)
 
        if(np.max(img)>1):
            img = img/255.0
        
        t0 = time.clock()
        
        pred_probab = classifierLoaded.predict(img)
        val = np.argmax(pred_probab,axis=1)
        #print(itr)
        if(itr>=40):
            print( 'prediction : ' , alpha[val[0]]  )
            itr = 0
            f.insert(tkinter.END,str(alpha[val[0]]))
            window.update_idletasks()
            window.update()
        cv2.imshow('frame',frame)
        
        
    except:
        print('Passing')
        pass
        
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()        