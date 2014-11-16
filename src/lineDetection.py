
from myro import *
initialize("/dev/tty.IPRE6-196107-DevB")


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
    if getLine(0) == 1 and getLine(1) == 1:
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
            move(-1,0)
            wait(1.1)
            stop()
            leftRotate()
            move(1,0)
            wait(0.5)
            stop()
            
        else:
            move(0.5,0)
            wait(0.5)
            #stop()
            #wait(1)



main()
        
            
        






