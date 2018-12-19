
from castle_game_edit import castle_game
from text_adventure_edit import text_adventure
import pygame
from pygame.locals import *
import time
import random

pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(255)

def button_check(pos, x, y, x1, y1):
    return pos[0] >= x and pos[0] < x + x1 and pos[1] >= y and pos[1] < y + y1

def make_button(surface, color, text_color, x, y, width, height, text):
    pygame.draw.rect(surface, (0, 0, 0), (x - 1, y - 1, width + 2, height + 2), 1)
    pygame.draw.rect(surface, color, (x, y, width, height))

    myfont = pygame.font.SysFont('Arial Black', 15)
    label = myfont.render(text, 1, text_color)
    surface.blit(label, (x + 2, y))
    pygame.display.flip()
menu_items = ['Play City Defense', 'Text Based Adventure', 'Exit']
while True:

    black = (0, 0, 0)
    silver = (143, 155, 173)
    for i in range(len(menu_items)):
        make_button(gameDisplay, silver, black, 10, 10 + (20 * i), 200, 20, menu_items[i])
    for event in pygame.event.get():
        if event.type == 5:
            if event.button == 1:
                for i in range(len(menu_items)):
                    if button_check(event.pos, 10, 10 + (20 * i), 200, 10 + (20 * i)):
                        if i == 0:
                            castle_game()
                        elif i == 1:
                            pygame.quit()
                            text_adventure()
                        if i == 2:
                            pygame.quit()
                            exit(0)
                        elif i == 3:
                            pygame.quit()
                            exit(0)
