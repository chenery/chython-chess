from typing import Optional
import re
from colour import Colour

short_name_pattern = re.compile("([W|B]){1}([R|N|Q|K|P]){1}")


class Piece:
    """A base class for all pieces that provides common behaviour."""

    def __init__(self, colour: Colour):
        self.colour = colour

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # todo abtract methods?


class King(Piece):

    def potential_moves(self):
        return None


class Queen(Piece):

    def potential_moves(self):
        return None


class Pawn(Piece):

    def potential_moves(self):
        return None


def build_piece(short_name: str) -> Optional[Piece]:
    """Factory method to build pieces based on short_name.

    Where short_name is of the form [W|B][R|N|Q|K|P]
    """
    if short_name is None:
        # Allow caller to supply None without raising an exception
        return None

    short_name_match = short_name_pattern.match(short_name)
    if short_name_match is None:
        raise ValueError("Invalid short_name: {0}. Use [W|B][R|N|Q|K|P].".format(short_name))

    colour_id = short_name_match.group(1)
    if colour_id == "W":
        colour = Colour.WHITE
    elif colour_id == "B":
        colour = Colour.BLACK
    else:
        raise ValueError("Invalid colour: {0}. Use W|B.".format(colour_id))

    piece_id = short_name_match.group(2)
    if piece_id == "K":
        return King(colour)
    elif piece_id == "Q":
        return Queen(colour)
    elif piece_id == "P":
        return Pawn(colour)
    else:
        raise ValueError("Invalid piece: {0}. Use [R|N|Q|K|P]".format(piece_id))
