from myro import *

<<<<<<< HEAD
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

=======
#ro = 0.8
#tim = 0.95

def turn(ro,tim):
    rotate(ro)
    wait(tim)
    stop()
#getObstacle() => [>1000,>1000,>1000]
>>>>>>> FETCH_HEAD
