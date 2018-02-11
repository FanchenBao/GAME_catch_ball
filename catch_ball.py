import pygame
from pygame.sprite import Group
from settings import Settings
#from ball import Ball
from basket import Basket
import game_function as gf

def run_game():
	''' initialize game and create a screen'''
	pygame.init()
	# create a screen whose size is determined in settings.
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Catch Ball")

	# create a group of balls
	balls = Group()
	# create one basket
	basket = Basket(screen, ai_settings)

	while True:
		gf.check_events(basket)
		basket.update()
		#gf.update_balls()
		gf.update_screen(screen, basket, ai_settings)

run_game()