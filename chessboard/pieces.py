import os
import pygame

from chessboard.constants import IMAGE_DIR


class PieceColor:
    BLACK = 'BLACK'
    WHITE = 'WHITE'


class PieceType:
    BISHOP = 'BISHOP'
    KING = 'KING'
    KNIGHT = 'KNIGHT'
    PAWN = 'PAWN'
    QUEEN = 'QUEEN'
    ROOK = 'ROOK'


class Piece:
    b_bishop = pygame.image.load(os.path.join(IMAGE_DIR, 'bB.png'))
    b_king = pygame.image.load(os.path.join(IMAGE_DIR, 'bK.png'))
    b_knight = pygame.image.load(os.path.join(IMAGE_DIR, 'bN.png'))
    b_pawn = pygame.image.load(os.path.join(IMAGE_DIR, 'bP.png'))
    b_queen = pygame.image.load(os.path.join(IMAGE_DIR, 'bQ.png'))
    b_rook = pygame.image.load(os.path.join(IMAGE_DIR, 'bR.png'))

    w_bishop = pygame.image.load(os.path.join(IMAGE_DIR, 'wB.png'))
    w_king = pygame.image.load(os.path.join(IMAGE_DIR, 'wK.png'))
    w_knight = pygame.image.load(os.path.join(IMAGE_DIR, 'wN.png'))
    w_pawn = pygame.image.load(os.path.join(IMAGE_DIR, 'wP.png'))
    w_queen = pygame.image.load(os.path.join(IMAGE_DIR, 'wQ.png'))
    w_rook = pygame.image.load(os.path.join(IMAGE_DIR, 'wR.png'))

    def __init__(self, color, piece, display_surf):
        self.position = None
        self.sprite = None
        self.display_surf = display_surf

        self.color = color
        self.piece = piece

        self.set_sprite()

    def set_position(self, position):
        self.position = position

    def set_sprite(self):
        if self.piece == PieceType.BISHOP:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_bishop
            elif self.color == PieceColor.WHITE:
                self.sprite = Piece.w_bishop

        elif self.piece == PieceType.KING:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_king
            elif self.color == PieceColor.WHITE:
                self.sprite = Piece.w_king

        elif self.piece == PieceType.KNIGHT:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_knight
            if self.color == PieceColor.WHITE:
                self.sprite = Piece.w_knight

        elif self.piece == PieceType.PAWN:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_pawn
            elif self.color == PieceColor.WHITE:
                self.sprite = Piece.w_pawn

        elif self.piece == PieceType.QUEEN:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_queen
            elif self.color == PieceColor.WHITE:
                self.sprite = Piece.w_queen

        elif self.piece == PieceType.ROOK:
            if self.color == PieceColor.BLACK:
                self.sprite = Piece.b_rook
            elif self.color == PieceColor.WHITE:
                self.sprite = Piece.w_rook

    def display_piece(self):
        self.display_surf.blit(self.sprite, self.position)
