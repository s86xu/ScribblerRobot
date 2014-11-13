"""
Show how to use a sprite backed by a graphic.
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
Explanation video: http://youtu.be/vRB_983kUMc
"""
from myro import*
initialize("COM3")
from pygame import*
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
pygame.init()
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
# --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            # --- Game logic should go here
            # --- Drawing code should go here
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                stop()
            if event.key == pygame.K_UP:
                stop()
            if event.key == pygame.K_LEFT:
                stop()
            if event.key == pygame.K_RIGHT:
                stop()
    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
        move(-1,0)

    if keys[K_UP]:
        move(1,0)
    
    if keys[K_LEFT]:
        move(0,1)

    if keys[K_RIGHT]:
        move(0,-1)

    screen.fill(WHITE)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
