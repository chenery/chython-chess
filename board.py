from typing import Tuple, Optional
import piece


class Board:

    """An list based implementation of a chess board.

    The list is 2 dimensional, we will insert character strings to represent pieces.
    """

    def __init__(self):
        """Create the board list as per:

         [row 1, row 2, row 3, ...]

         then insert the columns to achieve a row x column 2 dimensional list

         Direct access to board_list is then as per:

         board_list[row_index, column_index]

         """
        self.board_list = [
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"]]

    def get_piece(self, at_square: Tuple[int, int]) -> Optional[piece.Piece]:
        """Return the piece found at this board square.

        :at_square Tuple[int, int]: where [int, int] refers to the row_index and the column index starting from zero.
        """
        return piece.build_piece(self._get_piece(at_square))

    def _get_piece(self, at_square: Tuple[int, int]) -> Optional[str]:
        """Return the piece short name or None found at this board square."""
        try:
            return self.board_list[at_square[0]][at_square[1]]
        except IndexError:
            return None






