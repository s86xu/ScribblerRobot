from myro import *


#Rotation Value
ro = 0.8
rotim = 0.95

#Move Straight Value
mv = 1
mvtim = 0.5

#Collision Detection Value
colDecFluke = 1000
colDecIR


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
    rotate(ro)
    wait(rotim)
    stop()

def turnRight():
    rotate(-ro)
    wait(rotim)
    stop

def mvForward():
    move(mv, 0)
    wait(mvtim)
    stop()

def mvBackward():
    move(-mv, 0)
    wait(mvtim)
    stop()

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

# Picture Taking
def snapShot():
    img = takePicture()
    show(img)

# Music function()
def play(title):
    #robot.
    playSong(readSong(title))

#Speaking
def say(word):
    speak(word)
