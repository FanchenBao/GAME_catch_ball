'''
Author: Fanchen Bao
Date: 02/10/2018

Description: 
Basket class
'''

import pygame

class Basket():
	def __init__(self, screen, ai_settings):
		''' initialize a basket and its starting position'''
		self.screen = screen
		self.ai_settings = ai_settings

		# load image and get rect for image and screen
		self.image = pygame.image.load('images/basket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# set the starting position of the basket at bottom middle of screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		# set x coordinate as float to finely control basket movement
		self.center = float(self.rect.centerx)

		# movement flag for basket
		self.move_right = False
		self.move_left = False


	def update(self):
		''' update basket position based on key press'''
		if self.move_right:
			self.center += self.ai_settings.basket_speed
			# make sure basket does not move outside the scren
			if self.rect.right >= self.screen_rect.right:
				self.center = self.screen_rect.right - self.rect.width / 2
		if self.move_left:
			self.center -= self.ai_settings.basket_speed
			# make sure basket does not move outside the scren
			if self.rect.left <= 0:
				self.center = self.rect.width / 2

		self.rect.centerx = self.center

	def blitme(self):
		'''draw the basket'''
		self.screen.blit(self.image, self.rect)