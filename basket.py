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
		if self.move_left:
			self.center -= self.ai_settings.basket_speed

		self.rect.centerx = self.center

	def blitme(self):
		'''draw the basket'''
		self.screen.blit(self.image, self.rect)