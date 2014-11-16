from myro import *


#Rotation Value
trrot = 0.8
trtim = 0.95

#Move Straight Value
mvspd = 1
mvtim = 0.5

#Collision Detection Value
colDecFluke = 680
colDecIR = 10


# Basic Myro Commands:
def getJoystick():
    gamePad()

def getSensor():
    senses()

# Basic turn and move function
def turn(ro,tim):
    rotate(ro)
    wait(tim)
    stop()

def turnLeft():
    turn(-trrot, trtim)

def turnRight():
    turn(trrot, trtim)

def mv_nostop(speed,time):
    move(speed)
    wait(time)

def mv(speed , time):
    move(speed)
    wait(time)
    stop()

def mvForward():
    mv(mvspd, mvtim)

def mvBackward():
    mv(-mvspd, mvtim)

# Fluke Board Collision Detection check
def flukeCheck():
    L,C,R = getObstacle()
    if L > colDecFluke and C > colDecFluke and R > colDecFluke:
    	return True
    else:
        return False

def flukeCheckLeft():
    L = getObstacle(0)
    if L > colDecFluke:
	return True
    else:
        return False

def flukeCheckRight():
    R = getObstacle(2)
    if R > colDecFluke:
	return True
    else:
        return False

def flukeCheckCenter():
    C = getObstacle(1)
    if C > colDecFluke:
        return True
    else:
        return False

# IR Collision Check
def irCheck():
    val = getIR()
    if val[0] > colDecIR and val[1] > colDecIR:
        return True
    else:
        return False

def irCheckLeft():
    val = getIR(0)
    if val > colDecIR:
        return True
    else:
        return False

def irCheckRight():
    val = getIR(1)
    if val > colDecIR:
 	return True
    else:
	return False

#Check boundary function
def checkBoundary():
    if getLine(0) == 1 and getLine(1) == 1:
        return True
    else:
        return False
