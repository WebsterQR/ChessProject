import pygame
import settings

font_name = pygame.font.match_font('arial')


def draw_text(screen, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, settings.RED)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


colors = ["dark_cell.jpeg", "light_cell.jpeg", "border.jpeg"]


class Chessboard():
    def __init__(self, screen):
        self.screen = screen
        self.cells_group = pygame.sprite.Group()
        self.figures_group = pygame.sprite.Group()
        self.board_size = (0, 0)
        self.draw_desk(self.screen)
        self.draw_figures(self.screen)
        self.hasFigure = False
        self.takenFigureName = None
        self.matrix_board = [[0 for _ in range(8)]for _ in range(8)]

    def draw_desk(self, screen):
        font = pygame.font.Font(settings.FONT_PATH, settings.FONT_SIZE)

        num_lines = pygame.Surface((settings.cell_size * 8, settings.cell_size // 2))

        num_rows = pygame.Surface((settings.cell_size // 2, settings.cell_size * 8))

        cells = pygame.Surface((settings.cell_size * 8, settings.cell_size * 8))

        board = pygame.Surface((
            2 * num_rows.get_width() + cells.get_width(),
            2 * num_lines.get_height() + cells.get_height()
        ))
        self.board_size = board.get_size()
        board.fill(settings.DARK_RED)
        num_rows.fill(settings.DARK_RED)
        num_lines.fill(settings.DARK_RED)

        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color_index = 0
                else:
                    color_index = 1
                cell = Cell(color_index, settings.cell_size, (i, j), settings.LETTERS[i] + str(j + 1))
                self.cells_group.add(cell)

        for i in range(8):
            letter = font.render(settings.LETTERS[i], 1, settings.WHITE)
            number = font.render(str(i + 1), 1, settings.WHITE)
            num_rows.blit(number, (
                (num_rows.get_width() - letter.get_rect().width) // 2,
                i * settings.cell_size + (settings.cell_size - letter.get_rect().height) // 2
            ))
            num_lines.blit(letter, (
                i * settings.cell_size + (settings.cell_size - number.get_rect().width) // 2,
                (num_lines.get_height() - letter.get_rect().height) // 2
            ))

        board.blit(num_lines, (num_rows.get_width(), 0))
        board.blit(num_lines, (num_rows.get_width(), num_lines.get_height() + cells.get_height()))
        board.blit(num_rows, (0, num_lines.get_height()))
        board.blit(num_rows, (num_rows.get_width() + cells.get_width(), num_lines.get_height()))
        screen.blit(board, (settings.screen_width // 2 - board.get_width() // 2, 10))
        for one_cell in self.cells_group:
            one_cell.rect.x += ((settings.screen_width // 2 - board.get_width() // 2) + num_rows.get_width())
            one_cell.rect.y += (num_lines.get_height() + 10)
        self.cells_group.draw(self.screen)
        pygame.display.update()

    def draw_figures(self, screen):
        names = ['queen', 'king', 'bishop', 'pawn', 'rock', 'horse']
        place = pygame.Surface((settings.cell_size * 8, settings.cell_size))
        place.fill(settings.WHITE)
        x_start = settings.screen_width // 2 - place.get_width() // 2
        y_start = self.board_size[1] + 70
        cells_poses = []
        for i in range(6):
            place_cell = placeCell(2, (x_start, y_start), place.get_width() / 6, (i, 0), names[i])
            cells_poses.append(place_cell.rect)
            self.figures_group.add(place_cell)
        self.figures_group.draw(screen)
        for num, figure_name in enumerate(names):
            image = pygame.image.load(settings.IMG_PATH + figure_name + ".png").convert_alpha()
            # image = pygame.transform.scale(image, (cells_poses[num][2]- 10, cells_poses[num][3] - 10))
            image = pygame.transform.scale(image, (place_cell.rect.width * 0.5, place_cell.rect.height * 0.5))
            fig_x = cells_poses[num][0] + cells_poses[num][2] // 2 - image.get_width() * 0.75
            fig_y = cells_poses[num][1] + cells_poses[num][3] // 2 - image.get_height() * 0.75
            screen.blit(image, (fig_x, fig_y))
        pygame.display.update()

    def get_cell(self, position: tuple):
        for cell in self.cells_group:
            if cell.rect.collidepoint(position):
                return (cell, "board")
        for cell in self.figures_group:
            if cell.rect.collidepoint(position):
                return (cell, "figure")
        return None

    def button_down(self, button_type: int, position: tuple):
        cell = self.get_cell(position)
        if cell[0]:
            if cell[1] == "figure" and not self.hasFigure:
                print("Захват фигуры", cell[0].field_name)
                self.hasFigure = True
                self.takenFigureName = cell[0].field_name
            elif cell[1] == "board" and self.hasFigure:
                print(f"Ставим фигуру {self.takenFigureName} на клетку", cell[0].field_name)
                self.put_figure_on_board(cell[0], self.takenFigureName)
                coords_x, coords_y = get_matrix_indexes(cell[0].field_name)
                #self.matrix_board[coords_x][coords_y] = 1
                self.mark_matrix_after_move(self.takenFigureName, coords_x, coords_y)
                self.hasFigure = False
                self.takenFigureName = None

    def button_up(self, button_type: int, position: tuple):
        cell = self.get_cell(position)

    def put_figure_on_board(self, cell, figure_name):
        figure_image = pygame.image.load(settings.IMG_PATH + figure_name + ".png")
        figure_image = pygame.transform.scale(figure_image, (cell.rect.width * 0.75, cell.rect.height * 0.75))
        #figure_image.set_colorkey((255, 255, 255))
        self.screen.blit(figure_image,
                         (cell.rect.x + ((cell.rect.width - figure_image.get_width()) // 2),
                          (cell.rect.y + (cell.rect.height - figure_image.get_height()) // 2)))
        pygame.display.update()

    def mark_matrix_after_move(self, fig_name, x, y):
        self.matrix_board[x][y] = fig_name[0].upper()
        if fig_name == "king":
            for i in range(8):
                for j in range(8):
                    if abs(i - x) <= 1 and abs(j - y) <= 1 and self.matrix_board[i][j] == 0:
                        self.matrix_board[i][j] = 1
            for i in range(8):
                print(*self.matrix_board[i])
        if fig_name == "queen":
            for i in range(8):
                for j in range(8):
                    if (i == x or j == y or abs(i - x) == abs(j - y)) and self.matrix_board[i][j] == 0:
                        self.matrix_board[i][j] = 1
            for i in range(8):
                print(*self.matrix_board[i])


def get_matrix_indexes(cell_name):
    letter = cell_name[0]
    number = cell_name[1]
    return (settings.letter_to_num[letter], int(number) - 1)


class Cell(pygame.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x, y = coords
        self.color = color_index
        self.field_name = name
        self.image = pygame.image.load(settings.IMG_PATH + colors[color_index])
        self.image = pygame.transform.scale(self.image, (settings.cell_size, settings.cell_size))
        self.rect = pygame.Rect(x * settings.cell_size, y * settings.cell_size, settings.cell_size, settings.cell_size)


class placeCell(pygame.sprite.Sprite):
    def __init__(self, color_index: int, start_pos: tuple, cell_size: int, coords: int, name: str):
        super().__init__()
        self.color = color_index
        self.field_name = name
        x, y = coords[0], coords[1]
        self.image = pygame.image.load(settings.IMG_PATH + colors[color_index])
        self.image = pygame.transform.scale(self.image, (settings.cell_size, settings.cell_size))
        self.rect = pygame.Rect(start_pos[0] + x * cell_size, start_pos[1] + y * cell_size, cell_size, cell_size)


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
