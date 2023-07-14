import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Hide pygame support message

import sys
import pygame

from pygame.locals import QUIT, KEYUP, K_ESCAPE

from chessboard.board import Board, Color
from chessboard.constants import FPS, STARTING_FEN, WINDOW_CAPTION, WINDOW_WIDTH, WINDOW_HEIGHT


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


def start(fen=STARTING_FEN, bg_color=Color.ASH, caption=WINDOW_CAPTION):
    pygame.init()

    display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(caption)

    display_surf.fill(bg_color)
    game_board = Board(bg_color, display_surf)

    update(fen, game_board)

    return game_board


def update(fen, game_board):
    check_for_quit()
    game_board.update_pieces(fen)

    pygame.display.update()
    fps_clock.tick(FPS)


def flip(game_board: Board):
    check_for_quit()
    game_board.flip()

    pygame.display.update()
    fps_clock.tick(FPS)
