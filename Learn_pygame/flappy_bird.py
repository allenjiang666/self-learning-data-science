import pygame, sys

def draw_floor():
	#draw the base image on the canvas
	screen.blit(floor_surface,(floor_x_pos,700))
	#draw the base image on the canvas
	screen.blit(floor_surface,(floor_x_pos+576,700))

def create_pipe():
	new_pipe = pipe_surface.get_rect(midtop=(288,512))
	return new_pipe


def move_pipes(pipes):
	'''move all the pipes to the left '''
	for pipe in pipes:
		pipe.centerx -= 5
		return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		screen.blit(pipe_surface, pipe)

pygame.init()
# This is a canvas 
screen = pygame.display.set_mode((576,1024))
# Clock object help to control frame rate
clock = pygame.time.Clock()

# Game Variables
gravity = 0.25 #not the real g, 
bird_movement = 0 # vertical displacement

# load image from relative path
bg_surface = pygame.image.load('sprites/background-day.png')
# convert help to convert image to a better format for pygame to work
bg_surface = bg_surface.convert()
#Double the size of the image
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0

bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
#put a rectangle around the surface
bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
pipe_list.append(create_pipe())
SPAWNPIPE = pygame.USEREVENT
# set a timer for the spawn pipe
pygame.time.set_timer(SPAWNPIPE, 1200)

while True: 
	# even is any time of operation from keybord or mouth click
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#Close the pygame module
			pygame.quit()
			#Close the python stript
			sys.exit()
		# if press a key
		if event.type == pygame.KEYDOWN:
			# the key is a space key
			if event.key == pygame.K_SPACE:
				# stop the bird movement when press key
				bird_movement = 0
				# move the bird up by 12 pixles
				bird_movement -= 12
		if event.type == SPAWNPIPE:
			pipe_list.append(create_pipe())
			

	# Bird
	bird_movement += gravity
	bird_rect.centery += 2
	#draw the background image on the canvas
	screen.blit(bg_surface,(0,0))
	# Put the bird surface , and rectange on the canvas
	screen.blit(bird_surface, bird_rect)

	#Pipes
	print(pipe_list)
	pipe_list = move_pipes(pipe_list)
	print(pipe_list)
	draw_pipes(pipe_list)
	



	# Floor
	# graduately increase the floor image x positon to the right
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -576:
		floor_x_pos =0
	pygame.display.update()
	# frame rate of the game, numbers of cycle in 1s
	clock.tick((30))
	













