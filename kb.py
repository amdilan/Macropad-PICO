import board # type: ignore

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.GP17,
        board.GP8,
        board.GP9,
        board.GP10,
        board.GP11,
        board.GP12,
        board.GP13,
        board.GP6,
    )
    
    row_pins = (
        board.GP21,
        board.GP20,
        board.GP19,
        board.GP18,
    )
    
    diode_orientation = DiodeOrientation.COL2ROW
    
    coord_mapping = [
         0,  1,  2,  3,  4,  5,  6,  7,
         8,  9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22,
        24, 25, 26, 27, 28, 29, 30
    ]