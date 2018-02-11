class Settings():
	''' store basic game settings'''
	def __init__(self):
		self.screen_height = 700
		self.screen_width = 1050
		self.background_color = (230, 230, 230)

		# ball settings
		self.ball_speed = 3
		self.balls_allowed = 5

		# basket settings
		self.basket_speed = 10