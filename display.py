import os
import sys
import pygame

from pygame.locals import QUIT, KEYUP, K_ESCAPE

from board import Board, Color
from constants import FPS, WINDOW_WIDTH, WINDOW_HEIGHT

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centre display window.

fps_clock = pygame.time.Clock()


DISPLAY_SURF = None
game_board = None


def terminate():
    pygame.quit()
    sys.exit()


def check_for_quit():
    for _ in pygame.event.get(QUIT):
        terminate()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            terminate()
        pygame.event.post(event)

    return False


def start(fen='', bg_color=Color.ASH):
    pygame.init()

    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('LOCI')

    check_for_quit()

    DISPLAY_SURF.fill(bg_color)
    game_board = Board(bg_color, DISPLAY_SURF)
    game_board.display_board()

    if fen:
        game_board.update_pieces(fen)
    else:
        game_board.draw_pieces()

    pygame.display.update()
    fps_clock.tick(FPS)


def update(fen):
    check_for_quit()
    game_board.display_board()
    game_board.update_pieces(fen)

    pygame.display.update()
    fps_clock.tick(FPS)
