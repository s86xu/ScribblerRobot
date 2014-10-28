#Obstacle Avoidance

#notes
#you cannot move and detect at the same time
#check object before boundary

#getLine()

#after command, wait, and check
#if found object, turn off incruising and 

from myro import *
initialize("/dev/tty.IPRE6-196107-DevB")

cruiseSpeed = 0.6
turnSpeed = 0.5

inTurning = False
inTurningCount = 0
inCruising = True
inCruisingCound = 0

seenObstacle = False

hardDistance = 10

def leftRotate():
    rotate(0.8)#speed
    wait(0.95)#this is how long the rotation is
    stop()

def rightRotate():
    rotate(-0.8)
    wait(0.95)
    stop()

def checkObstacle():
    L,C,R = getObstacle()
    if L > 1000 and C > 1000 and R > 1000:
        return True
    else:
        return False
def checkBoundary():
    if getLine('left') == 1 and getLine('right') == 1:
        return True
    else:
        return False

def main():

    while True:

        if checkObstacle():
            stop()
            break
        elif checkBoundary():
            leftRotate()
            move(1,0)
            wait(0.5)
            stop()
        move(1,0)

        
            
        





            """
            rotateRight()
            if checkObstacle():
                rotateLeft()
                """

"""
        if inCruising:
            
            wait
            check if object detection now, or else just move
            
            wait(0.1)
            

            
            if found object (if checkObstacle is true)=> INCRUISING OFF->beep
            

            
            if distance reached => INCRUISING OFF , INTURNING ON
            


            
            else => just move,  increase distance
            


        #elif inCruising == False:
            
            
        elif inCruising == False and inTurning == True:
            wait(5)
            break




        
        
        
        
    
"""
