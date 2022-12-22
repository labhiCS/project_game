import sys
import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group

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
    
    #Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()