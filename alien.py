import pygame, time
from pygame.sprite import Sprite

class Alien(Sprite):
	'''A class to represent a single alien in the fleet.'''
	
	def __init__(self, ai_game):
		'''Initialize the alien and set its starting position.'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.ship = ai_game.ship
		self.game = ai_game
		
		#Hits needed to kill alien
		self.lives = 1
		
		#Creates a timer for each alien sprite
		self.clock = pygame.time.Clock()
		self.sprite_time = time.time()
	
	def check_edges(self):
		'''Return True if alien is at edge of screen'''
		
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
			
	def check_fleet(self):
		'''DEBUG: Fleet check implementation to combat the bug involving multiple declarations of _change_fleet_direction
		before check_edges returns False, resulting in excess downward movement'''
		
		screen_rect = self.screen.get_rect()
		if self.settings.fleet_direction == -1 and self.rect.left <= 10.0:
			return True
		if self.settings.fleet_direction == 1 and self.rect.right >= (screen_rect.width - 10):
			return True
	
	def update(self):
		'''Moves and animates the alien'''
			
		#Alien movement
		self.x += self.settings.alien_speed * self.settings.fleet_direction
		self.rect.x = self.x
		self.current = time.time()
		
		#Alien sprite updates every 350 milliseconds
		if (time.time() - self.sprite_time) > 0.35:
			self.current_sprite += 1
			self.sprite_time = time.time()

		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 0
					
		self.image = self.sprites[int(self.current_sprite)]
		self.image = pygame.transform.scale(self.image,(self.width, self.height))
		
#Work in progress to make three different alien classes		
class invader1(Alien):
	
	def __init__(self, ai_game):
		'''Initializes an instance of invader1'''
		
		super().__init__(ai_game)
		
		#Invader size
		self.width = 60
		self.height = 43
		
		#Points this invader is worth
		self.points = 20 + ai_game.stats.rd * 10
		
		#Load the alien image with animations and set its rect attribute
		self.sprites = []
		self.sprites.append(pygame.image.load('images/invader1.png'))
		self.sprites.append(pygame.image.load('images/invader1move.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		
		#Store the alien's exact horizontal position
		self.x = float(self.rect.x)
		
class invader2(Alien):
	
	def __init__(self, ai_game):
		'''Initializes an instance of invader2'''
		
		super().__init__(ai_game)
		
		#Invader size
		self.width = 43
		self.height = 43
		
		#Points this invader is worth
		self.points = 30 + ai_game.stats.rd * 10
		
		#Load the alien image with animations and set its rect attribute
		self.sprites = []
		self.sprites.append(pygame.image.load('images/invader2.png'))
		self.sprites.append(pygame.image.load('images/invader2move.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		
		#Store the alien's exact horizontal position
		self.x = float(self.rect.x)
		
class invader3(Alien):
	
	def __init__(self, ai_game):
		'''Initializes an instance of invader3'''
		
		super().__init__(ai_game)
		
		#Invader size
		self.width = 50
		self.height = 50
		
		#Points this invader is worth
		self.points = 40 + ai_game.stats.rd * 10
		
		#Load the alien image with animations and set its rect attribute
		self.sprites = []
		self.sprites.append(pygame.image.load('images/invader3.png'))
		self.sprites.append(pygame.image.load('images/invader3move.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		
		#Store the alien's exact horizontal position
		self.x = float(self.rect.x)
