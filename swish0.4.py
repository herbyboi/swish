#imports ======================

import cv2  # image processing > pip install opencv-python
import numpy as np # cv2 dependency (math oriented module) > installed automatically when you do > pip install opencv-python
import time # default python library comes preinstalled
from PIL import ImageGrab # image oriented library (used for screenshots, any similar way would work most likely) > pip install Pillow
from pynput.keyboard import Key, Controller # input library (emulates keyboard and mouse) best from what i tried so far > pip install pynput
keyboard = Controller() # creating keyboard object from imported class
from pynput.mouse import Button, Controller as mouseCont # input library (emulates keyboard and mouse) best from what i tried so far > pip install pynput  !!! important to import as something else then keyboard class to avoid conflicts
mouse = mouseCont() # creating mouse object from imported class



#constants ===================

bait = cv2.imread("bait.png",0) #loading premade image of reel icon, 0 is used to import in grayscale (no color mode)
bait_w,bait_h = bait.shape[::-1] #getting height and width of the icon using the imported image
threshold = 0.8 #constant for brute force matching - no need if image is
run = True # just a run condition cuz of cource we need more useless variables
# def functions ==================
########################### literraly reel
def reel():
    print("dbgfish")
    keyboard.press("f")
    keyboard.release("f")
################################################## same as reel just for hotbar
def toss(hotbar):
    keyboard.press(hotbar)
    keyboard.release(hotbar)




####################### function which gonna fetch the screenshot for as #####################################
def recieve_frame(bait,threshold):
    frame = cv2.cvtColor(np.array(ImageGrab.grab(bbox = None)),cv2.COLOR_BGR2GRAY)   ####################formatting screenshot into a processable format
    res = cv2.matchTemplate(frame,bait,cv2.TM_CCOEFF_NORMED)    ############ using cv2 algorithm for template matching
    pts = np.where( res >= threshold)  #### selecting results
    arr = [] #storing all of them just in case, and thats why i made an empty arrayss
    for pt in zip(*pts[::-1]): # yeeting all of the items in results to an array
        arr.append(pt)
    return(arr) #return the array





######################### main loop ##################################
hotbar = input("hotbar >> ")
while run:

    arr = recieve_frame(bait, threshold)
    if len(arr) > 0: # on at least one similarity with the bait image we do the following
        reel()  #call the reel
        time.sleep(3) # sleep so it actually reels
        toss(hotbar)
