from typing import Any, List, Optional

VERTICAL = "│"
HORIZONTAL = "─"
TOP_LEFT = "┌"
TOP_MIDDLE = "┬"
TOP_RIGHT = "┐"
LEFT_MIDDLE = "├"
MIDDLE = "┼"
RIGHT_MIDDLE = "┤"
BOTTOM_LEFT = "└"
BOTTOM_MIDDLE = "┴"
BOTTOM_RIGHT = "┘"




#if centered: character is ^, else: <
def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    # find longest label/element in a column of list, save that number (for all columns, same length of list.list.size) and use it to format the table: {:<10s}{:>4s}   (the number is the number + some lee-way margin)
    # some number + 2 lee way action
    longest_elements = []

    return "we got this"