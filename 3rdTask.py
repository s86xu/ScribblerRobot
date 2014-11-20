from myro import *
from basicFunctions import *
from colorDetTest import *
initialize("COM3")#or COM3
from pygame import*



while True:
    colorWantedDetected = raw_input("Should I find 'red','blue',or 'green'?: ")
    if colorWantedDetected == "red" or colorWantedDetected == "green" or colorWantedDetected == "blue":
        break
    else:
        print("sorry what?")


BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
RED = ( 255, 0, 0)
pygame.init()

screenWidth = 700
screenHeight = 500
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HideAndSeek Control Window")

done = False

clock = pygame.time.Clock()

#INITIALIZE IMPORTANT VARIABLES
gridWidth = screenWidth-100
gridHeight = screenHeight-100
gridRobotControlSpeed = 5
gridRobotCruiseSpeed = 2
turnCount = 0
inColorDetection = False

#FUNCTIONS
def drawGrid():
    pygame.draw.rect(screen, BLACK, [50,50,gridWidth,gridHeight],25)

#CLASSES
class Obstacle(pygame.sprite.Sprite):
    #color must be in capital letters and that color must be initialized at the top of this file
    def __init__(self,x,y,width,height,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.set_colorkey(BLACK)
        
class GridRobotPixel(pygame.sprite.Sprite):
    #color must be in capital letters and that color must be initialized at the top of this file
    def __init__(self,x,y,width,height,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.set_colorkey(BLACK)
        self.gridDirectionList = ["U","R","D","L"] #1 is heading up or down, 0 left right
        self.gridDirectionFacing = 0#direction facing 0up,1right,2down,3left RELATIVE to starting direction
    def updateColor(self,color):
        self.image.fill(color)
    def updatePos(self,keyPress,speed=8):
        if keyPress == "up":
            if self.gridDirectionFacing == 1:
                self.rect.x += speed
            if self.gridDirectionFacing == 3:
                self.rect.x -= speed
            if self.gridDirectionFacing == 0:
                self.rect.y -= speed
            if self.gridDirectionFacing == 2:
                self.rect.y += speed
        else: #if keyPress==down
            if self.gridDirectionFacing == 1:
                self.rect.x -= speed
            if self.gridDirectionFacing == 3:
                self.rect.x += speed
            if self.gridDirectionFacing == 0:
                self.rect.y += speed
            if self.gridDirectionFacing == 2:
                self.rect.y -= speed


    
#INITIALIZE CLASS VARIABLES
gridRobot = GridRobotPixel(gridWidth,gridHeight,10,10,GREEN)
allSprites = pygame.sprite.Group()
allSprites.add(gridRobot)
# -------- MAIN -----------
while not done:
# --- Main event loop
#TO REDUCE LAG, HAVE IF STATEMENTS AROUND BLOCKS OF ROBOT CONTROL CODE
    for event in pygame.event.get(): # Event
        if event.type == pygame.QUIT: # If close window
            done = True
            
        #---------------USER HELP-----------------
        if event.type == pygame.KEYUP and inColorDetection == False: 
            if event.key == pygame.K_DOWN:#IF IN HELP
                stop()
                #gridRobot.updateColor(GREEN)#IF IN HELP
            if event.key == pygame.K_UP:
                stop()
            if event.key == pygame.K_LEFT:#IF IN HELP
                stop()
            if event.key == pygame.K_RIGHT:#IF IN HELP
                stop()
            if event.key == pygame.K_z:#IF DETECTS BOX, FIND COLOR, THEN DRAW
                box = Obstacle(gridRobot.rect.x-30,gridRobot.rect.y-100,50,50,RED)
                allSprites.add(box)
        if event.type == pygame.KEYDOWN and inColorDetection == False:
            if event.key == pygame.K_w:
                gridRobot.gridDirectionFacing = 0
                #print("facing forward")
            elif event.key == pygame.K_d:
                gridRobot.gridDirectionFacing = 1
                #print("facing right")
            elif event.key == pygame.K_s:
                gridRobot.gridDirectionFacing = 2
                #print("facing down")
            elif event.key == pygame.K_a:
                gridRobot.gridDirectionFacing = 3
                #print("facing left")
            elif event.key == pygame.K_SPACE:
                print ("detecting...")
                colorDetected = findIfRGB()
                if colorDetected == colorWantedDetected:
                    print("color found!")
                    beep(1.5,800)
                    stop()
                    wait(0.2)
                    beep(1.5,800)
                    break
                else:
                    print("sorry, I don't think that's the color.")
                    
                    
            

    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:#IF IN HELP
        move(-1,0)
        gridRobot.updatePos("down")
    if keys[K_UP]:#IF IN HELP
        move(1,0)
        gridRobot.updatePos("up")
    if keys[K_LEFT]:#ALWAYS ALLOWED FOR MINOR ADJUSTMENTS DURING RUN
        move(0,1)
    if keys[K_RIGHT]:#ALWAYS ALLOWED FOR MINOR ADJUSTMENTS DURING RUN
        move(0,-1)

        
        
    
    #-------------CONSTANT DRAWINGS-----------------
    screen.fill(WHITE)
    drawGrid()
    allSprites.draw(screen)#WE NEED TO CALL THIS IMMEDIATELY AFTER EVERY
    #AFTER EVERY INCREMENT AND MOVEMENT TO HAVE CLOSETOSMOOTH UPDATE ON MAP
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()#WE NEED TO CALL THIS ALSO AFTER EVERY INCREMENT

    #-------------MOVEMENT---------------

    # --- Limit to 60 frames per second
    clock.tick(30)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
