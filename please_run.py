# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:37:27 2018

@author: dcdev
"""
import keras.models

classifierLoaded = keras.models.load_model('myModel') 

alpha = [ 'A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R',
         'S','T','U','V','W','X','Y']

classifierLoaded = keras.models.load_model('myModel') 
from skimage.io import imread
from skimage.transform import resize
import cv2
import numpy as np
cap = cv2.VideoCapture(1)
import time

count = 0

print(classifierLoaded)

     
while(1):
    x, y, w, h = 300, 100, 300, 300    
    try:  #an error comes if it does not find anything in window as it cannot find contour of max area
          #therefore this try error statement
          
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((3,3),np.uint8)
        
        #define region of interest
        roi=frame[100:300, 100:300]
        
        
        rect = cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)  
        #img = cap.read()[1]
        
        #k = cv2.waitKey(5) & 0xFF
        
        #img = roi.read()[1]
        
        #-------------------------------------------
        
         #define region of interest
        roi=frame[100:300, 100:300]
        
        
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        
         
    # define range of skin color in HSV
        lower_skin = np.array([0,20,70], dtype=np.uint8)
        upper_skin = np.array([20,255,255], dtype=np.uint8)
        
     #extract skin colur imagw  
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        
        
    #extrapolate the hand to fill dark spots within
        mask = cv2.dilate(mask,kernel,iterations = 4)
        
    #blur the image
        mask = cv2.GaussianBlur(mask,(5,5),100) 
        
        
        #img = cap.read()[1]
        
		
        #img = cv2.flip(img, 1)
		
        #imgCrop = img[y:y+h, x:x+w]
		
        #imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
        #dst = cv2.calcBackProject([imgHSV], [0, 1], hist, [0, 180, 0, 256], 1)
		
        #disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
		
        #cv2.filter2D(dst,-1,disc,dst)
		
        #blur = cv2.GaussianBlur(dst, (11,11), 0)
		
        #blur = cv2.medianBlur(blur, 15)
		
        #thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
		
        #thresh = cv2.merge((thresh,thresh,thresh))
		
        #thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
		
        #thresh = thresh[y:y+h, x:x+w]
		
        #contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
        
        #-------------------------------------------
        """
        cv2.imwrite("mask.jpg", mask)
        img = imread('mask.jpg')
        #img = roi
        img = resize(img,(50,50))
        img = np.expand_dims(img,axis=0)
 
        
        if(np.max(img)>1):
            img = img/255.0
        
        
        pred_probab = classifierLoaded.predict(img)
        val = np.argmax(pred_probab,axis=1)
        print( 'prediction : ' , alpha[val[0]]  )
        """
        
        cv2.imshow("mask", mask)
        cv2.imshow('frame',frame)
        
        
    except:
        print('Passing')
        pass
        
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.imwrite("roi.png", roi)
        break

#my_predict(np.zeros((50, 50), dtype=np.uint8))
cv2.destroyAllWindows()
cap.release()        