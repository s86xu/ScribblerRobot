#Obstacle Avoidance
from myro import *
initialize("/dev/tty.IPRE6-196107-DevB")

cruiseSpeed = 0.6
turnSpeed = 0.5

def leftRotate():
    rotate(0.8)
    wait(0.95)
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


def main():

while True:
    
            if checkObstacle():
                leftRotate()
                move(cruiseSpeed,0)
                wait(0.5)
                rotateRight()
            elif #Some condition here:
                move(cruiseSpeed,0)
                rotateRight()
                if checkObstacle():
                    rotateLeft()

        
                
