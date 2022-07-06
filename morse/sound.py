import time
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path

folder = Path("C:/git/py/morse")
src_path = folder / "tap_200.wav"

tap = AudioSegment.from_file(src_path, format="wav")

DIT_LENGTH = 200
dit_length = 250


if dit_length == DIT_LENGTH:
    dit = tap
    dah = tap * 3
else:
    silence_len_dit = dit_length - DIT_LENGTH
    silence_len_dah_middle = 3 * (dit_length - DIT_LENGTH) // 4
    silence_len_dah_end = 3 * (dit_length - DIT_LENGTH) - (2 * silence_len_dah_middle)
    silence_dit = AudioSegment.silent(duration=silence_len_dit)
    silence_dah_middle = AudioSegment.silent(duration=silence_len_dah_middle)
    silence_dah_end = AudioSegment.silent(duration=silence_len_dah_end)
    dit = tap + silence_dit
    dah = tap + silence_dah_middle + tap + silence_dah_middle + tap + silence_dah_end
    print(f"{silence_len_dit=} {silence_len_dah_middle=} {silence_len_dah_end=}")

print(f"{len(dit)=} , {len(dah)=}")

play(dit)
time.sleep(dit_length / 1000)
play(dah)
time.sleep(dit_length / 1000)
play(dit)


def slice_and_export():
    src_path = folder / "tapping-on-glass-31920.wav"
    dst_path = folder / "tap_200.wav"
    sound = AudioSegment.from_file(src_path, format="wav")
    tap_slice = sound[600:800]
    tap_slice = tap_slice + 5
    file_handle = tap_slice.export(dst_path, format="wav")
