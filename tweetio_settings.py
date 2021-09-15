import pygame


class GameSettings:
    # All settings for the Tweetio game are stored here
    def __init__(self):
        # initialize the game's settings.
        # Screen Settings
        title = 'Tweetio'
        resolution = [1200, 800]
        idiot = True
        # ask user for resolution input in loop
        while idiot:
            try:
                resolution[0] = input('Enter your width resolution: ')
                resolution[0] = int(resolution[0])
                resolution[1] = input('Enter your length resolution: ')
                resolution[1] = int(resolution[1])
                idiot = False
            except ValueError:
                print('Please input an integer')
        colour_values = (230, 230, 230)
        pygame.display.set_caption(title)
        # set screen width
        self.screen_width = resolution[0]
        # set screen height
        self.screen_height = resolution[1]
        # set background colour
        self.bg_colour = colour_values
