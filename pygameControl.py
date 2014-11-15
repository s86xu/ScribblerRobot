from myro import*
initialize("COM3")#or COM3
#import pygame
from pygame import*

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
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
    def updatePos(self,keyPress,speed=1):
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            #MOUSE POSITION
            mouseposition=pygame.mouse.get_pos()
            gridRobot.rect.x = mouseposition[0]-5
            gridRobot.rect.y = mouseposition[1]-5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                stop()
                gridRobot.updateColor(GREEN)
            if event.key == pygame.K_UP:
                stop()
            if event.key == pygame.K_LEFT:
                stop()
                print("hi")
            if event.key == pygame.K_RIGHT:
                stop()
                print("hi")
            if event.key == pygame.K_z:#IF DETECTS BOX, FIND COLOR, THEN DRAW
                box = Obstacle(gridRobot.rect.x-30,gridRobot.rect.y-100,50,50,RED)
                allSprites.add(box)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                gridRobot.updateColor(RED)
            if event.key == pygame.K_w:
                gridRobot.gridDirectionFacing = 0
                print("facing forward")
            elif event.key == pygame.K_d:
                gridRobot.gridDirectionFacing = 1
                print("facing right")
            elif event.key == pygame.K_s:
                gridRobot.gridDirectionFacing = 2
                print("facing down")
            elif event.key == pygame.K_a:
                gridRobot.gridDirectionFacing = 3
                print("facing left")
    
    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
        move(-1,0)
        gridRobot.updatePos("down")
    if keys[K_UP]:
        move(1,0)
        gridRobot.updatePos("up")
    if keys[K_LEFT]:
        move(0,0.5)
        print("rotating left")
    #gridRobot.updatePos("left",1)
    if keys[K_RIGHT]:
        move(0,-0.5)
        print("rotating right")
    #gridRobot.updatePos("right",1)
    
    #COMMIT THE MOUSE EVENT
    clickposition=event.type==pygame.MOUSEBUTTONDOWN
    
    
    #DRAWINGS
    screen.fill(WHITE)
    drawGrid()
    allSprites.draw(screen)
    #pygame.draw.line(screen, GREEN, [10, 10], [10, 20], 10)#if rect doesn't work
    #pygame.draw.rect(screen, GREEN, [robotPos[0],robotPos[1],10,10],0)
    
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
