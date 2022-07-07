# signal: "." or "-"
# symbol: sequence of signals e.g. letter 'J':'.---' and separators "/"
# timing as of: https://morsecode.world/international/timing.html

import time
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path


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
    "signal_pause": 1,  # dit/dah pause
    "symbol_pause": 3,
    "/": 7,  # word pause
}


def txt_to_morse(txt_message, fill_in_symbol=None):
    """ 
    
    """
    if fill_in_symbol is None:
        fill_in_symbol = ".-.-.-"  # . (dot)
    txt = txt_message.upper()
    morse_message = [MORSE_CODE_DICT.get(c, fill_in_symbol) for c in txt]
    return morse_message


def message_duration(morse_message):
    """
    gets relative morse message duration
    """
    duration = 0
    first_symbol_in_word = True
    for symbol in morse_message:
        if symbol == "/":
            duration += MORSE_DURATION_DICT["/"]
            # print(f"{symbol=} {duration=}")
            first_symbol_in_word = True
        else:
            if not first_symbol_in_word:
                duration += MORSE_DURATION_DICT["symbol_pause"]
                # print(f"{symbol=} {duration=}")
            else:
                # print(f"{symbol=} {duration=}")
                first_symbol_in_word = False

            first_signal_in_symbol = True
            for signal in symbol:
                duration += MORSE_DURATION_DICT[signal]
                if not first_signal_in_symbol:
                    duration += MORSE_DURATION_DICT["signal_pause"]
                    # print(f"{symbol=}  {signal=} {first_signal_in_symbol= } {duration=}")
                else:
                    # print(f"{symbol=}  {signal=} {first_signal_in_symbol= } {duration=}")
                    first_signal_in_symbol = False

    return duration


TAP_SOUND_FLDR = "C:/git/py/morse"
TAP_SOUND_FILE = "tap_200.wav"  # tap sound 200 ms (i.e. DIT_LENGTH) 
DIT_LENGTH = 200  # standard and minimum dit length in ms


def get_tapped_dit_dah(dit_length=DIT_LENGTH):
    folder = Path(TAP_SOUND_FLDR)
    src_path = folder / TAP_SOUND_FILE   # tap sound 200 ms (i.e. DIT_LENGTH) 

    tap = AudioSegment.from_file(src_path, format="wav")

    if dit_length < DIT_LENGTH:
        dit_length = DIT_LENGTH
        # TODO exception: tap_sound must be DIT_LENGTH
        # TODO exception: dit_length >= DIT_LENGTH

    if dit_length == DIT_LENGTH:
        dit = tap
        dah = tap * 3
    else:
        silence_len_dit = dit_length - DIT_LENGTH
        silence_len_dah_middle = 3 * (dit_length - DIT_LENGTH) // 4
        silence_len_dah_end = 3 * (dit_length - DIT_LENGTH) - (
            2 * silence_len_dah_middle
        )
        silence_dit = AudioSegment.silent(duration=silence_len_dit)
        silence_dah_middle = AudioSegment.silent(duration=silence_len_dah_middle)
        silence_dah_end = AudioSegment.silent(duration=silence_len_dah_end)
        dit = tap + silence_dit
        dah = (
            tap + silence_dah_middle + tap + silence_dah_middle + tap + silence_dah_end
        )
        # print(f"{silence_len_dit=} {silence_len_dah_middle=} {silence_len_dah_end=}")

    # print(f"{len(dit)=} , {len(dah)=}")

    # play(dit)
    # time.sleep(dit_length / 1000)
    # play(dah)
    # time.sleep(dit_length / 1000)
    # play(dit)

    return (dit, dah, dit_length)

txt_message = "What hath God wrought" # first morse message
# txt_message ="SOS"
morse_message = txt_to_morse(txt_message, fill_in_symbol=None)
duration = message_duration(morse_message)
print (morse_message , duration)

dit, dah, dit_length = get_tapped_dit_dah()

""" 
print(dit_length)
play(dit)
time.sleep(dit_length / 1000)
play(dah)
""" 


first_symbol_in_word = True
for symbol in morse_message:
    # print(f"{symbol=}")
    if not first_symbol_in_word:
        # print("going to sleep for the next symbol..." , end =" ")               
        time.sleep(MORSE_DURATION_DICT["symbol_pause"] * dit_length/1000)
        # print("... wake" , end =" ") 
    first_symbol_in_word = False
    if symbol == "/":
        time.sleep((MORSE_DURATION_DICT["/"] * dit_length)/1000)
        first_symbol_in_word = True
    else:
        # TODO check for presence of . or - only
        first_signal_in_symbol = True
        for signal in symbol:
            # print(f"{signal=}", end =" ")
            if not first_signal_in_symbol: 
                # print("going to sleep..." , end =" ")               
                time.sleep(MORSE_DURATION_DICT["signal_pause"] * dit_length /1000)
                # print("... wake" , end =" ")  
            first_signal_in_symbol = False
            if signal == ".":
                play(dit)                
                # print("play: ." )
            else:
                play(dah) 
                # print("play: -" )
               