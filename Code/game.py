#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        from Code import menu
        while True:
            menu = menu(self.window)
            menu.run()
            pass

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame
