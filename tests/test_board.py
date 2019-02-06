import unittest
import board
import piece


class BoardTest(unittest.TestCase):

    def test_get_piece_valid_existing_BK(self):
        # Given a new board
        chessboard = board.Board()
        # When get black king
        king = chessboard._get_piece(board.E_8)
        # Then king is returned
        self.assertEqual("BK", king)

    def test_get_piece_valid_existing_WR(self):
        # Given a new board
        chessboard = board.Board()
        # When get black king
        rook = chessboard._get_piece(board.A_1)
        # Then WR is returned
        self.assertEqual("WR", rook)

    def test_get_piece_valid_non_existent(self):
        # Given a new board
        chessboard = board.Board()
        # When get square with no piece
        king = chessboard._get_piece(board.A_4)
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
        king = chessboard.get_piece(board.E_8)
        # Then king object is returned
        self.assertEqual(piece.build_piece("BK"), king)

    def test_move_valid_move_no_capture(self):
        # Given a new board
        chessboard = board.Board()
        # When move a pawn
        chessboard.move(board.A_2, board.A_4)
        # Then pawn removed
        self.assertIsNone(chessboard.get_piece(board.A_2))
        # And pawn moved to
        self.assertEqual(piece.build_piece("WP"), chessboard.get_piece(board.A_4))

    def test_move_valid_move_capture(self):
        # Given a new board
        chessboard = board.Board()
        # When move a pawn to take BQ (no validation of moves in board module)
        chessboard.move(board.A_2, board.D_8)
        # Then pawn removed
        self.assertIsNone(chessboard.get_piece(board.A_2))
        # And pawn moved to
        self.assertEqual(piece.build_piece("WP"), chessboard.get_piece(board.D_8))
        # And BK captured by white
        captures = chessboard.get_captures()
        self.assertCountEqual([piece.build_piece("BQ")], captures)

    def test_move_invalid_move(self):
        # Given a new board
        chessboard = board.Board()
        # When the move has no piece on the from_location
        chessboard.move(board.A_3, board.A_4)
        # Then nothing happens
        self.assertIsNone(chessboard.get_piece(board.A_3))
        self.assertIsNone(chessboard.get_piece(board.A_4))
