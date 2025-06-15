# This is implementing what "The Coding Train" does in his youtube video
# But instead of Java I will be using python and python modules
# Solely for me to practice with making simulations and
# 	learning the logic behind it
# Youtube Link: https://youtu.be/17WoOqgXsRM?si=AyZLTZed77SL9uLj

# This Module that helps with physics simulations
import pymunk

# This module handles all the graphics
import pygame

# this sets pymunk up to use pygame to draw. 
import pymunk.pygame_util 
import math
import random

# initialize pygame.
pygame.init()

# set the parameters of your working space
width, height = 800, 800

window = pygame.display.set_mode((width, height))
# the window in which the simulation will run

# make sure the background of the window is black
def draw(space, window, draw_options):
	window.fill("black")

	# Draws the simulations
	space.debug_draw(draw_options)
	
	# This updates the display on the window
	pygame.display.update()

# make a star function
Class Star:
	def __init__(width, height, ):

		stars = [100]
	
		x = random.randint(-width/2, width/2)
		y = random.randint(-height/2, height/2)
		z = random.randint(0, width)


def run(window, width, height):
	run = True
	
	# Creating the drawing board
	# We will put all the objects in this space
	space = pymunk.Space()
	
	# The clock will make so that the game loop will run at a certain speed.
	clock = pygame.time.Clock()
	fps = 60

	# Every time it loops it moves the simulation forward by
	# 1/60th of seconds
	dt = 1/fps
	
	# Let's you draw whatever you want inside the window
	draw_options = pymunk.pygame_util.DrawOptions(window)

	# The while look will run max of 60 frames per second
	# This loop will run as long as run = True
	while run:
		# Any changes on the simulation window like mouse click,
		# or keyboard presses will be registered
		for event in pygame.event.get():
			# This will make sure we can end the function
			if event.type == pygame.QUIT:
				run = False
				break

		# call the draw function to have everything displayed
		draw(space, window, draw_options)

		# This is what acutally moves the simulation forward
		space.step(dt)
		
		# Makes it so the function runs 60 frames per second.
		clock.tick(fps)

		# This quits pygame
	pygame.quit()



if __name__ == "__main__":
	run(window, width, height)
