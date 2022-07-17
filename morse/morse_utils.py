class Morse:
    from typing import List  # 3.9+  remove import + replace List: -> list:

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

    DEFAULT_FILL_IN_SYMBOL = ".-.-.-"  # . (dot)

    MORSE_TIMING_DICT = {
        ".": 1,  # dit
        "-": 3,  # dah
        "signal_pause": 1,  # [dit|dah]-[dit|dah] pause
        "symbol_pause": 3,  # symbol separator
        "word_pause": 1,  # word separator "/" is treated as a symbol
        # total length  symbol_pause + word_pause + symbol_pause = 7
    }

    @classmethod   
    def txt_to_morse(cls,txt_message: str, fill_in_symbol=DEFAULT_FILL_IN_SYMBOL) -> List[str]:
        """ 
        
        """
        txt = txt_message.upper()
        morse_message = [cls.MORSE_CODE_DICT.get(c, fill_in_symbol) for c in txt]
        return morse_message

    @classmethod
    def morse_to_txt_for_else(cls, morse_message: List[str]):
        fill_in_symbol = "."
        txt_message = []
        for symbol in morse_message:            
            for k, v in cls.MORSE_CODE_DICT.items():
                if v == symbol:
                    txt_message.append(k)
                    break
            else:
                txt_message.append(fill_in_symbol)
        return "".join(txt_message)

    @classmethod
    def morse_to_txt(cls, morse_message: List[str]) -> str:
        rev_mc_dict = {v:k for k,v in cls.MORSE_CODE_DICT.items()}
        rev_fill_in_char = rev_mc_dict[cls.DEFAULT_FILL_IN_SYMBOL]
        txt_message = [rev_mc_dict.get(s, rev_fill_in_char) for s in morse_message ]
        return "".join(txt_message)

    @classmethod 
    def symbol_duration(cls, symbol: str) -> int:
        """
        relative duration of a morse symbol 
        """

        duration = 0
        if symbol == "/":
            duration += cls.MORSE_TIMING_DICT["word_pause"]
        else:
            first_signal_in_symbol = True
            for signal in symbol:            
                if signal not in [".","-"]:
                    raise ValueError(f"{signal} is a wrong signal")
                duration += cls.MORSE_TIMING_DICT[signal]
                if not first_signal_in_symbol:
                    duration += cls.MORSE_TIMING_DICT["signal_pause"]
                else:
                    first_signal_in_symbol = False
        return duration

    @classmethod 
    def message_duration(cls, morse_message: List[str]) -> int:
        """
        relative duration of a morse message
        """
        duration = 0
        symbol = morse_message[:1][0]
        duration += cls.symbol_duration(symbol)
        for symbol in morse_message[1:]:
            duration += cls.MORSE_TIMING_DICT["symbol_pause"]  
            duration += cls.symbol_duration(symbol)
        if morse_message[-1] == "/":
            # just showing respect to the 'test case' "PARIS "
            # https://morsecode.world/international/timing.html
            duration += cls.MORSE_TIMING_DICT["symbol_pause"]      
        return duration        

if __name__ == "__main__":
    from os import system
    # txt_message = "What hath God wrought" # the first public morse message
    # txt_message ="SOS"
    # txt_message = "Paris "
    # txt_message = "Paris is nice"
    #txt_message = "fill*in & symbol"
    txt_message = "dog"


    #system('cls')
    print(txt_message)

    morse_message = Morse.txt_to_morse(txt_message)
    duration = Morse.message_duration(morse_message)
    print (morse_message , duration)
    txt2_message = Morse.morse_to_txt(morse_message)      
    print(txt2_message)  

