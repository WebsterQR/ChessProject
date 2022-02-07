import pygame
import settings

font_name = pygame.font.match_font('arial')

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, settings.RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def draw_desk(screen):

    size = settings.cell_size
    font = pygame.font.Font("fonts/Arial/arial_bolditalicmt.ttf", 18)
    letters = 'abcdefghigklmnopqrstuvwxyz'.upper()

    num_lines = pygame.Surface((size * 8, size // 2))
    num_rows = pygame.Surface((size // 2, size * 8))
    cells = pygame.Surface((size * 8, size * 8))
    board = pygame.Surface((
        2 * num_rows.get_width() + cells.get_width(),
        2 * num_lines.get_height() + cells.get_height()
    ))

    board.fill(settings.DARK_RED)
    num_rows.fill(settings.DARK_RED)
    num_lines.fill(settings.DARK_RED)


    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                color = settings.LIGHT_CELL
            else:
                color = settings.DARK_CELL
            cell = pygame.Surface((size, size))
            cell.fill(color)
            cells.blit(cell, (i * size, j * size))

    for i in range(8):
        letter = font.render(letters[i], 1, settings.WHITE)
        number = font.render(str(i + 1), 1, settings.WHITE)
        num_rows.blit(letter, (
            (num_rows.get_width() - letter.get_rect().width) // 2,
            i * size + (size - letter.get_rect().height) // 2
        ))
        num_lines.blit(number, (
            i * size + (size - number.get_rect().width) // 2,
            (num_lines.get_height() - letter.get_rect().height) // 2
        ))

    board.blit(num_lines, (num_rows.get_width(), 0))
    board.blit(num_lines, (num_rows.get_width(), num_lines.get_height() + cells.get_height()))
    board.blit(num_rows, (0, num_lines.get_height()))
    board.blit(num_rows, (num_rows.get_width() + cells.get_width(), num_lines.get_height()))
    board.blit(cells, (num_rows.get_width(), num_lines.get_height()))
    screen.blit(board, (10, 10))

    pygame.display.update()


def put_figures(screen, white_figures, black_figures):
    pawn_black = pygame.image.load("images/pawn_black.png")
    pawn_white = pygame.image.load("images/pawn_white.png")
    bishop_black = pygame.image.load("images/bishop_black.png")
    bishop_white = pygame.image.load("images/bishop_white.png")
    horse_black = pygame.image.load("images/horse_black.png")
    horse_white = pygame.image.load("images/horse_white.png")
    rock_black = pygame.image.load("images/rock_black.png")
    rock_white = pygame.image.load("images/rock_white.png")
    king_black = pygame.image.load("images/king_black.png")
    king_white = pygame.image.load("images/king_white.png")
    queen_black = pygame.image.load("images/queen_black.png")
    queen_white = pygame.image.load("images/queen_white.png")
    black = dict(pawn=pawn_black, bishop=bishop_black, horse=horse_black, rock=rock_black, king=king_black,
                 queen=queen_black)
    white = dict(pawn=pawn_white, bishop=bishop_white, horse=horse_white, rock=rock_white, king=king_white,
                 queen=queen_white)

    x = 50
    y = 600

    for figure, image in black.items():
        screen.blit(image, (x, y))
        fig_count = black_figures[figure]
        draw_text(screen, str(fig_count), 18, x, y + 20)
        x += 70
    y += 70
    x = 50
    for figure, image in white.items():
        screen.blit(image, (x, y))
        fig_count = black_figures[figure]
        draw_text(screen, str(fig_count), 18, x, y + 20)
        x += 70

    pygame.display.update()