import pygame
import settings

def draw_desk(screen):
    desk_width = settings.screen_width * 0.8
    desk_height = settings.screen_height * 0.8
    step_width = desk_width // 8
    step_height = desk_height // 8
    for i in range(8):
        _draw_line(screen, 10, 10 + step_height * i, step_width, i)
    pygame.display.update()


def _draw_line(screen, x_coord, y_coord, square_width, line_num):
    for i in range(8):
        _draw_spot(screen, x_coord, y_coord, square_width, line_num, i)

def _draw_spot(screen, x_coord, y_coord, square_width, line_num, row_num):
    if (line_num + row_num) % 2 == 0:
        pygame.draw.rect(screen,
                         settings.WHITE,
                         pygame.Rect((x_coord + square_width * row_num, y_coord, square_width, square_width)),
                         )
    else:
        pygame.draw.rect(screen,
                         settings.BLACK,
                         pygame.Rect((x_coord + square_width * row_num, y_coord, square_width, square_width)),
                         )