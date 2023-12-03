#!python3
import pyautogui
import time

#Main Task
#Click the “plant a tree” button repeatedly


#Task 1:
#Every 3 minutes:
#Click on “chop a tree” repeatedly until you run out of trees 


#Task 2:
#After clicking “chop a tree”, click on different roles to buy. 
#After buying a desire amount of people, click back to Main Task


#It should make use of functions and function calls to help break up your program into manageable tasks
#It should incorporate a for loop
#There should be a decision making process using if statements
#A while loop should be incorporated to keep the program repeating
#Use of a variables, including a list type variable must be part of your program.

def main():
    try:
        x,y = pyautogui.locateCenterOnScreen('assets/newgame.png', confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click ()
    except:
        pass
    
def plantatree():
    try:
        x,y = pyautogui.locateCenterOnScreen('newplantatree.png', confidence=0.6) 
        pyautogui.moveTo(x,y)
        i=0
        while i<500:
            pyautogui.click()
            i = i + 1
    except:
        pass

def chopatree():
    try:
        x,y = pyautogui.locateCenterOnScreen('newchopatree.png') 
        pyautogui.moveTo(x,y)
        j=0
        while j<503:
            pyautogui.click()
            print (j)
            j = j + 1
    except:
        pass    
    
    #try:
        #position2 = pyautogui.locateCenterOnScreen("newchopatree.png", confidence=0.3)
        #x = position2[0]
        #y = position2[1]
        #print(x,y)
        #print('Found! Clicking above the image')
#
        #pyautogui.moveTo(x,y)
        #time.sleep(1)
       ## pyautogui.click(button='left')
        #time.sleep(1)
    #except:
        #pass
        #print("Fail! Didn't find the image")
    
def master():
    main()
    k = 0
    while k < 6:
        print (k)
        plantatree()
        chopatree()
        k = k+1
    
master()