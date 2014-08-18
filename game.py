"""
Show how to use a sprite backed by a graphic.
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
Explanation video: http://youtu.be/vRB_983kUMc
"""
import pygame
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
rect_x = 50
rect_y = 50
vel_x = 10
vel_y = 10
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
	screen.fill(BLACK)
	pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
	rect_x += vel_x
	rect_y += vel_y
	# Bounce the rectangle if needed
	if rect_y > 450 or rect_y < 0:
		vel_y = vel_y * -1
	if rect_x > 650 or rect_x < 0:
		vel_x = vel_x * -1

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()
	# --- Limit to 60 frames per second
	clock.tick(60)
	# Close the window and quit.
	# If you forget this line, the program will 'hang'
	# on exit if running from IDLE.
pygame.quit()