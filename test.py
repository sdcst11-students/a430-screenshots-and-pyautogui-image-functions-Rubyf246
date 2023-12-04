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
        
        while i<5:
            pyautogui.click()
            i = i + 1
    except:
        pass
        #for i in range(10):
        #    pyautogui.click()
def chopatree():        
    try: 
        x,y= pyautogui.locateCenterOnScreen('newchopatree.png')
        pyautogui.moveTo(x,y)
        j = 0
        while j < 5:
            pyautogui.click()
            print (j)
            j = j+1
    except:
        pass
   
def master():
    main()
    pyautogui.alert("begin autoclick")
    
    k = 0
    while k < 6:
        plantatree()
        chopatree()
        k = k+1
    pyautogui.alert('finished master')
    while True:
        florist()
        gatherer()
        ecoclick()
        fotuneclick()
        ecomerch()
    
def florist():
        try:
                florists= pyautogui.locateCenterOnScreen("assets/florists.png", confidence=0.6)
                pyautogui.moveTo(florists)
                pyautogui.click()
        except:
                gatherer()
                
def gatherer():
        try:
                gatherer = pyautogui.locateCenterOnScreen("assets/gather.png", confidence = 0.6)
                pyautogui.moveTo(gatherer)
                pyautogui.click()
        except: 
                ecoclick()
def ecoclick():
        try:
                ec = pyautogui.locateCenterOnScreen("assets/ecoclick.png", confidence = 0.6)
                pyautogui.moveTo(ec)
                pyautogui.click()
        except:
                fotuneclick()
def fotuneclick():
        try:
                fc = pyautogui.locateCenterOnScreen("assets/fortuneclick.png", confidence = 0.6)
                pyautogui.moveTo(fc)
                pyautogui.click()
        except:
                ecomerch()
def ecomerch():
        try:
                em = pyautogui.locateCenterOnScreen("assets/ecomerch.png", confidence = 0.6)
                pyautogui.moveTo(em)
                pyautogui.click()
        except:
                pyautogui.alert("finsihed")
                master()
        

master()



