# TAP CODE
# signal: "."
# halfsymbol: sequence of signals min 1 max 5
# symbol: 2 halfsymbols separated by " " e.g.  '.. .....' (letter 'J')
# tap message: sequence of symbols and separators "/"

import time
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

TAP_CODE_DICT = {
    "A": ". .",
    "B": ". ..",
    "C": ". ...",
    "K": ". ...",
    "D": ". ....",
    "E": ". .....",
    "F": ".. .",
    "G": ".. ..",
    "H": ".. ...",
    "I": ".. ....",
    "J": ".. .....",
    "L": "... .",
    "M": "... ..",
    "N": "... ...",
    "O": "... ....",
    "P": "... .....",
    "Q": ".... .",
    "R": ".... ..",
    "S": ".... ...",
    "T": ".... ....",
    "U": ".... .....",
    "V": "..... .",
    "W": "..... ..",
    "X": "..... ...",
    "Y": "..... ....",
    "Z": "..... .....",
    " ": "/",
}

TAP_DURATION_DICT = {
    ".": 1,
    "signal_pause": 1, 
    " ": 2,  # halfsymbol_separator i.e. inner pause
    "symbol_pause": 4,
    "/": 7,  # word pause
}

DEFAULT_FILL_IN_SYMBOL = "..... ....."  # letter Z


def txt_to_tap(txt_message, fill_in_symbol=DEFAULT_FILL_IN_SYMBOL):
    """
    TODO
    """
    txt = txt_message.upper()
    tap_message = [TAP_CODE_DICT.get(c, fill_in_symbol) for c in txt]
    return tap_message


def tap_duration(tap_message):
    duration = 0
    first_symbol_in_word = True
    for symbol in tap_message:
        if symbol == "/":
            duration += TAP_DURATION_DICT["/"]
            # print(f"{symbol=} {duration=}")
            first_symbol_in_word = True
        else:
            if not first_symbol_in_word:
                duration += TAP_DURATION_DICT["symbol_pause"]
                # print(f"{symbol=} {duration=}")
            else:
                # print(f"{symbol=} {duration=}")
                first_symbol_in_word = False
            first_signal_in_halfsymbol = True
            for signal in symbol:
                if signal == " ":
                    duration += TAP_DURATION_DICT[" "]
                    # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    first_signal_in_halfsymbol = True
                else:
                    duration += TAP_DURATION_DICT["."]
                    if not first_signal_in_halfsymbol:
                        duration += TAP_DURATION_DICT["signal_pause"]
                        # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    else:
                        # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                        first_signal_in_halfsymbol = False

    return duration


TAP_SOUND_FLDR = "C:/git/py/morse"
TAP_SOUND_FILE = "tap_200.wav"  # tap sound 200 ms (i.e. TAP_LENGTH) 
TAP_LENGTH = 200  # tap length in ms

def message_duration(tap_message):
    """
    relative tap message duration
    """
    duration = 0
    first_symbol_in_word = True
    for symbol in tap_message:
        if symbol == "/":
            duration += TAP_DURATION_DICT['/']
            # print(f"{symbol=} {dusurrogatetap morration=}") 
            first_symbol_in_word = True
        else:
            if not first_symbol_in_word:
                duration += TAP_DURATION_DICT["symbol_pause"]  
                # print(f"{symbol=} {duration=}")  
            else:
                # print(f"{symbol=} {duration=}") 
                first_symbol_in_word = False     
            first_signal_in_halfsymbol = True
            for signal in symbol:
                if signal == " ":
                    duration += TAP_DURATION_DICT[' ']
                    # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    first_signal_in_halfsymbol = True
                else:
                    duration += TAP_DURATION_DICT['.']
                    if not first_signal_in_halfsymbol:
                        duration += TAP_DURATION_DICT['signal_pause']
                        # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    else:
                        # print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                        first_signal_in_halfsymbol = False

    return(duration)  

TAP_SOUND_FLDR = "C:/git/py/morse"
TAP_SOUND_FILE = "tap_200.wav"  # tap sound 200 ms
folder = Path(TAP_SOUND_FLDR)
src_path = folder / TAP_SOUND_FILE  

tap = AudioSegment.from_file(src_path, format="wav")

txt_message = "What hath God wrought" # first public morse message
tap_message = txt_to_tap(txt_message)
duration = message_duration(tap_message)
print (tap_message , duration)

first_symbol_in_word = True
for symbol in tap_message:
    print(f"{symbol=}")
    if not first_symbol_in_word:
        print("going to sleep for the next symbol..." , end =" ")
        time.sleep(TAP_DURATION_DICT["symbol_pause"] * TAP_LENGTH / 1000)
        print("... wake" , end =" ") 
    first_symbol_in_word = False
    if symbol == "/":
        time.sleep(TAP_DURATION_DICT["/"] * TAP_LENGTH / 1000)
        first_symbol_in_word = True
    else:
        first_signal_in_halfsymbol = True
        for sigsep in symbol:  # sigsep: signal or separator
            if not first_signal_in_halfsymbol:
                time.sleep(TAP_DURATION_DICT["signal_pause"] * TAP_LENGTH / 1000)
            first_signal_in_halfsymbol = False
            if sigsep == " ":
                first_signal_in_halfsymbol = True
                time.sleep(TAP_DURATION_DICT[" "] * TAP_LENGTH / 1000)
            elif sigsep == ".":
                play(tap)
            else:
                pass # wrong input                
            
