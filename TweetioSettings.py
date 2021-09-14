import pygame


class GameSettings:
    # All settings for the Tweetio game are stored here
    def __init__(self):
        # initialize the game's settings.
        # Screen Settings
        title = 'Tweetio'
        resolution = [1200, 800]
        colour_values = (230, 230, 230)
        pygame.display.set_caption(title)
        self.screen_width = resolution[1]
        # Makes the most recently drawn screen visible
        self.screen_height = resolution[2]
        # set background colour
        self.bg_colour = colour_values

