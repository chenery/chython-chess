import unittest
import board
import piece


class BoardTest(unittest.TestCase):

    def test_get_piece_valid_existing(self):
        # Given a new board
        chessboard = board.Board()
        # When get black king
        king = chessboard._get_piece((7, 4))
        # Then king is returned
        self.assertEqual("BK", king)

    def test_get_piece_valid_non_existent(self):
        # Given a new board
        chessboard = board.Board()
        # When get square with no piece
        king = chessboard._get_piece((3, 0))
        self.assertIsNone(king)

    def test_get_piece_invalid_square(self):
        # Given a new board
        chessboard = board.Board()
        # When get called for out of range square
        king = chessboard._get_piece((9, 0))
        self.assertIsNone(king)

    def test_get_piece_object_valid_existing(self):
        # Given a new board
        chessboard = board.Board()
        # When get black king
        king = chessboard.get_piece((7, 4))
        # Then king object is returned
        self.assertEqual(piece.build_piece("BK"), king)
