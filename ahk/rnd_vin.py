import pathlib
from random import choice
from pathlib import Path

VINS = [
    "1FAHP35N98W293576",
    "1FTYR14V4XPA45478",
    "KM8SR4HF2FU064035",
    "WVWAB7AJ3BW054147",
    "5TDKK3DC4CS212300",
    "1GNSCAE01BR139140",
    "1GNSCBKC5FR140561",
    "1GKFK66U42J248738",
    "1HGFA16559L013534",
    "NMTBA3BE40R046913",
    "NMTBA3BE50R049593"
]

out_fld = Path("c:/tmp/ahk/")
out_pth = out_fld / "rnd_vin.txt"

rnd_vin = choice(VINS)

with open(out_pth, "w") as f:
    f.write(rnd_vin)
