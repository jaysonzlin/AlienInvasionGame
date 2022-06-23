# Settings
import pygame, time

class Settings:
	'''A class to store all settings for Alien Invasion'''
	def __init__(self):
		'''Initialize the game's settings.'''
		
		#Timing Test
		#Creates a timer for each alien sprite
		self.clock = pygame.time.Clock()
		self.current = time.time()
		
		#Screen settings
		self.screen_width = 1000
		self.screen_height = 750
		self.bg_color = (0,0,0)
		
		#Ship settings
		self.ship_speed = 1.5
		self.ship_lives = 3
		
		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (235,52,52)
		self.bullets_allowed = 99
		self.bullet_power = 3
		self.god_bullet_off = True 
		
		#Alien settings
		self.alien_speed = 10.0
		
		self.alien_spd_multi = 60.0 
		self.alien_spd_cap = 250  #Alien speed cap
		
		self.fleet_drop_speed = 20
		
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

	def update(self):
		'''Updates setting values'''
		
		#Caps the alien movement speed
		if self.alien_spd_multi >= 250:
			self.alien_spd_multi = 250
		
		#Delta time to enable frame rate independence for movements
		dt = (time.time() - self.current)
		self.alien_speed = self.alien_spd_multi * dt
		self.current = time.time()
