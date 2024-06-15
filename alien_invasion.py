import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInversion:
    """overall class to mange game assets and behaviour."""
    def __init__(self):
        """initialize the game,and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Inversion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        #set the background colour.
        self.bg_colour = (230,230,230)

    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        #respond for keyboard and mouse events .
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """respond to keypress"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to key release"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullect and add it to the bullects group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullet and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()

        #get rid of bullet that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

    def _create_fleet(self):
        """create the fleet of aliens"""
        #make an alien and keep adding aliens untill there's no room left
        #spaceing between aliens is one alien width
        alien = Alien(self)
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width ):
            self._create_alien(current_x)
            current_x += 2 * alien_width

    def _create_alien(self,x_postion):
        """create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_postion
        new_alien.rect.x = x_postion
        self.aliens.add(new_alien)

    def _update_screen(self):
         #update the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            self.aliens.draw(self.screen)

            pygame.display.flip()


if __name__=='__main__':
    #make a game instance,and run the game.
    ai=AlienInversion()
    ai.run_game()
