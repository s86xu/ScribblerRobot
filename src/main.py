
from myro import *
from basicFunctions import *
initialize("/dev/tty.IPRE6-196107-DevB")

def main():
    
    while True:
        
        if flukeCheck():
            stop()
        #if checkColor()
        #else run O.A. code
        if checkBoundary():
            mv(-1,1.1)
            turnLeft()
            mv(1,0.5)
        else:
            mv_nostop(0.5,0.5)










