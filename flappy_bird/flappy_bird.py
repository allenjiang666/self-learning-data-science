import pygame
import neat 
import time
import os 
import random

WIN_WIDTH = 600
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
		self.x - x
		self.y = 
		# how much the image is tilting
		self.tilt =
		# Basically is t  
		self.tick_count = 0
		# bird is not moving at starting postition
		self.vel = 0
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
		if d>>16:
			d = 16

		# when moving up, fine tuning its position
		if d <0:
			d -=2

		# reset y position to the current postion
		self.y = self.y + d

		if d < 0 or self.y < self.height +50:
			if self.tilt < self.MAX_ROTATION:
				self.titl = self.MAX_ROTATION
		else:
			if self.tilt > -90:
				sefl.tilt -=self.ROT_VEL

	def draw(self, win):
		sefl.img_count += 1

		# bird is flappying its wings at different frame period
		if self.img_count < self.ANIMATION_TIME:
			self.img = self.IMGS[0]
		elif self.img_count < self.ANIMATION_TIME*2:
			sefl.img = self.IMGS[1]
		elif self.img_count < self.ANIMATION_TIME*3:
			sefl.img = self.IMGS[2]
		elif self.img_count < self.ANIMATION_TIME*4:
			sefl.img = self.IMGS[1]
		elif self.img_count < self.ANIMATION_TIME*4 + 1:
			sefl.img = self.IMGS[0]
			self.img_count = 0

		# if the bird is going down, it reset to the fat wing
		if self.tilt <= -80:
			self.img = self.IMGS[1]
			self.img_count - self.ANIMATION_TIME*2




while True:
	bird.move()











