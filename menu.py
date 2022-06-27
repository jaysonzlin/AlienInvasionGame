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
		self.logo_rect.top = self.screen_rect.top + 20
		
		#Play button
		self.play_button = pygame.image.load('images/play.png')
		self.play_button = pygame.transform.scale(self.play_button,(self.button_width,self.button_height))
		#Play button rect
		self.play_rect = self.play_button.get_rect()
		self.play_rect.center = self.screen_rect.center
		self.play_rect.bottom = self.screen_rect.bottom - 150
		
##########################################################################################################################		
		#How-to-Play button
		self.htp_button = pygame.image.load('images/how_to_play.png')
		self.htp_button = pygame.transform.scale(self.htp_button,(self.button_width,self.button_height))
		#HTP button rect
		self.htp_rect = self.htp_button.get_rect()
		self.htp_rect.left = self.screen_rect.left + 150
		self.htp_rect.bottom = self.screen_rect.bottom - 150
		
		#First info box
		self.arrow = pygame.image.load('images/arrow.png')
		self.arrow = pygame.transform.scale(self.arrow,(250,250))
		#First box rect
		self.arrow_rect = self.arrow.get_rect()
		self.arrow_rect.left = self.screen_rect.left + 200
		self.arrow_rect.top = self.screen_rect.top + 100
		
		#Second info box
		self.space = pygame.image.load('images/space.png')
		self.space = pygame.transform.scale(self.space,(250,250))
		#Second box rect
		self.space_rect = self.space.get_rect()
		self.space_rect.right = self.screen_rect.right - 200
		self.space_rect.top = self.screen_rect.top + 100
		
		#Third info box
		self.pu = pygame.image.load('images/powerup.png')
		self.pu = pygame.transform.scale(self.pu,(250,250))
		#Third box rect
		self.pu_rect = self.pu.get_rect()
		self.pu_rect.left = self.screen_rect.left + 200
		self.pu_rect.bottom = self.screen_rect.bottom - 100
		
		#Fourth info box
		self.annihilate = pygame.image.load('images/annihilate.png')
		self.annihilate = pygame.transform.scale(self.annihilate,(250,250))
		#Fourth box rect
		self.annihilate_rect = self.annihilate.get_rect()
		self.annihilate_rect.right = self.screen_rect.right - 200
		self.annihilate_rect.bottom = self.screen_rect.bottom - 100
		
##########################################################################################################################	
		
		#Credits Button
		self.credits_button = pygame.image.load('images/credits.png')
		self.credits_button = pygame.transform.scale(self.credits_button, (self.button_width, self.button_height))
		#Credits button rect
		self.credits_rect = self.credits_button.get_rect()
		self.credits_rect.right = self.screen_rect.right - 150
		self.credits_rect.bottom = self.screen_rect.bottom - 150
		
		#Back Button
		self.back_button = pygame.image.load('images/back.png')
		self.back_button = pygame.transform.scale(self.back_button, (83, 57))
		#Back Button rect
		self.back_rect = self.back_button.get_rect()
		self.back_rect.left = self.screen_rect.left + 20
		self.back_rect.top = self.screen_rect.top + 20
		
		#Power Up - Speed Up
		self.spd_button = pygame.image.load('images/pubg.png')
		self.spd_button = pygame.transform.scale(self.spd_button, (800, 533))
		#Speed Up Rect
		self.spd_rect = self.spd_button.get_rect()
		self.spd_rect.center = self.screen_rect.center
		
		#Checks if How to Play section is active
		self.htp_check = False
		#Checks if Credits section is active
		self.credits_check = False
		#Checks if Power Up menu is active
		self.pu_check = False
		
	def draw_buttons(self):
		
		if not self.htp_check and not self.credits_check and not self.pu_check:
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.play_button, self.play_rect)
			self.screen.blit(self.htp_button, self.htp_rect)
			self.screen.blit(self.credits_button, self.credits_rect)
			self.screen.blit(self.logo, self.logo_rect)
			
		elif self.htp_check:
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.back_button, self.back_rect)
			self.screen.blit(self.space, self.space_rect)
			self.screen.blit(self.arrow, self.arrow_rect)
			self.screen.blit(self.pu, self.pu_rect)
			self.screen.blit(self.annihilate, self.annihilate_rect)
			
		elif self.credits_check:
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.back_button, self.back_rect)
			#placeholder for credits sprite
		
		elif self.pu_check:
			self.screen.blit(self.spd_button, self.spd_rect)
