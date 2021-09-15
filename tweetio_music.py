import pygame
from pygame import mixer


class MusicPlayer:
    """Handle music in Tweetio"""

    def __init__(self, music_path=str, music_volume=float):
        mixer.init()
        mixer.music.load(music_path)
        mixer.music.set_volume(music_volume)
        mixer.music.play()

