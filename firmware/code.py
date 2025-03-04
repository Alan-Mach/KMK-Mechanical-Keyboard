print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP0, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.DEL, KC.INS, KC.F12, KC.F11, KC.F10, KC.F9, KC.F8, KC.F7, KC.F6, KC.F5, KC.F4, KC.F3, KC.F2, KC.F1, KC.ESC, KC.PSCR, KC.VOLU, KC.VOLD, KC.MUTE,
        KC.HOME, KC.BSPC, KC.EQL, KC.MINS, KC.N0, KC.N9, KC.N8, KC.N7, KC.N6, KC.N5, KC.N4, KC.N3, KC.N2, KC.N1, KC.GRV, KC.PMNS, KC.PAST, KC.PSLS, KC.NLCK,
        KC.END, KC.BSLS, KC.RBRC, KC.LBRC, KC.P, KC.O, KC.I, KC.U, KC.Y, KC.T, KC.R, KC.E, KC.W, KC.Q, KC.TAB, KC.PPLS, KC.P9, KC.P8, KC.P7,
        KC.PGUP, KC.ENT, KC.NO, KC.QUOT, KC.SCLN, KC.L, KC.K, KC.J, KC.H, KC.G, KC.F, KC.D, KC.S, KC.A, KC.CAPS, KC.NO, KC.P6, KC.P5, KC.P4,
        KC.PGDN, KC.UP, KC.RSFT, KC.SLSH, KC.DOT, KC.COMM, KC.M, KC.N, KC.NO, KC.B, KC.V, KC.C, KC.X, KC.Z, KC.LSFT, KC.PENT, KC.P3, KC.P2, KC.P1,
        KC.RGHT, KC.DOWN, KC.LEFT, KC.RCTL, KC.RALT, KC.NO, KC.NO, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.LALT, KC.LGUI, KC.LCTL, KC.NO, KC.PDOT, KC.NO, KC.P0
    ]
]

if __name__ == '__main__':
    keyboard.go()