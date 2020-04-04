# -*- coding: utf-8 -*-
"""
panagrams
unicodedata.normalize('NFKD'...
unicodedata.normalize('NFD' ...
"""

import unicodedata
pangram_cz = "Příliš žluťoučký kůň úpěl ďábelské ódy." # (All the non-ASCII letters of the Czech alphabet )
pangram_sk = "Vypätá dcéra grófa Maxwella s IQ nižším ako kôň núti čeľaď hrýzť hŕbu jabĺk."
pangram_de = "Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deic."
pangram_pl = "Mężny bądź, chroń pułk twój i sześć flag."
pangram_hu = "Jó foxim és don Quijote húszwattos lámpánál ülve egy pár bűvös cipőt készít."
# Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu. (All 42 letters of the Czech alphabet)

unicodedata.normalize('NFD', pangram_cz).encode('ascii','ignore')
unicodedata.normalize('NFD', pangram_sk).encode('ascii','ignore')
_pangram_de = pangram_de.replace("ß", "ss")
unicodedata.normalize('NFD', _pangram_de).encode('ascii','ignore')
_pangram_pl = pangram_pl.replace("ł","l")
unicodedata.normalize('NFD', _pangram_pl).encode('ascii','ignore')
unicodedata.normalize('NFD', pangram_hu).encode('ascii','ignore')

# unicodedata.normalize('NFKD', string_to_normalize).encode('ascii','ignore')
# unicodedata.normalize('NFD', string_to_normalize).encode('ascii','ignore')

# out_b = unicodedata.normalize('NFD', pangram_cz).encode('ascii','ignore')
# out = out_b.decode("ascii")
