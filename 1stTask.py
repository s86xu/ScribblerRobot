from myro import *
from basicFunctions import *
from oa import *
from colorDetTest import *


initialize("COM3")
#setIRPower(130)

while True:
    colorWantedDetected = raw_input("Should I find 'red','blue',or 'green'?: ")
    if colorWantedDetected == "red" or colorWantedDetected == "green" or colorWantedDetected == "blue":
        break
    else:
        print("sorry what?")



def joshTurnLeft():
    rotate(0.4)
    wait(1.75)
    stop()
def joshTurnRight():
    rotate(-0.4)
    wait(1.75)
    stop()





done = False



sped = 0.75
turnCount = 0
inHelp = False
inOA = False
inColorDetection = False
inLawnMowing = True
wholeMapTravelled = False
colorFound = False
success = False
firstPhase = 0
firstQuestion = False
inQuestioning = False
answer = ""

#FUNCTIONS


#CLASSES



    
#INITIALIZE CLASS VARIABLES




# -------- MAIN -----------
while not done:



    #COMMIT THE MOUSE EVENT

    
        
    #used to be here


    #DETECTIONS
    #if object detected->lawnmowing=false,, stop, color detection = true
    #

    #-------------MOVEMENT---------------
    #gridRobot.gridDirectionFacing = 0,1,2,3
    #gridRobot.updatePos("up"/"down")
    if inLawnMowing:
        if checkBoundary():
            mv(-1,1.1)
            
            if (turnCount % 2 == 0):
                #turnLeft()
                joshTurnLeft()
                

                mv(1,1.3)
               
                if checkBoundary():
                    stop()
                    beep(1.5,800)
                    #break

                else:
                    joshTurnLeft()
                   

            else:
                joshTurnRight()
               
                

                mv(1,1.3)
                
                if checkBoundary():
                    stop()
                    beep(1.5,800)
                    break
                else:
                    joshTurnRight()
                    


            turnCount+=1
        else:
            mv_nostop(sped,0.3)



                #if not inHelp and not wholeMapTravelled:
        #------------COLOR DETECTION------------
        #if object detected and not inobjectavoidance
        if flukeCheck(500) and not inOA and not inHelp:

            inLawnMowing = False
            stop()
            firstQuestion = True
            #inColorDetection = True
            # sped = 0.5
        while firstQuestion:
            stop()
            answer = raw_input("Am I close enough? (yes/no/dne): ")
            if answer == "yes":
                inColorDetection = True
                firstQuestion = False
                break
            elif answer =="no":
                mv(1,0.5)
            elif answer == "dne":
                inLawnMowing = True
                firstQuestion = False
                break
        #if incolordet->execute color detection
        if inColorDetection and not inHelp:
            result = findIfRGB()
            
            if result == colorWantedDetected:
                stop()
                beep(1,800)
                wait(0.2)
                beep(1,800)
                success = True
                colorFound = True
                break
            elif result != colorWantedDetected:
                inColorDetection = False
                inOA = True
            inColorDetection = False
            #identify the color and do the following to add it to the map->
                #need seperate if statements for red blue green
                #box = Obstacle(gridRobot.rect.x-30,gridRobot.rect.y-100,50,50,COLOR)
                #allSprites.add(box)
            #if color is the one we're looking for, stop, beep, done break whatever
            #if not the color->colordetection = false,objectavoidance=true

        #------------OBJECT AVOIDANCE----------     
        #if inobjectavoidance->execute object avoidance
        if inOA:
            #execute objectAvoidance
            #once done->objectavoidance=false,colordet=false,lawnmowing=true

            objectAvoid()
            inOA = False
            inColorDetection = False
            inLawnMowing = True


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.

