import sys, pygame

from time import sleep, time
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien, invader1, invader2, invader3

class AlienInvasion:
	'''Overall class to manage game assets and behavior.'''
	
	def __init__(self):
		'''Initialize the game, and create game resources'''
		
		pygame.init()
		
		#Importing settings
		self.settings = Settings()
		
		#Game runtime
		self.clock = pygame.time.Clock()
		self.death_timer = time()
		
		#Round number
		self.rd = 1
		
		#Counter for increasing alien lives
		self.alien_up = 0
		
		#Prevents round increments due to empty screen from ship hits
		self.rdcheck = True
		
		#Sound effects and volume
		self.ship_death = pygame.mixer.Sound('sounds/ship_death.wav')
		self.bullet_firing = pygame.mixer.Sound('sounds/bullet_firing.wav')
		self.alien_pop = pygame.mixer.Sound('sounds/alien_pop.wav')
		self.ufo_death = pygame.mixer.Sound('sounds/ufo_death.wav')
		
		#Background Music
		pygame.mixer.music.load('sounds/bg_music.wav')
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.3)
		
		#Fleet check implementation boolean
		self.fleet_check = True
		
		#For preset screen size:
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		
		#Create an instance to store the game statistics
		self.stats = GameStats(self)
		
		#Creating the game window
		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion Game")
		
		#Creating an instance of our ship and a group to hold bullets
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		
		self._create_fleet()
		
	def run_game(self):
		'''Start the main loop for the game'''
		
		while True:
			self._check_events()
			
			if self.stats.game_active:	
				self.ship.update()					
				self.settings.update()
				self._update_aliens()
				self._update_bullets()
			
			self._update_screen()
			
			
	def _check_events(self):
		'''Respond to keypresses and mouse events.'''
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()			
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
				
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
					
	def _check_keydown_events(self, event):
		'''Respond to keypresses.'''
		
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			
	def _check_keyup_events(self, event):
		'''Respond to key releases'''
		
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
			
	def _ship_hit(self):
		'''Respond to the ship being hit by an alien'''
		
		#Decrement ship_lives
		if self.settings.ship_lives > 0:
			self.settings.ship_lives -= 1

		#Make the ship explode
		self.ship.image = pygame.image.load('images/explosion.png')
		self.ship.image = pygame.transform.scale(self.ship.image,(50,50))
		self.ship.blitme()

		#Get rid of any remaining aliens and bullets
		self.aliens.empty()
		self.bullets.empty()
		
		pygame.mixer.Sound.play(self.ship_death)
		self.ship.dead_check = True
		self.rdcheck = False
		self.death_timer = time()
		
		if self.settings.ship_lives <= 0:
			self.stats.game_active = False
		
		
	def _fire_bullet(self):
		'''Create a new bullet and add it to the bullets group.'''
		
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			pygame.mixer.Sound.play(self.bullet_firing)
			
	def _update_bullets(self):
		'''Update position of bullets and get rid of old bullets'''
		
		#Update bullet positions
		self.bullets.update()
		
		#Get rid of bullets that have disappeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		
		#Respond to bullet-alien collisions
		self._check_bullet_alien_collisions()
	
	def _check_bullet_alien_collisions(self):
		'''Respond to bullet-alien collisions'''
					
		#Check for any bullets that have hit aliens
		#If so, get rid of the bullet
		#Each hit causes the alien to lose life points and removes alien if alien life points are 0
		for alien in self.aliens.sprites():
			col_i = pygame.sprite.spritecollide(alien, self.bullets, self.settings.god_bullet_off)
			if col_i:
				alien.lives -= self.settings.bullet_power
				if alien.lives <= 0:
					pygame.mixer.Sound.play(self.alien_pop)
					alien.kill()
		
		if not self.aliens and self.ship.dead_check == False:
			#Destroy existing bullets, increment the round, and create new fleet
			self.bullets.empty()
			sleep(0.05)
			if self.rdcheck:
				self.rd += 1 
				#For every new round, add a life point to all aliens and increase their speed
				self.alien_up += 1
				self.settings.alien_spd_multi += 10
			if not self.rdcheck:
				self.ship.center_ship()
			self._create_fleet()
			self.rdcheck = True
				
	def _create_fleet(self):
		'''Create the fleet of aliens'''
		
		#Create an alien and find the number of aliens in a row
		#Different aliens for different rounds
		#Spacing between each alien is equal to one alien width
		if (self.rd % 3) == 1:
			alien = invader1(self)
		if (self.rd % 3) == 2:
			alien = invader2(self)
		if (self.rd % 3) == 0:
			alien = invader3(self)
			
		alien_width, alien_height = alien.rect.size
		
		#Determine the number of aliens in a row
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = int(available_space_x // (1.5 * alien_width))
		
		#Determine the number of rows of aliens that fit on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - (6 * alien_height) - ship_height)
		number_rows = int(available_space_y // (1.5 * alien_height))
		
		#Create the complete fleet of aliens
		for row_number in range(number_rows):	
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
		
		#New fleet always moves rightward		
		self.settings.fleet_direction = 1
			
	def _create_alien(self, alien_number, row_number):
		'''Create an alien and place it in the row'''
		
		if (self.rd % 3) == 1:
			alien = invader1(self)
			alien.lives += self.alien_up
		if (self.rd % 3) == 2:
			alien = invader2(self)
			alien.lives += self.alien_up
		if (self.rd % 3) == 0:
			alien = invader3(self)
			alien.lives += self.alien_up
			
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 1.5 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 1.5 * alien.rect.height * row_number + 25
		self.aliens.add(alien)
			
	def _check_fleet_edges(self):
		'''Respond appropriately if any aliens have reached an edge'''
		
		for alien in self.aliens.sprites():
			if alien.check_fleet():
				self.fleet_check = True
			if alien.check_edges() and self.fleet_check:
				self._change_fleet_direction()
				break
				
	def _change_fleet_direction(self):
		'''Drop the entire fleet and change the fleet's direction'''
		
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
			
		self.settings.fleet_direction *= -1
		self.fleet_check = False
		
	def _check_aliens_bottom(self):
		'''Check if any aliens have reached the bottom of the screen'''
		
		screen_rect = self.screen.get_rect()
		for alien in self.aliens.sprites():
			if alien.rect.bottom >= screen_rect.bottom:
			#Treat this the same as if the ship got hit.
				self._ship_hit()
				break
			
	def _update_aliens(self):
		'''Updates position and animation of aliens'''
		
		self._check_fleet_edges()	
		self.aliens.update()
		
		#Waits for two seconds to pass before respawning ship
		if (time() - self.death_timer) > 2:
			self.ship.dead_check = False
		
		#Look for alien-ship collisions
		if pygame.sprite.spritecollideany(self.ship,self.aliens):
			self._ship_hit()
			
		#Look for aliens hitting the bottom of the screen
		self._check_aliens_bottom()
		
	def _update_screen(self):
		'''Update images on the screen, and flip to the new screen.'''
		
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
			
		#Make the most recently drawn screen visible
		pygame.display.flip()
		
		
if __name__ == '__main__':
	#Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
				
