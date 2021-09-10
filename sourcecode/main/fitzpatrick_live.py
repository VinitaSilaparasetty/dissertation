# -*- coding: utf-8 -*-
"""fitzpatrick_live_new.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JHpwSd1SBOjzgZaPWyWD5b-au_7IDCl8
"""

# Python code for Multiple Color Detection
  
import numpy as np
import cv2
  
# Capturing video through webcam
webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print("Cannot open camera")
    exit()
  
# Start a while loop
while(1):
# Reading the video from the webcam in image frames 

    ret,imageFrame = webcam.read()
    
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    
    # Convert the imageFrame in BGR(RGB color space) to HSV(hue-saturation-value) color space
    hsvFrame = cv2.cvtColor(imageFrame,cv2.COLOR_BGR2HSV)
  
    # Set range for type1 and define mask
    I_lower = np.array([31.64,21.57,100.0], np.uint8)
    I_upper = np.array([20.8,29.41, 100.0], np.uint8)
    I_mask = cv2.inRange(hsvFrame, I_lower, I_upper)
  
    # Set range for type2 and define mask
    II_lower = np.array([17.65, 33.33, 100.0], np.uint8)
    II_upper = np.array([17.6, 33.33, 88.24], np.uint8)
    II_mask = cv2.inRange(hsvFrame, II_lower, II_upper)
  
    # Set range for type3 and define mask
    III_lower = np.array([18.0,33.33, 82.35], np.uint8)
    III_upper = np.array([18.0, 33.33, 70.59], np.uint8)
    III_mask = cv2.inRange(hsvFrame, III_lower, III_upper)
    
    
    # Set range for type4 and define mask
    IV_lower = np.array([17.45,33.33, 64.71], np.uint8)
    IV_upper = np.array([17.33,33.33,52.94], np.uint8)
    IV_mask = cv2.inRange(hsvFrame, IV_lower, IV_upper)
    
    
    # Set range for type3 and define mask
    V_lower = np.array([18.0,33.33,47.06], np.uint8)
    V_upper = np.array([18.0, 33.33,35.29], np.uint8)
    V_mask = cv2.inRange(hsvFrame, V_lower, V_upper)
    
    
    # Set range for type3 and define mask
    VI_lower = np.array([16.8,33.33, 29.41], np.uint8)
    VI_upper = np.array([327.27,24.44,17.65], np.uint8)
    VI_mask = cv2.inRange(hsvFrame, VI_lower, VI_upper)
      
    # Morphological Transform, Dilation for each color and bitwise_and operator between imageFrame and mask determines to detect only that particular color
    kernel = np.ones((5, 5), "uint8")
      
    # For type1
    IV_mask = cv2.dilate(IV_mask, kernel)
    res_IV = cv2.bitwise_and(imageFrame, imageFrame, 
                              mask = IV_mask)
      
    # For type2
    II_mask = cv2.dilate(II_mask, kernel)
    res_II = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = II_mask)
      
    # For type3
    III_mask = cv2.dilate(III_mask, kernel)
    res_III = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = III_mask)
    
    
    # For type4
    IV_mask = cv2.dilate(IV_mask, kernel)
    res_IV = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = IV_mask)
    
    
    # For type5
    V_mask = cv2.dilate(V_mask, kernel)
    res_V = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = V_mask)
    
    
    # For type6
    VI_mask = cv2.dilate(VI_mask, kernel)
    res_VI = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = VI_mask)
    
   
    # Contour to track type1
    contours, hierarchy = cv2.findContours(I_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Type I", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))    
  
    # Contour to track type2
    contours, hierarchy = cv2.findContours(II_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h),
                                       (0, 255, 0), 2)
              
            cv2.putText(imageFrame, "Type 2", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 
                        1.0, (0, 255, 0))
  
    # Contour to track type3
    contours, hierarchy = cv2.findContours(III_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(imageFrame, "Type III", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
      
    
    # Contour to track type4
    contours, hierarchy = cv2.findContours(IV_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Type IV", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))
   

    # Contour to track type5
    contours, hierarchy = cv2.findContours(V_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Type V", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))

    # Contour to track type6
    contours, hierarchy = cv2.findContours(VI_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y), 
                                       (x + w, y + h), 
                                       (0, 0, 255), 2)
              
            cv2.putText(imageFrame, "Type VI", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (0, 0, 255))


    # Program Termination
    cv2.imshow("Fitzpatrick Skin Type Classification", imageFrame)
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
webcam.release()
cv2.destroyAllWindows()