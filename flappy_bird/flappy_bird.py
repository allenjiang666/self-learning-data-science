import pygame
import neat 
import time
import os 
import random

WIN_WIDTH = 500
WIN_HEIGHT = 800 

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
			pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
			pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))]
PIP_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))


class Bird:
	IMGS = BIRD_IMGS
	MAX_ROTATION = 25
	ROT_VEL = 20
	ANIMATION_TIME = 5 

	def __init__(self,x, y):
		# represent start position of the bird
		self.x =x
		self.y = y
		# how much the image is tilting
		self.tilt = 0
		# Basically is t  
		self.tick_count = 0
		# bird is not moving at starting postition
		self.vel = 0
		# seems like the staring position
		self.height = self.y
		self.img_count = 0
		self.img = self.IMGS[0]

	def jump(self):
		'''Bird jump upward'''
		# pygame the origin is at the top left coner. moving down is positive vellcity, moving right is postive volicity
		self.vel = -10.5
		self.tick_count = 0
		self.height = self.y

	def move(self):
		# a tick happened, a frame went by
		self.tick_count +=1

		# d stands for displacement
		# d = v_0t + 1/2at^2, so a = 1
		d = self.vel*self.tick_count + 1.5 *self.tick_count **2

		# when moving down, stop at pixle 16.
		if d>=16:
			d = 16

		# when moving up, fine tuning its position
		if d <0:
			d -=2

		# reset y position to the current postion
		self.y = self.y + d

		if d < 0 or self.y < self.height +50:
			if self.tilt < self.MAX_ROTATION:
				self.tilt = self.MAX_ROTATION
		else:
			if self.tilt > -90:
				self.tilt -=self.ROT_VEL
  
	def draw(self, win):
		self.img_count += 1

		# bird is flappying its wings at different frame period
		if self.img_count < self.ANIMATION_TIME:
			self.img = self.IMGS[0]
		elif self.img_count < self.ANIMATION_TIME*2:
			self.img = self.IMGS[1]
		elif self.img_count < self.ANIMATION_TIME*3:
			self.img = self.IMGS[2]
		elif self.img_count < self.ANIMATION_TIME*4:
			self.img = self.IMGS[1]
		elif self.img_count == self.ANIMATION_TIME*4 + 1:
			self.img = self.IMGS[0]
			self.img_count = 0

		# if the bird is going down, it reset to the fat wing
		if self.tilt <= -80:
			self.img = self.IMGS[1]
			# when jump the bird image is the same when bird at it's original position
			self.img_count = self.ANIMATION_TIME*2

		rotated_image = pygame.transform.rotate(self.img, self.tilt)
		new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x,self.y)).center)
		win.blit(rotated_image, new_rect.topleft)

	def get_mask(self):
		return pygame.mask.from_surface(self.img)

def draw_window(win, bird):
	win.blit(BG_IMG,(0,0))
	bird.draw(win)
	pygame.display.update()

def main():
	bird = Bird(200,200)
	win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
	clock = pygame.time.Clock()

	run = True
	while run:
		clock.tick(100)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		# bird.move()
		draw_window(win,bird)

	pygame.quit()
	quit()

main()












