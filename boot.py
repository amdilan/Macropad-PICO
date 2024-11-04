import board
from kmk.bootcfg import bootcfg

bootcfg(
    # required:
    sense = board.GP6,
    source= board.GP21,
    # optional:,
    cdc_console=True,
    consumer_control=True,
    keyboard=True,
    midi=False,
    mouse=True,
    nkro=False,
    pan=False,
    storage=False,
    usb_id=('KMK Keyboard',),
)
