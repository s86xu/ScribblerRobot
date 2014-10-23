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

def cruise(speed, time):
    move(speed, 0)
    wait(time)
    stop()

def cruise(): # movevent forward for a fixed distance, change the variable.
    cruiseSpeed = 1
    time = 0.7
    cruise(cruiseSpeed, time)

def checkObstacle(): # check obstacle function, main func. Perhaps need tweaking
    L,C,R = getObstacle()
    if L > 800 or C > 800 or R > 800:
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
    else:OB
        return False


# //----------------------------------------------------------------------------------
def Straight():

    switch = False # initialize the switch
    count = -1 # check if this should be 0 or -1

    print "Initial Trigger Object Detected!"

    switch = True # initialized the switch

    while(switch): # bot stuck in first stage, keep track of distance traveled
        count += 1
        switch = stageOne()# switch should be in OFF for this loop to break.

    leftRotate()
    cruise(1, 0.5)

    rightRotate()
    cruise(1,0.5)

    switch = True # reset the switch
    cruis()

    print "Stage One Complete! Moving on to Stage Two."

    # //---------------------------------------------------------------------------------
    while(switch): # bot stuck in stage 2
        switch = stageTwo() # switch should be off for this loop to break.
    leftRotate()
    move(1,0)
    wait(0.5)
    stop()
    rightRotate()

    print "Stage Two Complete! Moving back to the Origional Rotation"

    # //----------------------------------------------------------------------------------
    for i in range(0, count): # Check value for 1 or 0, //return to the regular distance
        cruise()

    leftRotate() # Return to the origional facing position

    # //----------------------------------------------------------------------------------
    cruise() # End of the body() function

# //---------------------------------------------------------------------------------

def leftOne():
    leftRotate()
    cruise()
    rightRotate()
    cruise()

def leftTwo():
    rightRotate()
    cruise()
    leftRotate()
    cruise()

def rightOne():
    rightRotate()
    cruise()
    leftRotate()
    cruise()

def rightTwo():
    leftRotate()
    cruise()
    rightRotate()
    cruise()

def Diag(case):
    if case == 1: # Object on the Right side.

    elif case == 2: # Object on the Left side.

    #else:

# //----------------------------------------------------------------------------------
def main():

    while(not checkObstacle()): # while there is no obsticle in front, move forward
        move(1,0)
    stop()


    leftRotate()
    bolLeft = checkObstacle()

    rightRotate()
    rightRotate()
    bolRight = checkObstacle()

    leftRotate()

    if bolRight == False and bolLeft == False:
        Straight()
    elif bolRight:
        Diag(1)
    elif bolLeft:
        Diag(2)


# //-----------------------------------------------------------------------------------

main() # The start of the program.


