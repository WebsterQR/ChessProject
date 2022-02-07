FPS = 60

screen_width = 800
screen_height = 600

desk_size = min(screen_height, screen_width) * 0.8
cell_size = desk_size / 8

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
DARK_CELL = (139, 69, 19)
LIGHT_CELL = (244, 164, 96)
DARK_RED = (128, 0, 0)

chessboard = [[False for i in range(8)] for j in range(8)]

figures = {
    'pawn': 8,
    'horse': 2,
    'bishop': 2,
    'rock': 2,
    'queen': 1,
    'king': 1
}
