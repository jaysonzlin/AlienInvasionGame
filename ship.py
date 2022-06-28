import pygame, time
from pygame.sprite import Sprite

class Ship(Sprite):
	'''A class to manage the ship'''
	
	def __init__(self, ai_game, sprite_num):
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
		self.sprites.append(pygame.image.load('images/OGshippng.png'))
		self.sprites.append(pygame.image.load('images/shipfire.png'))		
		self.sprites.append(pygame.image.load('images/shipglow.png'))
		self.sprites.append(pygame.image.load('images/shipblue.png'))
		
		self.current_sprite = sprite_num
		self.start_sprite = 0
		self.image = self.sprites[self.current_sprite]
		self.image = pygame.transform.scale(self.image,(self.width,self.height))
		self.rect = self.image.get_rect()
		
		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		
		#Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		
	def update(self):
		'''Update the ship's position based on the movement flag.'''
		
		#Stops updating if ship is dead
		if self.dead_check:
			return
		
		#Updates position and sprite every 0.5 milliseconds
		if (time.time() - self.current) > 0.0005:
			
			#Update the ship's x value, not the rect
			if self.moving_right and self.rect.right < self.screen_rect.right:
				self.x += self.settings.ship_speed
			
			if self.moving_left and self.rect.left > 0:
				self.x -= self.settings.ship_speed
			
			if self.settings.shipfrm:
				if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
					self.y += self.settings.ship_speed
				if self.moving_up and self.rect.top > self.screen_rect.top:
					self.y -= self.settings.ship_speed
			
			#Update rect object from self.x
			self.rect.x = self.x
			self.rect.y = self.y
		
			#Animates the ship
			self.current_sprite += 0.008
			
			if self.settings.ship_type == 0:
				self.current_sprite = 0
			elif self.settings.ship_type == 1:
				self.current_sprite = 1
			elif self.settings.ship_type == 2:
				self.start_sprite = 2
		
			if self.current_sprite >= len(self.sprites):
				self.current_sprite = self.start_sprite
			
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
		self.y = float(self.rect.y)
	
	def bottom_out(self):
		'''Sends ship to the bottom of the screen'''
		self.rect.bottom = self.screen_rect.bottom
		self.y = float(self.rect.y)
