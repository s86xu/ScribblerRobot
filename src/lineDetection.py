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
    rotate(-0.8)#speed
    wait(0.95)#this is how long the rotation is
    stop()

def rightRotate():
    rotate(0.8)
    wait(0.95)
    stop()

def checkObstacle():
    L,C,R = getObstacle()
    if L > 1000 and C > 1000 and R > 1000:
        return True
    else:
        return False
def checkBoundary():
    if getLine(0) == 0 and getLine(1) == 0:
        return True
    else:
        return False

def main():

    while True:

        #if checkObstacle():
            #stop()
            #break
        if checkBoundary():
            #leftRotate()
            #move(-1,0)
            #wait(0.5)
            move(1,0)
            wait(1.0)
            stop()
            leftRotate()
            move(-1,0)
            wait(0.5)
            stop()
            
        else:
            move(-1,0)
            wait(0.5)
            #stop()
            #wait(1)



main()
        
            
        






