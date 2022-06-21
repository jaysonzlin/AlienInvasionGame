import pygame, time
from pygame.sprite import Sprite

class Ship(Sprite):
	'''A class to manage the ship'''
	
	def __init__(self, ai_game):
		'''Initialize the ship and set its starting position.'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		#ship size
		self.width = 50
		self.height = 50
		
		self.dead_check = False
		
		#Creating a timer for the ship's actions
		self.clock = pygame.time.Clock()
		self.current = time.time()
		
		#Load the ship image with its animations and get its rect
		self.sprites = []
		#self.sprites.append(pygame.image.load('images/shipno.bmp'))
		#self.sprites.append(pygame.image.load('images/shipfire.bmp'))		
		#self.sprites.append(pygame.image.load('images/shipglow.bmp'))
		#self.sprites.append(pygame.image.load('images/shipblue.bmp'))
		self.sprites.append(pygame.image.load('images/OGshippng.png'))
		#self.sprites.append(pygame.image.load('images/explosion.png'))
		
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		
		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		
		#Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		'''Update the ship's position based on the movement flag.'''
		
		#Updates position and sprite every 0.5 milliseconds
		if (time.time() - self.current) > 0.0005:
			
			if self.dead_check:
				self.image = pygame.image.load('images/explosion.png')
				self.image = pygame.transform.scale(self.image,(50,50))
				return
			
			#Update the ship's x value, not the rect
			if self.moving_right and self.rect.right < self.screen_rect.right:
				self.x += self.settings.ship_speed
			
			if self.moving_left and self.rect.left > 0:
				self.x -= self.settings.ship_speed
			
			#Update rect object from self.x
			self.rect.x = self.x
		
			#Animates the ship
			self.current_sprite += 0.005
		
			if self.current_sprite >= len(self.sprites):
				self.current_sprite = 0
			
			self.current = time.time()
			
		self.image = self.sprites[int(self.current_sprite)]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
	
	def blitme(self):
		'''Draw the ship at its current location.'''
		
		self.screen.blit(self.image, self.rect) 
		
	def center_ship(self):
		"""Center the ship on the screen."""
		
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
