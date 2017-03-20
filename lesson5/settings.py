# settings.py

class Settings():
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen settings
		self.screen_width = 600
		self.screen_height = 500
		self.bg_color = (230, 230, 230)

		# Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction of 1 means right; -1 means left
		self.fleet_direction = 1

		# Ship settings
		self.ship_speed_factor = 1.5

		# Bullet settings
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3