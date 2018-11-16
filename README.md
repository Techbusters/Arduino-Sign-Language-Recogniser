# Arduino-Sign-Language-Recogniser

An apparatus for translating American Sign Language (ASL) using Machine Learning and Arduino Uno

Purpose:

This apparatus is designed for bridging the communication gap between the deaf & dumb people and others of the society. The primary language for communication is the American Sign Language (ASL). Generally, people who are not an expert in this language require an additional human translator to communicate with the deaf & dumb people. Our project aims at creating a model which uses Convolutional Neural Networks in Machine Learning to translate ASL into any other language with the support of Arduino Uno.

Structure:


It contains two parts: one is the arduino based hand motion detector and the other is deep learning model using keras.
The former one is integrated for the ease of hand-eye coordination. The camera will follw the hand motion and rotate to the direction of the hand, so that the user does not have to remain stationary and perform gestures in a limited boundary.
The second part is the heart of the project. It uses Keras backend for predicting the class of the gesture captured by the web-cam, using some pre-trained model.The captured image is processed using OpenCV framework.The model is trained on a dataset which was generated by us. The output is shown as text in a GUI made using Tkinter.


File structures:

The trained model is available in myModeldataset1

The Arduino code is available in MotionSensorCamera.ino

The executable file is Modelpredict.py
