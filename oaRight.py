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
    v = 500  # 850 for Straight()
    if L > v and C > v and R > v-300:
        return True
    else:
        return False

def Right():
    print "Right Running"
    rightRotate()
    cruisep(1,3)
    leftRotate()
    cruisep(1,4)
    leftRotate()
    cruisep(1,3)
    rightRotate()
    cruisep(1,3)

# //----------------------------------------------------------------------------------
def main():

    while(not checkObstacle()): # while there is no obsticle in front, move forward
        move(0.8,0)
    stop()

    print "Initial Obsticle Detected."

    Right()

# //-----------------------------------------------------------------------------------

senses()
main() # The start of the program.


