import pygame
import os
import time

class MusicPlayer:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()

        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(self.base_dir, music_folder)

        self.playlist = [
            f for f in os.listdir(self.music_folder)
            if f.endswith((".mp3", ".wav"))
        ]

        self.index = 0
        self.playing = False
        self.paused = False

        self.start_time = 0
        self.paused_time = 0

        if self.playlist:
            self.load()

    def load(self):
        path = os.path.join(self.music_folder, self.playlist[self.index])
        pygame.mixer.music.load(path)

    def play(self):
        if not self.playlist:
            return

        pygame.mixer.music.play()
        self.playing = True
        self.paused = False
        self.start_time = time.time()

    def pause(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
            self.paused_time = time.time()

        elif self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.load()
        self.play()

    def prev(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.load()
        self.play()

    def current_track(self):
        if not self.playlist:
            return "No music"
        return self.playlist[self.index]

    def get_progress(self):
        if not self.playing:
            return 0

        if self.paused:
            elapsed = self.paused_time - self.start_time
        else:
            elapsed = time.time() - self.start_time

        return elapsed
