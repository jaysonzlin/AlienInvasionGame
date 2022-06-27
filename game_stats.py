import pygame, time

class GameStats:
	'''Track statistics for Alien Invasion'''
	
	def __init__(self, ai_game):
		'''Initialize statistics'''
		
		self.settings = ai_game.settings
		self.ship_lives = self.settings.ship_lives
		self.reset_stats()
		
		#Timing Test
		#Creates a timer for each alien sprite
		self.clock = pygame.time.Clock()
		self.prev_time = time.time()
		
		#Debug: counter prevents aliens from moving until the game is started
		self.time_counter = 0
		
		#Start game in an inactive state.
		self.game_active = False
		
		#High score should never be reset
		self.high_score = 0
		
		#Round number
		self.rd = 1
		
	def reset_stats(self):
		'''Initialize statistics that can change during the game'''
		
		self.settings.ship_lives = 4
		self.score = 0
		self.time_counter = 0
		self.rd = 1
		self.settings.alien_lives = 1
		
	def update(self):
		'''Updates setting values'''
		
		if self.time_counter == 0:
			self.time_counter += 1
			self.prev_time = time.time()
			return
		
		#Caps the alien movement speed
		if self.settings.alien_spd_multi >= 250:
			self.settings.alien_spd_multi = 250
		
		#Delta time to enable frame rate independence for movements
		dt = (time.time()  - self.prev_time)
		self.settings.alien_speed = self.settings.alien_spd_multi * dt
		self.settings.bullet_speed = self.settings.bullet_multi * dt
		self.settings.ship_speed = self.settings.ship_multi * dt
		self.prev_time = time.time()
