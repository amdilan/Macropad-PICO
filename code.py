print("Starting")

import board # type: ignore
from kb import KMKKeyboard
from kmk.modules.encoder import EncoderHandler

from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.tapdance import TapDance
from kmk.modules.holdtap import HoldTap

PICO = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()
macros = Macros()
holdtap = HoldTap()

tapdance = TapDance()
# tapdance.tap_time = 750
PICO.modules.append(tapdance)

PICO.extensions.append(MediaKeys())
PICO.modules.append(encoder_handler)
PICO.modules.append(layers)
PICO.modules.append(macros)
PICO.modules.append(holdtap)

encoder_handler.pins = (
    (board.GP2, board.GP3, None, True,), #Encoder 1
    (board.GP4, board.GP5, None, True,), #Encoder 2
)

# Filler keys
_______ = KC.TRNS
xxxxxxx = KC.NO

# Key Combination Sequence
WIN = KC.RGUI
ALT_TAB = KC.MACRO(
    Tap(KC.LALT(KC.TAB)),
)
WIN_D = KC.MACRO(
    Tap(WIN(KC.D)),
)
WIN_L = KC.MACRO(
    Tap(WIN(KC.L))
)
ALT_F4 = KC.MACRO(
    Tap(KC.LALT(KC.F4))
)
TSKMGR = KC.MACRO(
	Tap(KC.LCTRL(KC.LSHIFT(KC.ESC)))
)
SS = KC.MACRO(
    Tap(WIN(KC.PSCREEN))
)
ALT_L = KC.MACRO(
    Tap(KC.RALT(KC.LEFT))
)
ALT_U = KC.MACRO(
    Tap(KC.RALT(KC.UP))
)
ALT_R = KC.MACRO(
    Tap(KC.RALT(KC.RIGHT))
)
DKTP_L = KC.MACRO(
    Tap(WIN(KC.RCTRL(KC.LEFT)))
)
DSKTP_R = KC.MACRO(
    Tap(WIN(KC.RCTRL(KC.RIGHT)))
)
DSKTP_N = KC.MACRO(
    Tap(WIN(KC.RCTRL(KC.D)))
)
WIN_TAB = KC.MACRO(
    Tap(WIN(KC.TAB))
)
OBS_P = KC.MACRO(
    Tap(KC.LSHIFT(KC.LCTL(KC.KP_SLASH)))
)
OBS_START = KC.MACRO(
    Tap(KC.LSHIFT(KC.LCTL(KC.KP_ASTERISK)))
)
OBS_END = KC.MACRO(
    Tap(KC.LSHIFT(KC.LCTL(KC.KP_MINUS)))
)
WIN_E = KC.MACRO(
    Tap(WIN(KC.E))
)
OBS = KC.HT(
    OBS_START, 
    KC.F21, 
    tap_time=500
)

ENC2 = KC.TD(
    xxxxxxx,
    
)

PICO.keymap = [
    # Main Layer
    [
        WIN_E   ,   KC.F14  ,   KC.F15  ,   KC.F16  ,   KC.MPRV ,   KC.MPLY ,   KC.MNXT ,   ENC2,
        KC.F17  ,   KC.F18  ,   KC.F19  ,   KC.F20  ,   ALT_F4  ,   TSKMGR  ,   KC.F13  ,   KC.MUTE,
        SS      ,   ALT_TAB ,   WIN_D   ,   WIN_TAB ,   DKTP_L  ,   DSKTP_R ,   DSKTP_N ,     
        WIN_L   ,   OBS     ,   OBS_P   ,   OBS_END ,   ALT_L   ,   ALT_U   ,   ALT_R   ,
    ]
]

encoder_handler.map = [
    # Main Layer
    (    
        (KC.AUDIO_VOL_DOWN  , KC.AUDIO_VOL_UP,),
        (KC.BRIGHTNESS_DOWN , KC.BRIGHTNESS_UP,),
    )   
]


if __name__ == '__main__':
    PICO.go()