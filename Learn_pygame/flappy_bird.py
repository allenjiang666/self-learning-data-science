import pygame, sys, random

def draw_floor():
	#draw the base image on the canvas
	screen.blit(floor_surface,(floor_x_pos,900))
	#draw the base image on the canvas
	screen.blit(floor_surface,(floor_x_pos+576,900))

def create_pipe():
	random_pipe_pos = random.choice(pipe_height)
	bottom_pipe = pipe_surface.get_rect(midtop=(700,random_pipe_pos))
	top_pipe = pipe_surface.get_rect(midbottom=(700,random_pipe_pos-300))
	return  bottom_pipe, top_pipe


def move_pipes(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return pipes

def draw_pipes(pipes):
	for pipe in pipes:
		# bottom is the attribute of get_rect object
		if pipe.bottom >=1024:
			screen.blit(pipe_surface, pipe)
		else:
			# .flip(surface object, filp on X, flip on Y)
			flip_pipe = pygame.transform.flip(pipe_surface, False,True)
			screen.blit(flip_pipe,pipe)

def check_collision(pipes):
	for pipe in pipes:
		#try not to do collision as possible, it takes alot computational power
		if bird_rect.colliderect(pipe):
			death_sound.play()
			return False

	# check if the bird hit the top or floor
	# pixle messurement is not very precise, so always use < or >
	if bird_rect.top <= -100 or bird_rect.bottom >=900:
		return False

	return True

def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1)
	return new_bird

def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center =(100,bird_rect.centery))
	return new_bird, new_bird_rect

def score_display(game_state): 
	if game_state == 'main_game':
		# the last tuple is RGB value
		# render dosen't like integer as first argument
		score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
		score_rect = score_surface.get_rect(center =(288,100))
		screen.blit(score_surface,score_rect)
	if game_state == 'game_over':
		score_surface = game_font.render(f'Score: {int(score)}', True, (255,255,255))
		score_rect = score_surface.get_rect(center =(288,100))
		screen.blit(score_surface,score_rect)

		high_score_surface = game_font.render(f'High score: {int(score)}', True, (255,255,255))
		high_score_rect = high_score_surface.get_rect(center =(288,850))
		screen.blit(high_score_surface,high_score_rect)

def update_score(score, high_score):
	if score > high_score:
		high_score = score
	return high_score

pygame.mixer.pre_init(frequency = 44100, size =16, channels =1, buffer = 512)
pygame.init()
# This is a canvas 
screen = pygame.display.set_mode((576,1024))
# Clock object help to control frame rate
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF',40)

# Game Variables
gravity = 0.25 #not the real g, 
bird_movement = 0 # vertical displacement
game_active = True
score = 0
high_score = 0

# load image from relative path
bg_surface = pygame.image.load('sprites/background-day.png')
# convert help to convert image to a better format for pygame to work
bg_surface = bg_surface.convert()
#Double the size of the image
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# convert_alpha help to reduce the black box when apply rotation 
bird_downflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-downflap.png').convert_alpha())
bird_midflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-midflap.png').convert_alpha())
bird_upflap = pygame.transform.scale2x(pygame.image.load('sprites/bluebird-upflap.png').convert_alpha())
# put all the surfaces in to a list
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
#put a rectangle around the surface
bird_rect = bird_surface.get_rect(center=(100,512))

# + 1 means it is differnt from last even
BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)


# bird_surface = pygame.image.load('sprites/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# 
# bird_rect = bird_surface.get_rect(center = (100,512))

pipe_surface = pygame.image.load('sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
# set a timer for the spawn pipe
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400,600,800]

game_over_surface = pygame.transform.scale2x(pygame.image.load('sprites/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288,512))

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound =  pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound =  pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown =100
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
			if event.key == pygame.K_SPACE and game_active:
				# stop the bird movement when press key
				bird_movement = 0
				# move the bird up by 12 pixles
				bird_movement -= 12
				#play the win flap sound
				flap_sound.play()
			if event.key == pygame.K_SPACE and game_active == False:
				game_active = True
				pipe_list.clear()
				bird_rect.center = (100,512)
				bird_movement = 0
				score = 0



		if event.type == SPAWNPIPE:
			pipe_list.extend(create_pipe())

		if event.type == BIRDFLAP:
			if bird_index <2:
				bird_index +=1
			else:
				bird_index = 0

			bird_surface,bird_rect = bird_animation()

	#draw the background image on the canvas
	screen.blit(bg_surface,(0,0))
			
	if game_active:
		# Bird
		bird_movement += gravity
		rotated_bird = rotate_bird(bird_surface)
		bird_rect.centery += bird_movement

		# Put the bird surface , and rectange on the canvas
		screen.blit(rotated_bird, bird_rect)
		game_active = check_collision(pipe_list)

		#Pipes
		
		pipe_list = move_pipes(pipe_list)
		draw_pipes(pipe_list)

		score += 0.01
		score_display('main_game')
		score_sound_countdown -= 1
		if score_sound_countdown <= 0:
			score_sound.play()
			score_sound_countdown = 100

	else:
		screen.blit(game_over_surface, game_over_rect)
		high_score = update_score(score,high_score)
		score_display('game_over')
	



	# Floor
	# graduately increase the floor image x positon to the right
	floor_x_pos -= 1
	draw_floor()
	if floor_x_pos <= -576:
		floor_x_pos =0
	pygame.display.update()
	# frame rate of the game, numbers of cycle in 1s
	clock.tick((120))
	













