
# %%
# signal "." or "-"
# symbol sequence of signals e.g. letter 'J':'.---'

# TAP CODE
# signal "." or halfsymbol_separator " "
# symbol sequence of signals e.g. letter 'J': '.. .....',

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',
                    " ":"/"}
                    

MORSE_DURATION_DICT = {".": 1, 
               "-": 3,               
               "signal_pause": 1,
               "symbol_pause": 3,
               "/": 7, # word pause
                }
TAP_CODE_DICT = {'A': '. .',
 'B': '. ..',
 'C': '. ...',
 'K': '. ...',
 'D': '. ....',
 'E': '. .....',
 'F': '.. .',
 'G': '.. ..',
 'H': '.. ...',
 'I': '.. ....',
 'J': '.. .....',
 'L': '... .',
 'M': '... ..',
 'N': '... ...',
 'O': '... ....',
 'P': '... .....',
 'Q': '.... .',
 'R': '.... ..',
 'S': '.... ...',
 'T': '.... ....',
 'U': '.... .....',
 'V': '..... .',
 'W': '..... ..',
 'X': '..... ...',
 'Y': '..... ....',
 'Z': '..... .....',
  " ":"/"}


TAP_DURATION_DICT = {".": 1, 
               "signal_pause": 1, 
               " ": 2 , # halfsymbol_separator i.e. inner pause
               "symbol_pause": 4,
               "/": 7, # word pause
                }
# %%
def txt_to_morse(txt_message, surrogate_symbol = ".-.-.-"):
    # surrogate_symbol = ".-.-.-" # .
    txt = txt_message.upper()
    morse_message = [MORSE_CODE_DICT.get(c, surrogate_symbol) for c in txt]
    return(morse_message)


def morse_duration(morse_message):
    duration = 0
    first_symbol_in_word = True
    for symbol in morse_message:        
        if symbol == "/":
            duration += MORSE_DURATION_DICT['/']
            # print(f"{symbol=} {duration=}")
            first_symbol_in_word = True
        else:
            if not first_symbol_in_word:
                duration += MORSE_DURATION_DICT["symbol_pause"]  
                # print(f"{symbol=} {duration=}")  
            else:
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


def txt_to_tap(txt_message, surrogate_symbols = None):

    if surrogate_symbols is None:
        surrogate_symbols = ".... ./.... ..." #  QS
    txt = txt_message.upper()
    tap_message = [TAP_CODE_DICT.get(c, surrogate_symbols) for c in txt]
    return tap_message

def tap_duration(tap_message):
    duration = 0
    first_symbol_in_word = True
    for symbol in tap_message:
        if symbol == "/":
            duration += TAP_DURATION_DICT['/']
            print(f"{symbol=} {duration=}") 
            first_symbol_in_word = True
        else:
            if not first_symbol_in_word:
                duration += TAP_DURATION_DICT["symbol_pause"]  
                print(f"{symbol=} {duration=}")  
            else:
                print(f"{symbol=} {duration=}") 
                first_symbol_in_word = False     
            first_signal_in_halfsymbol = True
            for signal in symbol:
                if signal == " ":
                    duration += TAP_DURATION_DICT[' ']
                    print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    first_signal_in_halfsymbol = True
                else:
                    duration += TAP_DURATION_DICT['.']
                    if not first_signal_in_halfsymbol:
                        duration += TAP_DURATION_DICT['signal_pause']
                        print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    else:
                        print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                        first_signal_in_halfsymbol = False

    return(duration)    

# %%

#txt_message = "What hath God wrought"
txt_message = "PARIS is nice"
#txt_message = "NICE"
tap_message = txt_to_tap(txt_message)
tap_message_duration = tap_duration(tap_message)
print(tap_message)
print(tap_message_duration)



morse_message = txt_to_morse(txt_message)
morse_message_duration = morse_duration(morse_message)
print(morse_message)
print(morse_message_duration)

# %%
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

txt_message = "PARIS is nice"
txt_message = "PARIS "
tap_message = txt_to_tap(txt_message)
print (tap_message)

duration = 0
first_symbol_in_word = True
for symbol in tap_message:
    if symbol == "/":
        duration += TAP_DURATION_DICT['/']
        print(f"{symbol=} {duration=}") 
        first_symbol_in_word = True
    else:
        if not first_symbol_in_word:
            duration += TAP_DURATION_DICT["symbol_pause"]  
            print(f"{symbol=} {duration=}")  
        else:
            print(f"{symbol=} {duration=}") 
            first_symbol_in_word = False     
        first_signal_in_halfsymbol = True
        for signal in symbol:
            if signal == " ":
                duration += TAP_DURATION_DICT[' ']
                print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                first_signal_in_halfsymbol = True
            else:
                duration += TAP_DURATION_DICT['.']
                if not first_signal_in_halfsymbol:
                    duration += TAP_DURATION_DICT['signal_pause']
                    print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                else:
                    print(f"{symbol=}  {signal=} {first_signal_in_halfsymbol= } {duration=}")
                    first_signal_in_halfsymbol = False

print(duration)




               

# %%

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# %%
txt_message = "What hath God wrought"
surrogate_symbols = ".... ./.... ..." #  QS
txt = txt_message.upper()
tap_message = [TAP_CODE_DICT.get(c, surrogate_symbols) for c in txt]
tap_message
        
# %%
import string

string.ascii_uppercase

letters = [c for c in string.ascii_uppercase if c != "K"]

taps = []
for outer_dot in range(1,6):
    for inner_dot in range(1,6):
        taps.append (("." * outer_dot) + " " + ("." * inner_dot))



tap_code_dict = dict(zip(letters, taps))
tap_code_dict["K"] = tap_code_dict["C"]
tap_code_dict = dict(sorted(tap_code_dict.items(), key = lambda x:x[1] ))
tap_code_dict
# %%
[outer for outer in range(1,6)]
# %%
