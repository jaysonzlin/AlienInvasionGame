import pygame

class Morgana:
	'''Test character Morgana; All Rights Reserved by ATLUS'''
	
	def __init__(self, ai_game):
		'''Initialize Morgana and set his starting position.'''
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Loads Morgana and gets his rect
		self.image = pygame.image.load('images/P5R_Morgana.bmp')
		self.image = pygame.transform.scale(self.image,(258.5,317))
		self.rect = self.image.get_rect()
		
		#Starts Morgana at the center of the screen
		self.rect.center = self.screen_rect.center
		
	def blitme(self):
		'''Draw Morgana at current location.'''
		
		self.screen.blit(self.image, self.rect) 
