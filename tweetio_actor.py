import os
import pygame
from pygame import surface

class ActorCharacter:
    """This class manages the actor character"""

    def __init__(self, actor_controller, actor_image=os.environ['test_image'], twitter_word='Default',
                 twitter_sentiment_colour=(0, 0, 230), starting_position=(600, 600, 100, 100)):
        """Initialize the actor character and set's its starting position"""
        self.screen = actor_controller.screen
        self.screen_rect = actor_controller.screen.get_rect()

        # load the actor character image and get its rect.
        self.image = pygame.image.load(actor_image)
        # create a rectangle around image
        self.rect = self.image.get_rect()
        # set the font of the text drawn on the player character(change impact to font file environ)
        self.font_title = pygame.font.SysFont("impact", 20)
        # render the text using the variables provided
        self.text_title = self.font_title.render(twitter_word, True, twitter_sentiment_colour)
        # creates a rectangle surface for text
        self.rect_title = self.text_title.get_rect()
        # display text in the center of the screen
        self.start_ps = pygame.Rect(starting_position)

    def blit_me(self):
        """Draw actor character at its current location"""
        s1 = self.screen.blit(self.image, self.rect)
        s2 = s1.pygame.surface.blit(self.rect, self.rect_title)
        return s2
