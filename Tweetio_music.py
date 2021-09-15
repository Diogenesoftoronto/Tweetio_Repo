import pygame
from pygame import mixer


class MusicPlayer:
    """Handle music in Tweetio"""

    def __init__(self, music_path=str, music_volume=float):
        mixer.init()
        mixer.music.load(music_path)
        mixer.music.set_volume(music_volume)
        mixer.music.play()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            # pauses music
            mixer.music.pause()
        elif keys[pygame.K_r]:
            # resumes music
            mixer.music.unpause()
        elif keys[pygame.K_e]:
            mixer.music.stop()
