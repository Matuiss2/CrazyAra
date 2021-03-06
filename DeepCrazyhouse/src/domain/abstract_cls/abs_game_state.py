"""
@file: _GameState.py
Created on 14.10.18
@project: crazy_ara_refactor
@author: queensgambit

Please describe what the content of this file is about
"""

from abc import ABC, abstractmethod
import chess.variant


class AbsGameState(ABC):
    """Abstract class for the GameState child class"""

    def __init__(self, board):
        self.board = board
        self._fen_dic = {}

    @abstractmethod
    def apply_move(self, move: chess.Move):  # , remember_state=False):
        """Force the child to implement apply_move method"""

    @abstractmethod
    def get_state_planes(self):
        """Force the child to implement get_state_planes method"""
        # return board_to_planes(self.board, 0, normalize=True)

    @abstractmethod
    def get_pythonchess_board(self):
        """ Force the child to implement get_pythonchess_board method"""

    def is_draw(self):
        """ Check if you can claim a draw - its assumed that the draw is always claimed """
        return self.board.can_claim_draw()

    @abstractmethod
    def is_won(self):
        """Force the child to implement is_won method"""

    def get_legal_moves(self):
        """ Find legal moves based on the board state"""
        return self.board.legal_moves

    @abstractmethod
    def is_white_to_move(self):
        """Force the child to implement is_white_to_move method"""

    def __str__(self):
        return self.board.fen()

    def get_board_fen(self):
        """ Create an identifier string for the board state"""
        return self.board.fen()

    def get_transposition_key(self):
        """
        Returns an identifier key for the current board state excluding move counters.
        Calling ._transposition_key() is faster than .fen()
        :return:
        """
        return self.board._transposition_key()  # protected member access(pylint error)

    @abstractmethod
    def new_game(self):
        """Force the child to implement new_game method"""

    def get_halfmove_counter(self):
        """ TODO: docstring """
        return self.board.halfmove_clock

    def get_fullmove_number(self):
        """ TODO: docstring """
        return self.board.fullmove_number
