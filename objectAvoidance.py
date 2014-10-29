# Obstacle Avoidance

# initialize the whole program and port
from myro import *
initialize() # string can be removed to make it ask for port.

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
    time = 0.7
    cruisep(cruiseSpeed, time)

def cruisep(speed, time):
    move(speed, 0)
    wait(time)
    stop()

def checkObstacle(): # check obstacle function, main func. Perhaps need tweaking
    L,C,R = getObstacle()
    v = 1000
    if L > v and C > v and R > v:
        return True
    else:
        return False


def r_checkObstacle():
    L,C,R = getObstacle()
    if L > 1000 and C > 900:
        return True
    else:
        return False

def l_checkObstacle():
    L,C,R = getObstacle()
    if R > 1000 and C > 900:
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
    cruisep(0.8, 0.6)

    rightRotate()
    cruisep(0.8,0.6)

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

# //---------------------------------------------------------------------------------

def leftOne(): # Object on the Right Side.
    if checkObsticle():
        leftRotate()
        cruise()
        rightRotate()
        cruise()
        return True
    else:
        return False

def leftTwo():
    if checkObsticle():
        rightRotate()
        cruise()
        leftRotate()
        cruise()
        return True
    else:
        return False

def rightOne(): # Object on the LEFT side.
    if checkObsticle():
        rightRotate()
        cruise()
        leftRotate()
        cruise()
        return True
    else:
        return False

def rightTwo():
    if checkObsticle():
        leftRotate()
        cruise()
        rightRotate()
        cruise()
        return True
    else:
        return False

def Diag(case):
    print "Diagonal Case: " + str(case) + " Run."

    count = 0
    switch = True

    if case == 1: # Object on the Right side.

        while switch: # First stage.
            switch = leftOne()
            count += 1

        cruise()
        
        print "Stage One ended."

        switch = True

        while switch and count != 0:
            switch = leftTwo()
            count -= 1

        print "Stage Two Ended."

        cruise()

    elif case == 2: # Object on the Left side.

        while switch:
            switch = rightOne()
            count += 1

        cruise()
        
        print "Stage One end. Moving to Stage 2"
        
        switch = True

        while switch and count !=0:
            switch = rightTwo()
            count -= 1

        print "Stage Two end. Moving Straight"

        cruise()

    #else:

# //----------------------------------------------------------------------------------
def main():

    while(not checkObstacle() and not l_checkObstacle() and not r_checkObstacle): # while there is no obsticle in front, move forward
        move(0.8,0)
    stop()

    print "Initial Obsticle Detected. Running Left & Right Check"

    leftRotate()
    bolLeft = l_checkObstacle()

    rightRotate()
    rightRotate()
    bolRight = r_checkObstacle()

    leftRotate()

    print "Left Right check ended."

    if bolRight == False and bolLeft == False:
        Straight()
    elif bolRight:
        Diag(1)
    elif bolLeft:
        Diag(2)


# //-----------------------------------------------------------------------------------

main() # The start of the program.


