import pygame, pygame.font
from pygame.sprite import Sprite

from settings import Settings

class Menu(Sprite):
	'''Main Menu'''
	
	def __init__(self, ai_game):
		'''Initialize main menu'''
		
		super().__init__()
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.creds = 0
		self.stats = ai_game.stats
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

##########################################################################################################################
		
		#Back Button
		self.back_button = pygame.image.load('images/back.png')
		self.back_button = pygame.transform.scale(self.back_button, (83, 57))
		#Back Button rect
		self.back_rect = self.back_button.get_rect()
		self.back_rect.left = self.screen_rect.left + 20
		self.back_rect.top = self.screen_rect.top + 20
		
##########################################################################################################################		
		
		#Power Up Menu
		self.pumenu_button = pygame.image.load('images/pubg.png')
		self.pumenu_button = pygame.transform.scale(self.pumenu_button, (800, 533))
		#Power Up Menu Rect
		self.pumenu_rect = self.pumenu_button.get_rect()
		self.pumenu_rect.center = self.screen_rect.center
		
		#Font settings for power-up menu space credits
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('impact', 28)
		
		#Bullet Dmg Upgrade
		self.bdmg_sprites = []
		self.bdmg_sprites.append(pygame.image.load('images/dmgpu/bdmg3000.png'))
		self.bdmg_sprites.append(pygame.image.load('images/dmgpu/bdmg10000.png'))
		self.bdmg_sprites.append(pygame.image.load('images/dmgpu/bdmg50000.png'))
		self.bdmg_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_bdmg = 0
		self.bdmg = self.bdmg_sprites[self.current_bdmg]
		self.bdmg = pygame.transform.scale(self.bdmg,(150,150))
		self.bdmg_rect = self.bdmg.get_rect()
		self.bdmg_rect.left = self.screen_rect.left + 150
		self.bdmg_rect.top = self.screen_rect.top + 180
		
		#Bullet Spd Upgrade
		self.bspd_sprites = []
		self.bspd_sprites.append(pygame.image.load('images/dmgpu/bspd5000.png'))
		self.bspd_sprites.append(pygame.image.load('images/dmgpu/laser.png'))
		self.bspd_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_bspd = 0
		self.bspd = self.bspd_sprites[self.current_bspd]
		self.bspd = pygame.transform.scale(self.bspd,(150,150))
		self.bspd_rect = self.bspd.get_rect()
		self.bspd_rect.left = self.screen_rect.left + 335
		self.bspd_rect.top = self.screen_rect.top + 180
		
		#Triple Shot
		self.ts_sprites = []
		self.ts_sprites.append(pygame.image.load('images/dmgpu/triple.png'))
		self.ts_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_ts = 0
		self.ts = self.ts_sprites[self.current_ts]
		self.ts = pygame.transform.scale(self.ts,(150,150))
		self.ts_rect = self.ts.get_rect()
		self.ts_rect.right = self.screen_rect.right - 335
		self.ts_rect.top = self.screen_rect.top + 180
		
		#Deus Bullets
		self.deus_sprites = []
		self.deus_sprites.append(pygame.image.load('images/dmgpu/deus.png'))
		self.deus_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_deus = 0
		self.deus = self.deus_sprites[self.current_deus]
		self.deus = pygame.transform.scale(self.deus,(150,150))
		self.deus_rect = self.deus.get_rect()
		self.deus_rect.right = self.screen_rect.right - 150
		self.deus_rect.top = self.screen_rect.top + 180
		
		#Ship Spd Upgrade
		self.sspd_sprites = []
		self.sspd_sprites.append(pygame.image.load('images/utilpu/shipspd5000.png'))
		self.sspd_sprites.append(pygame.image.load('images/utilpu/shipspd20000.png'))
		self.sspd_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_sspd = 0
		self.sspd = self.sspd_sprites[self.current_sspd]
		self.sspd = pygame.transform.scale(self.sspd,(150,150))
		self.sspd_rect = self.sspd.get_rect()
		self.sspd_rect.left = self.screen_rect.left + 150
		self.sspd_rect.bottom = self.screen_rect.bottom - 180
		
		#Ship Full Range Movement
		self.sfrm_sprites = []
		self.sfrm_sprites.append(pygame.image.load('images/utilpu/shipfrm.png'))
		self.sfrm_sprites.append(pygame.image.load('images/completed.png'))	
		self.current_sfrm = 0
		self.sfrm = self.sfrm_sprites[self.current_sfrm]
		self.sfrm = pygame.transform.scale(self.sfrm,(150,150))
		self.sfrm_rect = self.sfrm.get_rect()
		self.sfrm_rect.left = self.screen_rect.left + 335
		self.sfrm_rect.bottom = self.screen_rect.bottom - 180
		
		#Bullet Capacity Upgrade
		self.bc_sprites = []
		self.bc_sprites.append(pygame.image.load('images/utilpu/bulletcapa.png'))
		self.bc_sprites.append(pygame.image.load('images/utilpu/unlimited.png'))
		self.bc_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_bc = 0
		self.bc = self.bc_sprites[self.current_bc]
		self.bc = pygame.transform.scale(self.bc,(150,150))
		self.bc_rect = self.bc.get_rect()
		self.bc_rect.right = self.screen_rect.right - 335
		self.bc_rect.bottom = self.screen_rect.bottom - 180
		
		#Extra Life
		self.elife_sprites = []
		self.elife_sprites.append(pygame.image.load('images/utilpu/extralife10000.png'))
		self.elife_sprites.append(pygame.image.load('images/utilpu/extralife30000.png'))
		self.elife_sprites.append(pygame.image.load('images/utilpu/extralife50000.png'))
		self.elife_sprites.append(pygame.image.load('images/completed.png'))		
		self.current_elife = 0
		self.elife = self.elife_sprites[self.current_elife]
		self.elife = pygame.transform.scale(self.elife,(150,150))
		self.elife_rect = self.elife.get_rect()
		self.elife_rect.right = self.screen_rect.right - 150
		self.elife_rect.bottom = self.screen_rect.bottom - 180
		
##########################################################################################################################		
		
		#Checks if How to Play section is active
		self.htp_check = False
		#Checks if Credits section is active
		self.credits_check = False
		#Checks if Power Up menu is active
		self.pu_check = False
		
	def draw_buttons(self):
		
		if not self.htp_check and not self.credits_check and not self.pu_check:
			#Generates Main Menu
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.play_button, self.play_rect)
			self.screen.blit(self.htp_button, self.htp_rect)
			self.screen.blit(self.credits_button, self.credits_rect)
			self.screen.blit(self.logo, self.logo_rect)
			
		elif self.htp_check:
			#Generates How To Play Menu
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.back_button, self.back_rect)
			self.screen.blit(self.space, self.space_rect)
			self.screen.blit(self.arrow, self.arrow_rect)
			self.screen.blit(self.pu, self.pu_rect)
			self.screen.blit(self.annihilate, self.annihilate_rect)
			
		elif self.credits_check:
			#Generates Credits Menu
			self.screen.fill(self.settings.bg_color, self.screen_rect)
			self.screen.blit(self.back_button, self.back_rect)
			#placeholder for credits sprite
		
		elif self.pu_check:
			#Generates Power-Up Menu
			self.screen.blit(self.pumenu_button, self.pumenu_rect)
			self.screen.blit(self.creds_image, self.creds_rect)
			self.screen.blit(self.bdmg, self.bdmg_rect)
			self.screen.blit(self.bspd, self.bspd_rect)
			self.screen.blit(self.ts, self.ts_rect)
			self.screen.blit(self.deus, self.deus_rect)
			self.screen.blit(self.sspd, self.sspd_rect)
			self.screen.blit(self.sfrm, self.sfrm_rect)
			self.screen.blit(self.bc, self.bc_rect)
			self.screen.blit(self.elife, self.elife_rect)
			
		#Text for available space credits
		self.creds = self.stats.creds
		creds_str = 'Spaces Credits: ' + str(self.creds)
		self.creds_image = self.font.render(creds_str, True, self.text_color, self.settings.bg_color)
		self.creds_rect = self.creds_image.get_rect()
		self.creds_rect.left = self.screen_rect.left + 120
		self.creds_rect.top = self.screen_rect.top + 120
			
		
