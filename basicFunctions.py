from myro import *

trans = 0
rotat = 0

def setTrans(i):
	trans = i

def setRotat(i):
	rotat = i

def turnRight():
	global trans, rotat
	move(trans, rotat)

def turnLeft():
	global trans, rotat
	move(trans, -rotat)

def moveForward():
	forward(1)

def moveBackward():
	forward(-1)

