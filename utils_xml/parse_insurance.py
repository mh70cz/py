# %%

from lxml import etree
from pathlib import Path

# %%
src_fld = "c:/tmp/STEP2/SPO_Kred_Nove_Lexus"
# src_file = "CALCULATEINSURANCES_Response.xml"
src_file = "CALCULATEINSURANCES_Response_Error.xml"
# src_file = "CALCULATE_Response.xml"

src_path = Path(src_fld) / src_file
# src_path_str = src_fld + "/" + src_file

# %%

# recode win-1250 > utf-8

RECODE = True

if RECODE:
    stem = Path(src_file).stem
    suffix = Path(src_file).suffix
    dst_file_utf8 = Path(stem + "_utf8" + suffix)
    dst_path_utf8 = Path(src_fld) / dst_file_utf8

    with open(src_path, encoding="windows-1250") as reader:
        f = reader.read()

        f = f.replace("Windows-1250", "utf-8")
        # print (f)

        with open(
            dst_path_utf8,
            "w",
            encoding="utf-8",
        ) as writer:
            writer.write(f)

    src_path = dst_path_utf8

# %%


def get_root(path):
    with open(path, encoding="utf-8") as fp:  # utf-16le  utf-8  windows-1250
        tree = etree.parse(fp)
    root = tree.getroot()
    return root


root = get_root(src_path)
# %%

insurances_offer = root.find(".//InsurancesOffer")
if insurances_offer is not None:
    for insurances in insurances_offer:
        zp = insurances.find("./Insurance[@TypeCode='ZAK_POJ']")
        hp = insurances.find("./Insurance[@TypeCode='KAS_POJ']")
        jmeno_kampane_zp = zp.xpath(
            "./VariableItems/Item[@TypeCode='KAMPAN_POJ']/@ItemText"
        )
        jmeno_kampane_hp = hp.xpath(
            "./VariableItems/Item[@TypeCode='KAMPAN_POJ']/@ItemText"
        )

        modulis_dotaz = insurances.xpath("./RawData/Modulis/Dotaz/text()")
        modulis_vypocteno = insurances.xpath("./RawData/Modulis/Vypocteno/text()")

        print(insurances)
        print(jmeno_kampane_zp)
        print(jmeno_kampane_hp)
        # print(modulis_dotaz)
        # print(modulis_vypocteno)


# %%

debug_info = root.find("./Message/Response/DebugInfo")
if debug_info is not None:
    debug_modulis_dotaz_vypocet = debug_info.find("./DotazVypocet").text
    debug_modulis_response = debug_info.find("./Response").text


# %%
