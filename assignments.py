#!python3
import pyautogui

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
        pyautogui.click (x,y)
    except:
        x=1215
        y=357
        coordsplant = pyautogui.locateCenterOnScreen('assets/plantatree.png', confidence = 0.9)
        pyautogui.moveTo(coordsplant)
        for i in coordsplant:
            pyautogui.mouseDown(i)


main()




