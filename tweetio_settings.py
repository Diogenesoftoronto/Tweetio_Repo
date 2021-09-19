import pygame


class GameSettings:
    # All settings for the Tweetio game are stored here
    def __init__(self, screen_dimensions=(800, 1200)):
        # initialize the game's settings.
        # Screen Settings
        title = 'Tweetio'

        colour_values = (0, 0, 0)
        pygame.display.set_caption(title)
        # set screen width
        self.screen_width = screen_dimensions[0]
        # set screen length
        self.screen_height = screen_dimensions[1]
        # set background colour
        self.bg_colour = colour_values
