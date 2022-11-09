#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3
import pygame
pygame.init()
pygame.mixer.music.load("desafio21.mp3")
pygame.mixer.music.play()
pygame.event.wait()