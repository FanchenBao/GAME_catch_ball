class GameStats():
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

	def reset_stats(self):
		self.balls_left = self.ai_settings.balls_allowed