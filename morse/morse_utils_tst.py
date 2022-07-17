import pytest

from morse_utils import Morse

# fmt: off
txt_message_1 = "Dog"
morse_message_1 = ['-..', '---', '--.']
message_duration_1 = 33

txt_message_2 = "Paris is nice" 
morse_message_2 = ['.--.', '.-', '.-.', '..', '...', '/', '..', '...', '/', '-.', '..', '-.-.', '.']
message_duration_2 = 97

# the first public morse message
txt_message_3 = "What hath God wrought" 
morse_message_3 = ['.--', '....', '.-', '-', '/', '....', '.-', '-', '....', '/', '--.', '---', '-..', '/', '.--', '.-.', '---', '..-', '--.', '....', '-']
message_duration_3 = 189

txt_message_4 = "fill*in&symbol"
morse_message_4 = ['..-.', '..', '.-..', '.-..', '.-.-.-', '..', '-.', '.-.-.-', '...', '-.--', '--', '-...', '---', '.-..']
message_duration_4 = 165
# fmt: on


@pytest.mark.parametrize(
    "txt_message, expected",
    [
        (txt_message_1, morse_message_1),
        (txt_message_2, morse_message_2),
        (txt_message_3, morse_message_3),
        (txt_message_4, morse_message_4),  # fill in symbol
    ],
)
def test_txt_to_morse(txt_message, expected):
    assert Morse.txt_to_morse(txt_message) == expected


@pytest.mark.parametrize(
    "morse_message, expected_raw",
    [
        (morse_message_1, txt_message_1),
        (morse_message_2, txt_message_2),
        (morse_message_3, txt_message_3),
        (["--.", "*", "-&-", "-..", "%."], "G..D."),  # fill in char
    ],
)
def test_morse_to_txt(morse_message, expected_raw):
    assert Morse.morse_to_txt(morse_message) == expected_raw.upper()


@pytest.mark.parametrize(
    "symbol, expected",
    [
        (".", 1),
        ("-", 3),
        (".-", 5),
        ("-...", 9),
        ("-.-.", 11),
        ("...", 5),
        ("---", 11),
        ("/", 1),  # word separator "/" is treated as a symbol
        # total length  symbol_pause + word_pause + symbol_pause = 7
    ],
)
def test_symbol_duration(symbol, expected):
    assert Morse.symbol_duration(symbol) == expected


@pytest.mark.parametrize(
    "morse_message, expected",
    [
        (morse_message_1, message_duration_1),
        (morse_message_2, message_duration_2),
        (morse_message_3, message_duration_3),
        (morse_message_4, message_duration_4),
    ],
)
def test_message_duration(morse_message, expected):
    assert Morse.message_duration(morse_message) == expected
