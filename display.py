import os
import sys
import pygame

from pygame.locals import QUIT, KEYUP, K_ESCAPE

from board import Board, Color
from constants import FPS, WINDOW_WIDTH, WINDOW_HEIGHT


os.environ['SDL_VIDEO_CENTERED'] = '1'  # Centre display window.

fps_clock = pygame.time.Clock()


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


def start(fen='', bg_color=Color.ASH, caption="chess-board"):
    pygame.init()

    display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(caption)

    check_for_quit()

    display_surf.fill(bg_color)
    game_board = Board(bg_color, display_surf)

    if not fen:
        game_board.display_board()
        game_board.draw_pieces()
    else:
        game_board.update_pieces(fen)

    pygame.display.update()
    fps_clock.tick(FPS)

    return game_board


def update(fen, game_board):
    check_for_quit()
    game_board.update_pieces(fen)

    pygame.display.update()
    fps_clock.tick(FPS)
