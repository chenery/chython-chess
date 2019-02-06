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

         board_list[row_index][column_index]

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

        self.captures = []

    def get_piece(self, at_square: Tuple[int, int]) -> Optional[piece.Piece]:
        """Return the piece found at this board square.

        :at_square Tuple[int, int]: where [int, int] refers to the row_index and the column index starting from zero.
        """
        return piece.build_piece(self._get_piece(at_square))

    def move(self, from_location: Tuple[int, int], to_location: Tuple[int, int]) -> None:
        """Move a piece from the from_location to the to_location

        Method assumes valid arguments. If no piece at from_location, method will silently end.
        """
        piece_at_from = self._get_piece(from_location)
        if piece_at_from:
            piece_at_to = self._get_piece(to_location)
            if piece_at_to:
                self.captures.append(piece_at_to)

            self.board_list[to_location[0]][to_location[1]] = piece_at_from

            # remove the piece that moved
            self.board_list[from_location[0]][from_location[1]] = None

    def get_captures(self) -> Tuple[Optional[piece.Piece]]:
        """Return a tuple of all the captures made on the board

        Tuple returned to provide an immutable collection for the caller.
        In future this method could provide the ability to filter by piece colour.

        Note: captures stored in memory as str rather than Piece object for memory saving.
        Decorated as piece objects when accessed through this method.
        """
        return tuple(map(lambda short_name: piece.build_piece(short_name), self.captures))

    def _get_piece(self, at_square: Tuple[int, int]) -> Optional[str]:
        """Return the piece short name or None found at this board square."""
        try:
            return self.board_list[at_square[0]][at_square[1]]
        except IndexError:
            return None


# 'Constants' for board squares/locations:
A_1 = 0, 0
A_2 = 1, 0
A_3 = 2, 0
A_4 = 3, 0
A_5 = 4, 0
A_6 = 5, 0
A_7 = 6, 0
A_8 = 7, 0

B_1 = 0, 1
B_2 = 1, 1
B_3 = 2, 1
B_4 = 3, 1
B_5 = 4, 1
B_6 = 5, 1
B_7 = 6, 1
B_8 = 7, 1

C_1 = 0, 2
C_2 = 1, 2
C_3 = 2, 2
C_4 = 3, 2
C_5 = 4, 2
C_6 = 5, 2
C_7 = 6, 2
C_8 = 7, 2

D_1 = 0, 3
D_2 = 1, 3
D_3 = 2, 3
D_4 = 3, 3
D_5 = 4, 3
D_6 = 5, 3
D_7 = 6, 3
D_8 = 7, 3

E_1 = 0, 4
E_2 = 1, 4
E_3 = 2, 4
E_4 = 3, 4
E_5 = 4, 4
E_6 = 5, 4
E_7 = 6, 4
E_8 = 7, 4

F_1 = 0, 5
F_2 = 1, 5
F_3 = 2, 5
F_4 = 3, 5
F_5 = 4, 5
F_6 = 5, 5
F_7 = 6, 5
F_8 = 7, 5

G_1 = 0, 6
G_2 = 1, 6
G_3 = 2, 6
G_4 = 3, 6
G_5 = 4, 6
G_6 = 5, 6
G_7 = 6, 6
G_8 = 7, 6

H_1 = 0, 7
H_2 = 1, 7
H_3 = 2, 7
H_4 = 3, 7
H_5 = 4, 7
H_6 = 5, 7
H_7 = 6, 7
H_8 = 7, 7



