
#Josh's "Lawnmower Algorithm"; Allows the robot to systematically maneuver through the course
from myro import *
from basicFunctions import *
initialize("/dev/tty.IPRE6-196107-DevB")

def main():
    #TurnCount dictates the direction of rotation
    #Even values (incl. 0) = Left rotation; Odd values = Right rotation
    #Default to left turn
    turnCount = 0
    while True:
        
        if checkBoundary():
            mv(-1,1.1)
            if (turnCount % 2 == 0):
                turnLeft()
                mv(1,0.5)
                if checkBoundary():
                    stop()
                    beep(1.5,800)
                    break
                else:
                    turnLeft()
            else:
                turnRight()
                mv(1,0.5)
                if checkBoundary():
                    stop()
                    beep(1.5,800)
                    break
                else:
                    turnRight()

            turnCount+=1
        else:
            mv_nostop(0.5,0.5)


main()







