# Settings

class Settings:
	'''A class to store all settings for Alien Invasion'''
	def __init__(self):
		'''Initialize the game's settings.'''
		
		#Screen settings
		self.screen_width = 1000
		self.screen_height = 750
		self.bg_color = (0,0,0)
		
		#Ship settings
		self.ship_speed = 1.5 
		self.ship_multi = 250.0
		self.ship_multi2 = 700.0
		self.ship_multi3 = 2000
		self.ship_lives = 4
		
		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_multi = 750.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (235,52,52)
		self.bullets_allowed = 99
		self.bullet_power = 1
		self.bullet_firing_speed = 0.25 #machine gun: 0.10 laser:0.005
		self.god_bullet_off = True
		
		#Alien settings
		self.alien_lives = 1
		self.alien_speed = 0.0
		
		self.alien_spd_multi = 60.0 
		self.alien_spd_cap = 250  #Alien speed cap
		
		self.fleet_drop_speed = 20
		
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

