import random

import pygame
import settings
import UI


def main():
    pygame.init()

    pygame.display.set_caption('Chess game')
    #pygame.display.set_mode((settings.screen_width, settings.screen_width), pygame.RESIZABLE)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_width), pygame.RESIZABLE)
    screen.fill(settings.LIGHT_BLUE)

    pygame.display.update()

    clock = pygame.time.Clock()


    UI.draw_desk(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        #clock.tick(settings.FPS)

        #pygame.display.update()


if __name__ == "__main__":
    main()