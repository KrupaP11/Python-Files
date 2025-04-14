'''
This code is a tutorial from Tech With Tim Youtube video. 
I am using this as a tool to learn how to create a simulation on python.
Link: https://youtu.be/tLsi2DeUsak?si=3L6Gr99fIYWZ2VpJ

This tutorial is to learn how to launch a ball around to destory some stuff.
'''
'''
Note as of 04/14/25 this code works exactly how the youtube video shows it
I still don't fully understand some of the operations.
In the future I am going to move the pendulum around and create different tables just to get used to the space.
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

def calculate_distance(p1, p2):
	return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)
	# gives us distance between the two points.

def calculate_angle(p1, p2):
	return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

def draw(space, window, draw_options, line):
	# clear the window by filling the entire screen with a color of your choice.
	window.fill("white")

	if line:
		pygame.draw.line(window, "black", line[0], line[1], 3)
		# this creates the line on the window. With black color and the line[1] and line[0]
		# are the position of the lines where as 3 is the thickness of the line.

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
		# adds an element of bouncy

		shape.friction = 0.5
		# adds an element of friction
		space.add(body, shape)

# this function creates a structure using rectangles. These numbers are given by Tim in his video
def create_structure(space, width, height):
	BROWN = (139, 69, 19, 100)
	rects = [
		[(600, height - 120), (40, 200), BROWN, 100],
		[(700, height - 120), (40, 200), BROWN, 100],
		[(750, height - 240), (340, 40), BROWN, 150]
	]

	for pos, size, color, mass in rects:
		body = pymunk.Body()
		body.position = pos
		shape = pymunk.Poly.create_box(body, size, radius = 2)
		# takes in the body that we want to assign to the shape as well as it's size.
		# radius will add a small boarder to the shape.

		shape.color = color
		shape.mass = mass
		shape.elasticity = 0.4
		shape.friction = 0.4
		space.add(body, shape)


def create_pendulum(space):
	rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
	# this is the rotation axis

	rotation_center_body.position = (400, 200)
	# this assigns position to the rotation axis.

	body = pymunk.Body()
	# this is the body of the pendulm
	body.position = (400, 200)
	# this is the position of it. If it aligns with the rotation axis than you won't
	# have a length

	line = pymunk.Segment(body, (0, 0), (255, 0), 5)
	# this creates a line from the center of the body (0, 0) to (255, 0)
	# these positions are defined relative to the body. 5 is the thickness of the line

	circle = pymunk.Circle(body, 40, (255, 0))
	# this creates a circle with radius of 40 cm. (0, 0) is relative to the body so this puts
	# the circle at the end of the line segment which was defined previously
	
	line.friction = 1
	circle.friction = 1
	line.mass = 8
	circle.mass = 30
	circle.elasticity = 0.95

	rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
	# this assigns a joint to the center. This is with respect to both bodies hence the (0, 0) center

	space.add(circle, line, body, rotation_center_joint)
	# the rotation_center_body isn't here because there is no shape associated with it. It is simply there
	# to be used in respect to joint.

# Let's create an object
def create_ball(space, radius, mass, pos):
	# in pymunk there is body which is a rigid body like objects 
	# we also have polygon which determines the shape of the body. 
	# In pymunk the image aka the shape is attached to the body but all the physical calculations are done 
	# on the body. 

	body = pymunk.Body(body_type = pymunk.Body.STATIC)
	# This creates a body	

	body.position = pos
	# in pymunk (0,0) is the top left hand corner. Middle of the screen will be (width/2, height/2).

	shape = pymunk.Circle(body, radius)
	# assigns a shape to the body.

	shape.mass = mass
	# assignes the default mass that the system has.

	space.color = (0, 0, 255, 100)
	# the color is assinged in RGB alpha. This is when the ball is red.
	# the alpha is the opacity of the object. 100 is fully opaque.

	space.add(body, shape)
	# this will add the object to the simulation
	# You can add the body without adding the shape to the simulation however, adding a shape without body
	# doesn't work because the shape is attached to the body and without body it won't work.

	shape.elasticity = 0.9
	# adds an element of bouncy. Higher than 1 will give you weird results.

	shape.friction = 0.4
	# adds an element of friction
	# higher number gives you more friction.

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

	pressed_pos = None
	ball = None

	# calling all the fuctions that draw the body and shape
	create_boundaries(space, width, height)
	create_structure(space, width, height)
	create_pendulum(space)

	# Drawing the Simulation.
	# By default pymunk won't draw anything. It does the simulation and allows us to get the information about 
	# different bodies.

	draw_options = pymunk.pygame_util.DrawOptions(window)
	# passing windows is what will draw your simulation on the window you created before.


	# as long as run = true this loop will run.
	while run:

		line = None

		if ball and pressed_pos:
			line = [pressed_pos, pygame.mouse.get_pos()]
			# basically if the ball exsits that it will make a like between the position of the mouse 
			# and the pressed position

		for event in pygame.event.get():
			# looping through all of the events taht are occurring in pygame.
			# any mouse clicks or movements or keyboard presses also the quit button on the window.
			if event.type == pygame.QUIT:
				# If we press the quit button on the window then we need to stop running the code.
				run = False
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				# this is basically saying if the input is caused by mouse button then,
				
				if not ball:
					# if there is no ball on the screen than we will create one.
					pressed_pos = pygame.mouse.get_pos()
					ball = create_ball(space, 30, 10, pressed_pos)
					# this will pass the space and then it will pass the pressed_pos as well.
					# this should create the ball at the position where the mouse it

				elif pressed_pos:
					# if there is a ball that exsits then it will apply the force to it

					ball.body.body_type = pymunk.Body.DYNAMIC
					# this will change the body of the ball from Static to dynamic.

					angle = calculate_angle(*line)
					# this will calculate the angle. The *line will break the line into two different elements
					# in the list and pass those as p1 and p2
					# the angle will be given in radians
					
					force = calculate_distance(*line) * 50
					# this calculates the amount of force but taking in the two components of line
					# p1 and p2. Multiplying it by 100 will increase the force.

					fx = math.cos(angle)* force					
					# this is calculating the force in the x-direction. 

					fy = math.sin(angle) * force
					# this is calculating the force in the y-direction.

					ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					# then we apply force. We are applying 10000 Newtons in the x-direction
					# at the center of the body.
					# if there is high amount of velocity there is a chance that between the frames of your
					# ball moving you don't find a collision with an object because it moved too quickly. 
					# the way collisions work is you are checking every frame if the ball is hiting an object.
					pressed_pos = None

				else:
					# if we click again then it will remove the ball from the space
					space.remove(ball, ball.body)
					ball = None
					


		# call the draw function
		draw(space, window, draw_options, line)

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
