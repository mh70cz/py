class Morse:
    

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
    def txt_to_morse(cls,txt_message, fill_in_symbol=DEFAULT_FILL_IN_SYMBOL):
        """ 
        
        """
        txt = txt_message.upper()
        morse_message = [cls.MORSE_CODE_DICT.get(c, fill_in_symbol) for c in txt]
        return morse_message

    @classmethod
    def morse_to_txt(cls, morse_message):
        pass

    @classmethod 
    def symbol_duration(cls, symbol):
        """
        relative duration of morse symbol 
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
    def message_duration(cls, morse_message):
        """
        relative duration of morse message
        """
        duration = 0
        symbol = morse_message[:1][0]
        duration += cls.symbol_duration(symbol)
        for symbol in morse_message[1:]:
            duration += cls.MORSE_TIMING_DICT["symbol_pause"]  
            duration += cls.symbol_duration(symbol)
        return duration        

txt_message = "What hath God wrought" # first public morse message
# txt_message ="SOS"

morse_message = Morse.txt_to_morse(txt_message)
duration = Morse.message_duration(morse_message)
print (morse_message , duration)        