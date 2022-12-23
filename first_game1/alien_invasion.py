import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (0, 0, 230)

    # Make a a ship
    ship = Ship(ai_settings, screen)

    #make a group to store bullet in.
    bullets= Group()

    # Make an alien.
    alien = Alien(ai_settings, screen)
    
    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        
run_game()