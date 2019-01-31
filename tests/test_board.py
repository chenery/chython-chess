import unittest
import board

class BoardTest(unittest.TestCase):

    def test_printBoard(self):

        chessboard = board.Board()

        expectedBoardName = "Hardcoded board name"
        self.assertEqual(chessboard.getBoardName(), expectedBoardName)
        self.assertEqual(chessboard.boardName, expectedBoardName)

