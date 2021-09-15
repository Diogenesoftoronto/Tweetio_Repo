import pygame


class PlayerCharacter:
    """This class manages the player character"""

    def __init__(self, pc_controller, twitter_word=str,twitter_sentiment_colour=tuple):
        """Initialize the player character and set's its starting position"""
        self.screen = pc_controller.screen
        self.screen_rect = pc_controller.screen.get_rect()

        # load the player character image and get its rect.
        self.image = pygame.image.load(player_image)
        self.rect = self.image.get_rect()
        self.font_title = pygame.font.SysFont("impact", 20)
        self.text_title = self.font_title.render(twitter_word, True, twitter_sentiment_colour)
        self.rect_title = self.text_title.get_rect(center=pygame.screen.get_rect().center)

    def blit_me(self):
        """Draw Player character at its current location"""
        self.screen.blit(self.image, self.rect, self.rect_title)