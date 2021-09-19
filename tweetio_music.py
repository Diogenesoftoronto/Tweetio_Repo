import os
from pygame import mixer


class MusicPlayer:
    """Handles music in Tweetio"""

    def __init__(self, music_path=os.environ['music_positive_path'], music_volume=0.7):
        # initiates the music class
        mixer.init()
        # loads the music from the file path
        mixer.music.load(music_path)
        # sets the volume of the music
        mixer.music.set_volume(music_volume)

    def play(self):
        """play music function"""
        mixer.music.play()

