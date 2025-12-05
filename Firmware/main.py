# main.py for Zura's HackPad
#
# Hardware (from KiCad netlist):
# - SW1 → GPIO26/ADC0/A0
# - SW2 → GPIO27/ADC1/A1
# - SW3 → GPIO28/ADC2/A2
# - SW4 → GPIO29/ADC3/A3
# - Encoder A → GPIO2/SCK
# - Encoder B → GPIO4/MISO
# - SK6812 DIN → GPIO0/TX
# - OLED SDA → GPIO6/SDA
# - OLED SCL → GPIO7/SCL

import board

from kmk.kmk_keyboard import KMKKeyboard          # Core KMK keyboard class
from kmk.scanners.keypad import KeysScanner      # Simple per-pin key scanner
from kmk.keys import KC                          # Keycodes (Ctrl, etc.)
from kmk.modules.encoder import EncoderHandler   # Rotary encoder support
from kmk.extensions.media_keys import MediaKeys  # Volume/media keys


# -----------------------------
# PIN ASSIGNMENTS (from netlist)
# -----------------------------

# Switches: SW1..SW4 -> A0..A3
PIN_KEY_CP  = board.A0  # SW1 -> GPIO26/ADC0/A0
PIN_KEY_FC  = board.A1  # SW2 -> GPIO27/ADC1/A1
PIN_KEY_OT  = board.A2  # SW3 -> GPIO28/ADC2/A2
PIN_KEY_LFN = board.A3  # SW4 -> GPIO29/ADC3/A3

# Rotary encoder A/B (no push switch wired)
PIN_ENC_A   = board.D8  # GPIO2/SCK
PIN_ENC_B   = board.D9  # GPIO4/MISO

# RGB LED data in (first SK6812 DIN)
PIN_RGB_DIN = board.D6  # GPIO0/TX

# OLED I2C (header J1)
PIN_OLED_SDA = board.SDA  # GPIO6/SDA
PIN_OLED_SCL = board.SCL  # GPIO7/SCL


# -----------------------------
# KMK keyboard setup
# -----------------------------

keyboard = KMKKeyboard()  # Create keyboard instance

# 1×4 matrix for the 4 switches (CP, FC, OT, LFN)
key_pins = (
    PIN_KEY_CP,
    PIN_KEY_FC,
    PIN_KEY_OT,
    PIN_KEY_LFN,
)

keyboard.matrix = KeysScanner(
    pins=key_pins,             # list of GPIOs for each key
    value_when_pressed=False,  # active-low (pins go to GND when pressed)
    pull=True,                 # enable internal pull-ups
)

# Add media keys + encoder support
keyboard.extensions.append(MediaKeys())     # enable KC.VOLU / KC.VOLD etc.
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)


# -----------------------------
# Encoder configuration
# -----------------------------

# One encoder: (A, B, switch_pin_or_None)
encoder_handler.pins = (
    (PIN_ENC_A, PIN_ENC_B, None),  # Only rotation, no switch
)

# Encoder map:
# For each layer, for each encoder: (CCW, CW)
# Layer 0, encoder 0 -> Volume Down / Volume Up
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),  # layer 0
    ),
]


# -----------------------------
# Keymap
# -----------------------------
# Key order in matrix: [CP, FC, OT, LFN]

# Common shortcuts
CP_COPY    = KC.LCTL(KC.C)              # Ctrl+C
CP_PASTE   = KC.LCTL(KC.V)              # Ctrl+V
NEW_FOLDER = KC.LCTL(KC.LSFT(KC.N))     # Ctrl+Shift+N (new folder)
OPEN_TERM  = KC.LCTL(KC.LALT(KC.T))     # Ctrl+Alt+T (Linux terminal)
FN_LOCK    = KC.F14                     # Fake Fn-lock key (map F14 in OS to toggle Fn)

# For now: CP key just does copy. Later we can implement stateful copy/paste toggling.
keyboard.keymap = [
    [
        CP_COPY,       # SW1 -> CP
        NEW_FOLDER,    # SW2 -> FC
        OPEN_TERM,     # SW3 -> OT
        FN_LOCK,       # SW4 -> LFN
    ]
]


# -----------------------------
# Run the keyboard
# -----------------------------

if __name__ == "__main__":
    keyboard.go()
