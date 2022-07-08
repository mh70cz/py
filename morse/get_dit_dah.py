import time
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path


TAP_SOUND_FLDR = "C:/git/py/morse"
TAP_SOUND_FILE = "tap_200.wav"  # tap sound 200 ms 

def get_tapped_dit_dah(dit_len=None):
    """
    
    """
    folder = Path(TAP_SOUND_FLDR)
    src_path = folder / TAP_SOUND_FILE   

    tap = AudioSegment.from_file(src_path, format="wav")

    tap_len = len(tap)
    if dit_len is None:
        dit_len = tap_len

    if tap_len == dit_len:
        dit = tap
        dah = tap * 3
    elif tap_len < dit_len:
        silence_len_dit = dit_len - tap_len
        silence_len_dah_middle = 3 * (dit_len - tap_len) // 4
        silence_len_dah_end = 3 * (dit_len - tap_len) - (
            2 * silence_len_dah_middle
        )
        silence_dit = AudioSegment.silent(duration=silence_len_dit)
        silence_dah_middle = AudioSegment.silent(duration=silence_len_dah_middle)
        silence_dah_end = AudioSegment.silent(duration=silence_len_dah_end)
        dit = tap + silence_dit
        dah = (
            tap + silence_dah_middle + tap + silence_dah_middle + tap + silence_dah_end
        )
    else:
        pass
        raise NotImplementedError("Not implemented yet: tap_len > dit_len")

    return dit, dah

""" 
dit_len = 800
dit, dah = get_tapped_dit_dah(dit_len)
print(dit_len)
play(dit)
time.sleep(dit_len / 1000)
play(dah)
"""