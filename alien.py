import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	'''A class to represent a single alien in the fleet.'''
	
	def __init__(self, ai_game):
		'''Initialize the alien and set its starting position.'''
		
		super().__init__()
		self.screen = ai_game.screen
		
		#Load the alien image with animations and set its rect attribute
		self.sprites = []
		self.sprites.append(pygame.image.load('images/invader1.bmp'))
		self.sprites.append(pygame.image.load('images/invader1move.bmp'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(60,43))
		self.rect = self.image.get_rect()
		
		#Start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Store the alien's exact horizontal position
		self.x = float(self.rect.x)
		
	def update(self, speed):
		'''Animates the alien'''
		
		self.current_sprite += speed
		
		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 0
					
		self.image = self.sprites[int(self.current_sprite)]
		self.image = pygame.transform.scale(self.image,(60,43))
		

