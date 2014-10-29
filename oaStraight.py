# Obstacle Avoidance

# initialize the whole program and port
from myro import *
initialize("/dev/tty.IPRE6-196107-DevB") # string can be removed to make it ask for port.

# COM3 or COM4 or /dev/tty.IPRE6-196107-DevB

def leftRotate(): # Rotate 90 to the left
    rotate(0.8)
    wait(0.95)
    stop()

def rightRotate(): # Rotate 90 to the right
    rotate(-0.8)
    wait(0.95)
    stop()

def cruise(): # movevent forward for a fixed distance, change the variable.
    cruiseSpeed = 1
    time = 0.5
    cruisep(cruiseSpeed, time)

def cruisep(speed, time):
    move(speed, 0)
    wait(time)
    stop()

def checkObstacle(): # check obstacle function, main func. Perhaps need tweaking
    L,C,R = getObstacle()
    v = 700  # 850 for Straight()
    if L > v and C > v and R > v:
        return True
    else:
        return False

# //-----------------------------------------------------------------------------
def stageOne(): # check for object avoid while it is in first stage.
    if checkObstacle():
        leftRotate()
        cruise()
        rightRotate()
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

def Straight():

    print "Object is Directly ahead. Straight() Run."

    count = -1 # check if this should be 0 or -1
    switch = True # initialized the switch

    while(switch): # bot stuck in first stage, keep track of distance traveled
        count += 1
        switch = stageOne()# switch should be in OFF for this loop to break.

    leftRotate()
    cruisep(0.8, 0.7)

    rightRotate()
    cruisep(0.8,0.7)

    switch = True # reset the switch
    cruise()

    print "Stage One Complete! Moving on to Stage Two."

    while(switch): # bot stuck in stage 2
        switch = stageTwo() # switch should be off for this loop to break.
    leftRotate()
    cruisep(0.8, 0.6)
    rightRotate()

    print "Stage Two Complete! Moving back to the Origional Rotation"

    print count
    for i in range(0, count): # Check value for 1 or 0, //return to the regular distance
        cruise()

    cruisep(0.8, 0.6)

    leftRotate() # Return to the origional facing position

    cruise() # End of the body() function

# //----------------------------------------------------------------------------------
def main():

    while(not checkObstacle()): # while there is no obsticle in front, move forward
        move(0.8,0)
    stop()

    print "Initial Obsticle Detected"
    Straight()

# //-----------------------------------------------------------------------------------

senses()
main() # The start of the program.


