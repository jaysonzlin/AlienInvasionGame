import pygame.font, pygame.sprite

from ship import Ship

class Scoreboard:
	'''A class to report scoring information'''
	
	def __init__(self, ai_game):
		'''Initialize scorekeeping attributes'''
		
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = ai_game.settings
		self.stats = ai_game.stats
		self.ai_game = ai_game
		
		#Font settings for scoring information
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('impact', 20)
		self.lvl_font = pygame.font.SysFont('impact', 30)
		
		#Prepare the initial score image
		self.prep_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		'''Turn the score into a rendered image'''
		
		score_str = 'Score: ' + str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
		high_score_str = 'High Score: ' + str(self.stats.high_score)
		self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
		
		#Display the score at the top right of the screen
		#High Score on top of Score
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.right - 20
		self.high_score_rect.top = 10
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 35
	
	def check_high_score(self):
		'''Check to see if there's a new high score'''
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			
	def prep_level(self):
		'''Turn the level into a rendered image'''
		level_str = 'Level ' + str(self.stats.rd)
		self.level_image = self.lvl_font.render(level_str, True, self.text_color, self.settings.bg_color)
		
		#Position the level in the center
		self.level_rect = self.level_image.get_rect()
		self.level_rect.centerx = self.screen_rect.centerx
		self.level_rect.top = 15
			
	def prep_ships(self):
		'''Show how many ships are left'''
		self.ships = pygame.sprite.Group()
		
		#For four or more lives
		if self.settings.ship_lives > 3:
			ship = Ship(self.ai_game, self.settings.ship_type)
			ship.rect.x = 10
			ship.rect.y = 10
			self.ships.add(ship)
			
			lives_str = 'x ' + str(self.settings.ship_lives)
			self.lives_image = self.lvl_font.render(lives_str, True, self.text_color, self.settings.bg_color)
			self.lives_rect = self.lives_image.get_rect()
			self.lives_rect.left = ship.width + 20
			self.lives_rect.top = 15
			return
		
		lives_str = ''
		self.lives_image = self.lvl_font.render(lives_str, True, self.text_color, self.settings.bg_color)
		self.lives_rect = self.lives_image.get_rect()
		self.lives_rect.left = 70
		self.lives_rect.top = 15
		
		#For three or less lives
		for ship_number in range(self.settings.ship_lives):
			ship = Ship(self.ai_game, self.settings.ship_type)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	def show_score(self):
		'''Draw score to the screen'''
		
		self.check_high_score()
		self.prep_score()
		self.prep_level()
		self.prep_ships()
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.lives_image, self.lives_rect)
		self.ships.draw(self.screen)
		

