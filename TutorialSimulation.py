'''
This code is a tutorial from Tech With Tim Youtube video. 
I am using this as a tool to learn how to create a simulation on python.
Link: https://youtu.be/tLsi2DeUsak?si=3L6Gr99fIYWZ2VpJ

This tutorial is to learn how to launch a ball around to destory some stuff.
'''

# For this code to work I had to install pymonk which handles all the physics and simulations stuff
# as well as pygame which handles all the graphics.

import pygame
import pymunk
import pymunk.pygame_util # this sets pymunk up to use pygame to draw. 
import math

# initialize pygame. First will draw all of the simulation graphics.
pygame.init()

width, height = 800, 800

window = pygame.display.set_mode((width, height))
# Gives us pygame window.

# the draw function won't draw unless you manually draw it. So here is the function that does that.

def draw(space, window, draw_options):
	# clear the window by filling the entire screen with a color of your choice.
	window.fill("white")
	space.debug_draw(draw_options)
	pygame.display.update()
	# without this it won't show up on the screen.

# Let's create a boundary. So objects don't fall through

def create_boundaries(space, width, height):
	# create a list rectangles. In this list we will define how each of our rectangles will look
	# later use for loop to loop through all of them
	rects = [
		[(width/2, height - 10), (width, 20)],
		# this will cause the lower boundaries center to be 400 and 790. The width will be the entire box
		# and the height will be 20.

		[(width/2, 10), (width, 20)],
		# this will be the ceiling or upper boundary. Center will be 400 and 10. The width and height is
		# the same as lower boundary.

		[(10, height/2), (20, height)],
		# this is for the wall on the left side. Center will be 10 and 400. The width will be 20 and height
		# is the height of the window.

		[(width - 10, height/2), (20, height)],
		# this is for the right wall. Center is 790 and 400. The width is the same as the previous one.
	]
	# for rectangle in pymonk you need x and y position of the center of the rectangle and then you need
	# the width and the height.

	for pos, size in rects:
		# draw all the rectangles in rects

		body = pymunk.Body(body_type = pymunk.Body.STATIC)
		# this will create a static body.

		body.position = pos
		# applies position. I am assuming it applies position however we deiced early on
		# he didn't specify what pos does. 
		
		shape = pymunk.Poly.create_box(body, size)
		# creates the shape. Create box will take in the body we want the shape to be attached as well as it's size.

		shape.elasticity = 0.4

		shape.friction = 0.5
		space.add(body, shape)


# Let's create an object

def create_ball(space, radius, mass):
	# in pymunk there is body which is a rigid body like objects 
	# we also have polygon which determines the shape of the body. 
	# In pymunk the image aka the shape is attached to the body but all the physical calculations are done 
	# on the body. 

	body = pymunk.Body()
	# This creates a body	

	body.position = (300, 300)
	# in pymunk (0,0) is the top left hand corner. Middle of the screen will be (width/2, height/2).

	shape = pymunk.Circle(body, radius)
	# assigns a shape to the body.

	shape.mass = mass
	# assignes the default mass that the system has.

	space.color = (255, 0, 0, 100)
	# the color is assinged in RGB alpha. This is when the ball is red.
	# the alpha is the opacity of the object. 100 is fully opaque.

	space.add(body, shape)
	# this will add the object to the simulation
	# You can add the body without adding the shape to the simulation however, adding a shape without body
	# doesn't work because the shape is attached to the body and without body it won't work.

	return shape


# Now set up the main event loop which will display the pygame window.

def run(window, width, height):
	run = True

	# The clock will make so that the game loop will run at a certain speed.
	clock = pygame.time.Clock()
	fps = 60

	dt = 1/fps

	# creating a pymunk space.
	# Space is where we will be putting all of our objects

	space = pymunk.Space()
	# we can draw whatever will be in this space. We have multiple spaces if needed.
	# pymunk will handle how the objects within this space interact. It will apply all the physics needed in this space.

	space.gravity = (0, 981)
	# this assigns gravity in x and y -direction. If we do -9.81 then it is very slow for the simulation
	# the units don't have be real for this simulations. We can pass any values.
	# pymunk is a unit less library, we decide what the units will be.
	# the direction is positive because in pygame as we go down the screen the y increases. We want gravity to pull us down.
	# If this was negative it would work against and push us up.

	ball = create_ball(space, 30, 10)
	# the unit can be whatever you want.

	create_boundaries(space, width, height)

	# Drawing the Simulation.
	# By default pymunk won't draw anything. It does the simulation and allows us to get the information about 
	# different bodies.

	draw_options = pymunk.pygame_util.DrawOptions(window)
	# passing windows is what will draw your simulation on the window you created before.


	# as long as run = true this loop will run.
	while run:
		for event in pygame.event.get():
			# looping through all of the events taht are occurring in pygame.
			# any mouse clicks or movements or keyboard presses also the quit button on the window.
			if event.type == pygame.QUIT:
				# If we press the quit button on the window then we need to stop running the code.
				run = False
				break

		# call the draw function
		draw(space, window, draw_options)

		space.step(dt)
		# how fast should the simulation go.
		# stepping the simulation foward by one over fps so 1/60th of second in this case with every loop.

		clock.tick(fps)
		# This code basically makes it so that the while loop can run a maximum
		# of 60 frames per second. The clock is regulating the speed. 
		# If this line wasn't here than the simulation would depend on processor speed.

	pygame.quit()


# call the function to run.
if __name__ == "__main__":
	run(window, width, height)