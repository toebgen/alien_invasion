import pygame
from pygame.sprite import Group

from alien import Alien
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions


def run_game():
    # Initialize settings, game and screen object
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(settings, screen, "Play")

    # Create an instance to store game statistics and scoreboard
    stats = GameStats(settings)
    scoreboard = Scoreboard(settings, screen, stats)

    # Make a ship
    ship = Ship(screen, settings)
    # Make a group for storing bullets
    bullets = Group()
    # Make a group of aliens
    aliens = Group()
    game_functions.create_fleet(settings, screen, ship, aliens)
    
    # main loop of the game
    while True:
        game_functions.check_events(settings, screen, stats, play_button,
                                    ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            game_functions.update_bullets(settings, screen, ship, stats,
                                          scoreboard, aliens, bullets)
            game_functions.update_aliens(settings, stats, screen, ship, aliens, bullets)
        
        game_functions.update_screen(settings, screen, stats, scoreboard, ship,
                                     aliens, bullets, play_button)


run_game()
