import sys

import pygame

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set background color
    bg_color = (220, 220, 220)

    # main loop of the game
    while True:
        # Check for keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make most recent screen visible
        screen.fill(bg_color)
        pygame.display.flip()

run_game()
