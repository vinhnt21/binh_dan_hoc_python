import pygame
import os
pygame.mixer.init()
file_path = os.path.abspath('Lec01/01_play_thienlioi.mp3')
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue


