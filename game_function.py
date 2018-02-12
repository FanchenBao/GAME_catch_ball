import sys
import pygame
from ball import Ball
from time import sleep

def ball_caught(ball, basket):
	'''if center of ball collides within the width of basket, it's a catch'''
	if ball.rect.centerx < basket.rect.right and ball.rect.centerx > basket.rect.left:
		print("Caught!")
	else:
		print("Miss!")

def update_balls(balls, basket, screen, ai_settings, stats):
	''' update current ball location and determine whether ball has been caught or missed'''
	# in order to use spritecollideany, ball has to be in a group
	for ball in balls.sprites():
		# detect ball and basket collision
		if pygame.sprite.spritecollideany(basket, balls):
			# give player a little pause to identify where the collision happens
			sleep(0.2)
			ball_caught(ball, basket)

			# reduce number of balls left and reposition ball if there are still balls left	
			stats.balls_left -= 1
			if stats.balls_left > 0:
				ball.reposition()

		# deal with situation where ball is missed completely and falls through the screen
		if ball.rect.top >= ball.screen_rect.bottom:
			print("Miss!")
			stats.balls_left -= 1
			if stats.balls_left > 0:
				ball.reposition()

		# when no ball is left, give a longer pause and reset stats and restart the game.
		if stats.balls_left == 0:
			print("No ball left!")
			# end game
			stats.game_active = False
			break
		ball.update()

def create_ball(balls, screen, ai_settings):
	# create a ball and put that in the group balls
	ball = Ball(screen, ai_settings)
	balls.add(ball)


def check_key_down_event(event, basket):
	''' check key press event'''
	# press right arrow key
	if event.key == pygame.K_RIGHT:
		basket.move_right = True
	# press left arrow key
	if event.key == pygame.K_LEFT:
		basket.move_left = True
	# press 'Q' to exit game
	if event.key == pygame.K_q:
		sys.exit()

def check_key_up_event(event, basket):
	''' check key release event'''
	# release right arrow key
	if event.key == pygame.K_RIGHT:
		basket.move_right = False
	# press left arrow key
	if event.key == pygame.K_LEFT:
		basket.move_left = False


def check_events(basket):
	'''check key press'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		# check key press or release 
		elif event.type == pygame.KEYDOWN:
			check_key_down_event(event, basket)
		elif event.type == pygame.KEYUP:
			check_key_up_event(event, basket)

def update_screen(screen, basket, ai_settings, balls):
	screen.fill(ai_settings.background_color)
	basket.blitme()
	balls.draw(screen)
	# display the most recent drawing on the screen
	pygame.display.flip()

