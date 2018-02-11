import sys
import pygame


def basket_check_edges(basket):
	''' if baseket hit the edge of screen, it cannot keep moving'''
	if basket.rect.right == basket.screen_rect.right:
		basket.move_right = False
	if basket.rect.left == basket.screen_rect.left:
		basket.move_left == False

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

def update_screen(screen, basket, ai_settings):
	screen.fill(ai_settings.background_color)
	basket.blitme()
	# display the most recent drawing on the screen
	pygame.display.flip()

