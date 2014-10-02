# Obstacle Avoidance

from myro import *
initialize("/dev/tty.IPRE6-196107-DevB")

final cruiseSpeed = 0.6
final time = 0.5

def leftRotate():
    rotate(0.8)
    wait(0.95)
    stop()

def rightRotate():
    rotate(-0.8)
    wait(0.95)
    stop()

def cruise():
    global cruiseSpeed, time
    move(cruiseSpeed, time)

def checkObstacle():
    L,C,R = getObstacle()
    if L > 1000 and C > 1000 and R > 1000:
        return True
    else:
        return False

def stageOne():
    if checkObstacle():
        leftRotate()
        cruise()
	rotateRight()
	return True
    else:
	return False

def stageTwo():
    rightRotate()
    if checkObstacle():
	leftRotate()
	cruise()
	return True
    else:
	return False



def main():

    switch = False
    
    while(!checkObstacle()):
	cruise()

    switch = True

    while(switch):
	switch = stageOne()

    switch = True
    cruise()
	
    while(switch):
	switch = stageTwo()

    switch = True

    while(switch):
	cruise()





