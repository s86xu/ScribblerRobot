# Obstacle Avoidance

# initialize the whole program and port
from myro import *
initialize("/dev/tty.IPRE6-196107-DevB") # string can be removed to make it ask for port.

def leftRotate(): # Rotate 90 to the left
    rotate(0.8)
    wait(0.95)
    stop()

def rightRotate(): # Rotate 90 to the right
    rotate(-0.8)
    wait(0.95)
    stop()

def cruise(): # movevent forward for a fixed distance, change the variable.
    cruiseSpeed = 0.6
    time = 0
    move(cruiseSpeed, time)

def checkObstacle(): # check obstacle function, main func. Perhaps need tweaking
    L,C,R = getObstacle()
    if L > 1000 and C > 1000 and R > 1000:
        return True
    else:
        return False

def stageOne(): # check for object avoid while it is in first stage.
    if checkObstacle():
        leftRotate()
        cruise()
        rotateRight()
        return True
    else:
        return False

def stageTwo():  # check for object while in second stage
    rightRotate()
    if checkObstacle():
        leftRotate()
        cruise()
        return True
    else:
        return False



def body():

    switch = False # initialize the switch
    count = -1 # check if this should be 0 or -1

    while(not checkObstacle()): # while there is no obsticle infront, move forward
        move(1,0)
    stop()

    switch = True # initialized the switch

    while(switch): # bot stuck in first stage, keep track of distance traveled
        count += 1
        switch = stageOne() # switch should be in OFF for this loop to break.

    switch = True # reset the switch
    cruise()
	
    while(switch): # bot stuck in stage 2
        switch = stageTwo() # switch should be off for this loop to break.

    for i in range(1, count): # Check value for 1 or 0, //return to the regular distance
        cruise()

    rotateLeft() # Return to the origional facing position

    cruise() # End of the body() function

def main():
    count = 2 # the number of obsticle that it need to pass through before it shutdown.
    for i in range(1, count):
         body()

main() # The start of the program.


