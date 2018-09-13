'''
Author: Fanchen Bao
Date: 02/10/2018

Description: 
Driver file
Player moves the basket around to catch falling balls
'''

import pygame
from pygame.sprite import Group
from settings import Settings
from ball import Ball
from basket import Basket
from game_stats import GameStats
import game_function as gf

def run_game():
	''' initialize game and create a screen'''
	pygame.init()
	# create a screen whose size is determined in settings.
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Catch Ball")

	# create an instance to store game stats
	stats = GameStats(ai_settings)

	# create a group of balls
	balls = Group()
	gf.create_ball(balls, screen, ai_settings)
	# create one basket
	basket = Basket(screen, ai_settings)

	while True:
		gf.check_events(basket)
		if stats.game_active:
			basket.update()
			gf.update_balls(balls, basket, screen, ai_settings, stats)
		gf.update_screen(screen, basket, ai_settings, balls)

run_game()