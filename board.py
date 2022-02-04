import os
import pygame

from constants import IMAGE_DIR
from pieces import Piece, PieceColor, PieceType
from fenparser import FenParser
from utils import is_odd


class Board:
    a8, a7, a6, a5, a4, a3, a2, a1 = (100, 100), (100, 150), (100, 200), (100, 250), (100, 300), (100, 350), (100, 400), (100, 450)
    b8, b7, b6, b5, b4, b3, b2, b1 = (150, 100), (150, 150), (150, 200), (150, 250), (150, 300), (150, 350), (150, 400), (150, 450)
    c8, c7, c6, c5, c4, c3, c2, c1 = (200, 100), (200, 150), (200, 200), (200, 250), (200, 300), (200, 350), (200, 400), (200, 450)
    d8, d7, d6, d5, d4, d3, d2, d1 = (250, 100), (250, 150), (250, 200), (250, 250), (250, 300), (250, 350), (250, 400), (250, 450)
    e8, e7, e6, e5, e4, e3, e2, e1 = (300, 100), (300, 150), (300, 200), (300, 250), (300, 300), (300, 350), (300, 400), (300, 450)
    f8, f7, f6, f5, f4, f3, f2, f1 = (350, 100), (350, 150), (350, 200), (350, 250), (350, 300), (350, 350), (350, 400), (350, 450)
    g8, g7, g6, g5, g4, g3, g2, g1 = (400, 100), (400, 150), (400, 200), (400, 250), (400, 300), (400, 350), (400, 400), (400, 450)
    h8, h7, h6, h5, h4, h3, h2, h1 = (450, 100), (450, 150), (450, 200), (450, 250), (450, 300), (450, 350), (450, 400), (450, 450)

    pos_b = [a7, b7, c7, d7, e7, f7, g7, h7,
             a8, b8, c8, d8, e8, f8, g8, h8]

    pos_w = [a2, b2, c2, d2, e2, f2, g2, h2,
             a1, b1, c1, d1, e1, f1, g1, h1]

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

    def draw_pieces(self):
        self.map_pieces()

        for piece in self.piece_rect:
            piece.display_piece()

    def map_pieces(self):
        self.map_side(PieceColor.BLACK, Board.pos_b)
        self.map_side(PieceColor.WHITE, Board.pos_w)

    def map_side(self, side, pos):
        for i in range(len(pos)):
            if i in [0, 1, 2, 3, 4, 5, 6, 7]:
                piece = self.create_piece(side, PieceType.PAWN, Board.pos_b[i])
                self.piece_rect.append(piece)
            elif i in [8, 15]:
                piece = self.create_piece(side, PieceType.ROOK, Board.pos_b[i])
                self.piece_rect.append(piece)
            elif i in [9, 14]:
                piece = self.create_piece(side, PieceType.KNIGHT, Board.pos_b[i])
                self.piece_rect.append(piece)
            elif i in [10, 13]:
                piece = self.create_piece(side, PieceType.BISHOP, Board.pos_b[i])
                self.piece_rect.append(piece)
            elif i in [11]:
                piece = self.create_piece(side, PieceType.QUEEN, Board.pos_b[i])
                self.piece_rect.append(piece)
            elif i in [12]:
                piece = self.create_piece(side, PieceType.KING, Board.pos_b[i])
                self.piece_rect.append(piece)

    def create_piece(self, color, piece_type, position):
        piece = Piece(color, piece_type, self.display_surf)
        piece.set_position(position)
        return piece

    def update_pieces(self, fen):
        self.piece_rect = []
        fp = FenParser(fen)
        fen_board = fp.parse()

        for i in range(len(fen_board)):
            for j in range(len(fen_board[i])):
                if fen_board[i][j] in ['b', 'B']:
                    if fen_board[i][j] == 'b':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.BISHOP, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'B':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.BISHOP, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

                elif fen_board[i][j] in ['k', 'K']:
                    if fen_board[i][j] == 'k':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.KING, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'K':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.KING, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

                elif fen_board[i][j] in ['n', 'N']:
                    if fen_board[i][j] == 'n':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.KNIGHT, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'N':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.KNIGHT, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

                elif fen_board[i][j] in ['p', 'P']:
                    if fen_board[i][j] == 'p':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.PAWN, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'P':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.PAWN, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

                elif fen_board[i][j] in ['q', 'Q']:
                    if fen_board[i][j] == 'q':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.QUEEN, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'Q':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.QUEEN, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

                elif fen_board[i][j] in ['r', 'R']:
                    if fen_board[i][j] == 'r':
                        piece = self.create_piece(PieceColor.BLACK, PieceType.ROOK, Board.board_rect[i][j])
                        self.piece_rect.append(piece)
                    elif fen_board[i][j] == 'R':
                        piece = self.create_piece(PieceColor.WHITE, PieceType.ROOK, Board.board_rect[i][j])
                        self.piece_rect.append(piece)

        for piece in self.piece_rect:
            piece.display_piece()


class Color:
    WHITE = (255, 255, 255)
    ASH = (50, 50, 50)
    BLACK = (0, 0, 0)
