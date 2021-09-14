"""In Tweetio, the player controls a collection of words that that appears in the center of
the screen. The player character as the game progress the player must stay within the
display in order to survive. As the game progresses more obstacles appear that hamper the player's
ability to stay within the screen. The game is rather similar to shovel knight, Mario, and Space invaders
in terms of gameplay.

What makes it unique is that content the player engages with is based on sentiment analysis from twitter
and tweets from live online data. Enemies and power-ups as well as boss dialogue is generated using twitter.com
The player can destroy enemies or avoid them. if the player destroys enemies they gain power-ups. However, more enemies
are generated. If the player avoids enemies they gain no power-ups but not as many enemies are generated. A score is
generated after killing the first enemy along with the score board at the top of the screen. If the player dies without
killing enemies a score is generated based on how much time was spent alive. Positive music is activated when the player
kills no enemies and negative music when the player kills enemies.

Space invaders but for feelings--Death from Discord"""

import pygame
import Tweepy
import credentials
import TweetioSettings
import sys
from pygame import mixer
import json

"""import otherlibraries"""


class TweetioGame:
    """Overall class to manage game assets and create game resources, and behaviour"""

    def __init__(self):
        """initialize game, and create game resources"""
        pygame.init()
        self.TweetioSettings = TweetioSettings.GameSettings()
        self.screen = pygame.display.set_mode(self.TweetioSettings.screen_height, self.TweetioSettings.screen_width)

    def run_game(self):
        """start the main loop for the game."""
        # make the most recently drawn screen visible.
        pygame.display.flip()
        mixer.init()
        mixer.music.load('Positive_Music.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play()

        while True:
            # watches for keyboard and mouse events.
            for event in pygame.event.get():
                print("Press 'p' to pause, 'r' to resume")
                query = input("  ")
                if query == 'p':
                    # Pausing the music
                    mixer.music.pause()
                elif query == 'r':
                    # Resuming the music
                    mixer.music.unpause()
                if event.type == pygame.QUIT:
                    sys.exit()

    class PlayerCharacter:
        """This class manages the player character"""
        def __init__(self, pc_controller):
            """Initialize the player character and set's its starting position"""
            self.screen = pc_controller.screen
            self.screen_rect = pc_controller.screen.get_rect()

            # load the player character image and get its rect.
            self.image
    # def twitterdata(self):
    # method that allows the game to use data generated from twitter


if __name__ == '__main__':
    # makes a game instance, and run the game.
    tg = TweetioGame()
    tg.run_game()
