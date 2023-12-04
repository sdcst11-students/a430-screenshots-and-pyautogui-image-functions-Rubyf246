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
        x,y= pyautogui.locateCenterOnScreen('assets/newgame.png', confidence=0.9)
        pyautogui.moveTo(x,y)
        pyautogui.click ()
    except:
        pass
def plantatree():
        x,y = pyautogui.locateCenterOnScreen('assets/newplantatree.png', confidence = 0.9)
        pyautogui.moveTo(x,y)
        for i in range(300):
            pyautogui.click()
            i = i + 1
    except:
        pass
        #for i in range(10):
        #    pyautogui.click()
def chopatree():        
    #try: 
        chop= pyautogui.locateCenterOnScreen('newchopatree.png', confidence=0.3)
   
        if chop:
         
            print(str(chop),'found',chop.x,chop.y)
            pyautogui.click(chop)
        
        #pyautogui.moveTo(chop)
        #j = 0
        #while j<500:
        #  
        #    pyautogui.click(chop)
        #    j = j + 1
            
    #except:
    #    pass

def master():
    main()
    k = 0
    while k < 3:
        plantatree()
        chopatree()
        k = k +1 
    
    #florist()     
#def florist():
#    try: 
#        coordsflor= pyautogui.locateCenterOnScreen("assets/florists.png", confidence=0.9)
#        #coordsflor is not None
#        pyautogui.moveTo(coordsflor)
#        pyautogui.click()
#    except:
#        master()
    

#coordsgather= pyautogui.locateCenterOnScreen("assets/gather.png", confidence=0.9)
#pyautogui.moveTo(coordsgather)
#pyautogui.click()

#florist()


#chopatree()
master()




