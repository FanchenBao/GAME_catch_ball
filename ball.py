'''
Author: Fanchen Bao
Date: 02/10/2018

Description: 
Ball class
'''

import pygame
from pygame.sprite import Sprite
from random import randint

class Ball(Sprite):
	''' a class to mamage all balls'''
	def __init__(self, screen, ai_settings):
		super().__init__()
		# initialize ball and screen
		self.screen = screen
		self.ai_settings = ai_settings
		# load images and get rect
		self.image = pygame.image.load('images/ball.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		# default ball starting position is the top left corner of screen
		self.rect.x = randint(0, (self.screen_rect.right - self.rect.width))
		self.rect.y = 0
		self.y = float(self.rect.y)

		self.ball_speed = self.ai_settings.ball_speed

	def update(self):
		'''ball always goes down'''
		self.y += self.ball_speed
		self.rect.y = self.y

	def reposition(self):
		'''reposition ball to the top of the screen as if to start a new ball'''
		self.y = 0
		self.rect.y =self.y
		self.rect.x = randint(0, (self.screen_rect.right - self.rect.width))

	def blitme(self):
		''' draw the ball'''
		self.screen.blit(self.image, self.rect)
