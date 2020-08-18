import pygame, sys

def draw_floor():
	#draw the base image on the canvas
	screen.blit(floor_surface,(floor_x_pos,700))
	# #draw the base image on the canvas
	# screen.blit(floor_surface,(floor_x_pos+576,700))




pygame.init()
# This is a canvas 
screen = pygame.display.set_mode((576,1024))
# Clock object help to control frame rate
clock = pygame.time.Clock()

# load image from relative path
bg_surface = pygame.image.load('sprites/background-day.png')
# convert help to convert image to a better format for pygame to work
bg_surface = bg_surface.convert()
#Double the size of the image
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)

floor_x_pos = 0

while True: 
	# even is any time of operation from keybord or mouth click
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#Close the pygame module
			pygame.quit()
			#Close the python stript
			sys.exit()
	#draw the background image on the canvas
	screen.blit(bg_surface,(0,0))
	# graduately increase the floor image x positon to the right
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -576:
		floor_x_pos =0
	pygame.display.update()
	# frame rate of the game, numbers of cycle in 1s
	clock.tick((120))
	













