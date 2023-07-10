import os
import pygame

from chessboard.constants import IMAGE_DIR
from chessboard.pieces import Piece, PieceColor, PieceType
from chessboard.fenparser import FenParser
from chessboard.utils import is_odd


class Board:
    a8, a7, a6, a5, a4, a3, a2, a1 = (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350), (100, 400), (100, 450)
    b8, b7, b6, b5, b4, b3, b2, b1 = (150, 100), (150, 150), (150, 200), (150, 250), (150, 300), (150, 350), (150, 400), (150, 450)
    c8, c7, c6, c5, c4, c3, c2, c1 = (200, 100), (200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450)
    d8, d7, d6, d5, d4, d3, d2, d1 = (250, 100), (250, 150), (250, 200), (250, 250), (250, 300), (250, 350), (250, 400), (250, 450)
    e8, e7, e6, e5, e4, e3, e2, e1 = (300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400), (300, 450)
    f8, f7, f6, f5, f4, f3, f2, f1 = (350, 100), (350, 150), (350, 200), (350, 250), (350, 300), (350, 350), (350, 400), (350, 450)
    g8, g7, g6, g5, g4, g3, g2, g1 = (400, 100), (400, 150), (400, 200), (400, 250), (400, 300), (400, 350), (400, 400), (400, 450)
    h8, h7, h6, h5, h4, h3, h2, h1 = (450, 100), (450, 150), (450, 200), (450, 250), (450, 300), (450, 350), (450, 400), (450, 450)

    board_rect = (
        (a8, b8, c8, d8, e8, f8, g8, h8),
        (a7, b7, c7, d7, e7, f7, g7, h7),
        (a6, b6, c6, d6, e6, f6, g6, h6),
        (a5, b5, c5, d5, e5, f5, g5, h5),
        (a4, b4, c4, d4, e4, f4, g4, h4),
        (a3, b3, c3, d3, e3, f3, g3, h3),
        (a2, b2, c2, d2, e2, f2, g2, h2),
        (a1, b1, c1, d1, e1, f1, g1, h1)
    )

    b_tile = pygame.image.load(os.path.join(IMAGE_DIR, 'btile.png'))
    w_tile = pygame.image.load(os.path.join(IMAGE_DIR, 'wtile.png'))

    def __init__(self, bg_color, display_surf):
        self.bg_color = bg_color
        self.display_surf = display_surf

        self.piece_rect = []
        self.current_fen = ''
        self.flipped = False
        self.fp = FenParser()

    def display_board(self):
        self.display_surf.fill(self.bg_color)
        pygame.draw.rect(self.display_surf, Color.BLACK, (95, 95, 410, 410), 10)

        self.draw_tiles()

    def draw_tiles(self):
        for i in range(1, len(Board.board_rect) + 1):
            for j in range(1, len(Board.board_rect[i - 1]) + 1):
                if is_odd(i):
                    if is_odd(j):
                        self.display_surf.blit(Board.w_tile, Board.board_rect[i - 1][j - 1])
                    else:
                        self.display_surf.blit(Board.b_tile, Board.board_rect[i - 1][j - 1])
                elif not is_odd(i):
                    if is_odd(j):
                        self.display_surf.blit(Board.b_tile, Board.board_rect[i - 1][j - 1])
                    else:
                        self.display_surf.blit(Board.w_tile, Board.board_rect[i - 1][j - 1])

    def update_pieces(self, fen):
        self.current_fen = fen
        self.display_board()
        self.draw_pieces(fen)

    def flip(self):
        self.flipped = not self.flipped
        self.update_pieces(self.current_fen)

    def create_piece(self, color, piece_type, position):
        piece = Piece(color, piece_type, self.display_surf)
        piece.set_position(position)
        return piece

    def create_piece_for_side(self, board_piece, color, position):
        if board_piece == 'b':
            piece = self.create_piece(color, PieceType.BISHOP, position)
            self.piece_rect.append(piece)

        if board_piece == 'k':
            piece = self.create_piece(color, PieceType.KING, position)
            self.piece_rect.append(piece)

        if board_piece == 'n':
            piece = self.create_piece(color, PieceType.KNIGHT, position)
            self.piece_rect.append(piece)

        if board_piece == 'p':
            piece = self.create_piece(color, PieceType.PAWN, position)
            self.piece_rect.append(piece)

        if board_piece == 'q':
            piece = self.create_piece(color, PieceType.QUEEN, position)
            self.piece_rect.append(piece)

        if board_piece == 'r':
            piece = self.create_piece(color, PieceType.ROOK, position)
            self.piece_rect.append(piece)

    def parse_fen(self, fen):
        return self.fp.parse(fen)

    def draw_pieces(self, fen):
        self.piece_rect = []
        fen_board = self.fp.parse(fen)

        if self.flipped:
            fen_board.reverse()
            fen_board = list(map(lambda x: x[::-1], fen_board))

        for i in range(len(fen_board)):
            for j in range(len(fen_board[i])):
                if fen_board[i][j].isupper():
                    self.create_piece_for_side(fen_board[i][j].lower(), PieceColor.WHITE, Board.board_rect[i][j])

                if fen_board[i][j].islower():
                    self.create_piece_for_side(fen_board[i][j], PieceColor.BLACK, Board.board_rect[i][j])

        for piece in self.piece_rect:
            piece.display_piece()


class Color:
    WHITE = (255, 255, 255)
    ASH = (50, 50, 50)
    BLACK = (0, 0, 0)
