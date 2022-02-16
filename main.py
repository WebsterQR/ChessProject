import random

import pygame
import settings
import UI


def main():
    pygame.init()

    pygame.display.set_caption('Chess game')
    #pygame.display.set_mode((settings.screen_width, settings.screen_width), pygame.RESIZABLE)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_width), pygame.RESIZABLE)
    screen.fill(settings.WHITE)

    pygame.display.update()

    clock = pygame.time.Clock()


    chessboard = UI.Chessboard(screen)

    #UI.draw_desk(screen)

    #UI.put_figures(screen, white_figures, black_figures)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                chessboard.button_down(event.button, event.pos)
                print(event.button, event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                chessboard.button_up(event.button, event.pos)


if __name__ == "__main__":
    main()