import unittest
import piece
from colour import Colour


class PieceTest(unittest.TestCase):

    def test_build_piece_valid(self):
        black_king = piece.build_piece("BK")
        self.assertIsNotNone(black_king)
        self.assertEqual(Colour.BLACK, black_king.colour)
        self.assertIsInstance(black_king, piece.King)

    def test_build_piece_none_supplied(self):
        black_king = piece.build_piece(None)
        self.assertIsNone(black_king)

    def test_build_piece_invalid_colour(self):
        # WHEN call build_piece with invalid short_name "OK"
        self.assertRaises(ValueError, piece.build_piece, "OK")
