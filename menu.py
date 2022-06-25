import pygame

from settings import Settings

class Menu:
	'''Main Menu'''
	
	def __init__(self, ai_game):
		'''Initialize main menu'''
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		
		#Set the dimensions and properties of the button
		self.button_width, self.button_height = 159.5, 53
		
		#Game Title
		self.logo_width, self.logo_height = 500, 500
		self.logo = pygame.image.load('images/logo2.png')
		self.play_button = pygame.transform.scale(self.logo,(self.logo_width,self.logo_height))
		
		self.logo_rect = self.logo.get_rect()
		self.logo_rect.center = self.screen_rect.center
		self.logo_rect.top = 20
		
		#Play button
		self.play_button = pygame.image.load('images/play.png')
		self.play_button = pygame.transform.scale(self.play_button,(self.button_width,self.button_height))
		#Play button rect
		self.play_rect = self.play_button.get_rect()
		self.play_rect.center = self.screen_rect.center
		self.play_rect.bottom = self.screen_rect.bottom - 150
		
		#How-to-Play button
		self.htp_button = pygame.image.load('images/how_to_play.png')
		self.htp_button = pygame.transform.scale(self.htp_button,(self.button_width,self.button_height))
		#HTP button rect
		self.htp_rect = self.htp_button.get_rect()
		self.htp_rect.left = self.screen_rect.left + 150
		self.htp_rect.bottom = self.screen_rect.bottom - 150
		
		#Credits Button
		self.credits_button = pygame.image.load('images/credits.png')
		self.credits_button = pygame.transform.scale(self.credits_button, (self.button_width, self.button_height))
		#Credits button rect
		self.credits_rect = self.credits_button.get_rect()
		self.credits_rect.right = self.screen_rect.right - 150
		self.credits_rect.bottom = self.screen_rect.bottom - 150
		
	def draw_buttons(self):
		
		self.screen.fill(self.settings.bg_color, self.screen_rect)
		self.screen.blit(self.play_button, self.play_rect)
		self.screen.blit(self.htp_button, self.htp_rect)
		self.screen.blit(self.credits_button, self.credits_rect)
		self.screen.blit(self.logo, self.logo_rect)
