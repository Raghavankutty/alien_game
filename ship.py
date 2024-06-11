import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.screen_react = ai_game.screen.get_react()

        #load the ship and get its react.

        self.image = pygame.image.load('images/Ship.bmp')
        self.rect = self.image.get.rect()

        #start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_react.midbottom

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    
