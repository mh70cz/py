# MORSE CODE 
# tapped morese code message 
# signal: "." (aka dit) or "-" (aka dah)
# symbol: 
#     sequence of signals e.g. '.---'  (letter 'J')
#     word separator "/"
# morse message: sequence (list) of symbols 
# timing as of: https://morsecode.world/international/timing.html

import time
from get_dit_dah import get_tapped_dit_dah
from pydub.playback import play



MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/",
}


MORSE_DURATION_DICT = {
    ".": 1,  # dit
    "-": 3,  # dah
    "signal_pause": 1,  # [dit|dah]-[dit|dah] pause
    "symbol_pause": 3, # symbol separator
    "word_pause": 1,  # word separator "/" is treated as a symbol
    # total length  symbol_pause + word_pause + symbol_pause = 7
}

DEFAULT_FILL_IN_SYMBOL = ".-.-.-"  # . (dot)

DIT_LENGTH = 200  # dit length in ms

def txt_to_morse(txt_message, fill_in_symbol=DEFAULT_FILL_IN_SYMBOL):
    """ 
    
    """
    txt = txt_message.upper()
    morse_message = [MORSE_CODE_DICT.get(c, fill_in_symbol) for c in txt]
    return morse_message


def message_duration(morse_message):
    """
    morse message relative duration
    """
    duration = 0
    symbol = morse_message[:1][0]
    duration += symbol_duration(symbol)
    for symbol in morse_message[1:]:
        duration += MORSE_DURATION_DICT["symbol_pause"]  
        duration += symbol_duration(symbol)
    return duration


def symbol_duration(symbol):
    """
    morse symbol relative duration
    """

    duration = 0
    if symbol == "/":
        duration += MORSE_DURATION_DICT["word_pause"]
    else:
        first_signal_in_symbol = True
        for signal in symbol:            
            if signal not in [".","-"]:
                raise ValueError(f"{signal} is wrong signal")
            duration += MORSE_DURATION_DICT[signal]
            if not first_signal_in_symbol:
                duration += MORSE_DURATION_DICT["signal_pause"]
            else:
                first_signal_in_symbol = False
    return duration


TAP_SOUND_FLDR = "C:/git/py/morse"
TAP_SOUND_FILE = "tap_200.wav"  # tap sound 200 ms (i.e. DIT_BASE_LENGTH) 
DIT_BASE_LENGTH = 200  # base and minimum dit length in ms


def tap_morse_message(morse_message):
    """
    tap morse message
    """

    symbol = morse_message[:1][0]
    tap_morse_symbol(symbol)
    for symbol in morse_message[1:]:
        time.sleep(MORSE_DURATION_DICT["symbol_pause"] * DIT_LENGTH/1000)
        tap_morse_symbol(symbol)

def tap_morse_symbol(symbol):
    """
    tap morse message
    """
    if symbol == "/":
        time.sleep((MORSE_DURATION_DICT["word_pause"] * DIT_LENGTH)/1000)
    else:
        first_signal_in_symbol = True
        for signal in symbol:
            if not first_signal_in_symbol:
                time.sleep(MORSE_DURATION_DICT["signal_pause"] * DIT_LENGTH /1000)
            else:
                first_signal_in_symbol = False
            if signal == ".":
                play(dit)                
                # print("play: ." )
            elif signal == "-":
                play(dah) 
                # print("play: -" )
            else:
                # pass # silently ignore a wrong input                  
                raise ValueError(f"{signal} is wrong signal")
            



dit, dah = get_tapped_dit_dah(DIT_LENGTH)
""" 
symbol = "-..." # letter B
tap_morse_symbol(symbol)
exit("explicit script termination")
"""
txt_message = "What hath God wrought" # first public morse message
# txt_message ="SOS"
morse_message = txt_to_morse(txt_message)
duration = message_duration(morse_message)
print (morse_message , duration)
tap_morse_message(morse_message)

""" 
exit("explicit script termination")
print(dit_length)
play(dit)
time.sleep(dit_length / 1000)
play(dah)
""" 

