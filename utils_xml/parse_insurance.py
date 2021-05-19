# %%

from lxml import etree
from pathlib import Path
# %%
src_fld = "c:/tmp"
#src_file = "CALCULATEINSURANCES_Response.xml"
src_file = "CALCULATEINSURANCES_Response_DcM.xml"
#src_file = "CALCULATE_Response.xml"

src_path = Path(src_fld) / src_file
#src_path_str = src_fld + "/" + src_file




# %%
def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8  windows-1250
        tree = etree.parse(fp)
    root = tree.getroot()
    return root

root = get_root(src_path)    
# %%

      
insurances_offer = root.find(".//InsurancesOffer") 

for insurances in insurances_offer:
    zp = insurances.find("./Insurance[@TypeCode='ZAK_POJ']")
    hp = insurances.find("./Insurance[@TypeCode='KAS_POJ']")
    jmeno_kampane_zp = zp.xpath("./VariableItems/Item[@TypeCode='KAMPAN_POJ']/@ItemText")
    jmeno_kampane_hp = hp.xpath("./VariableItems/Item[@TypeCode='KAMPAN_POJ']/@ItemText")

    modulis_dotaz = insurances.xpath('./RawData/Modulis/Dotaz/text()')
    modulis_vypocteno = insurances.xpath('./RawData/Modulis/Vypocteno/text()')
    
    print(insurances)
    print(jmeno_kampane_zp)
    print(jmeno_kampane_hp)
    #print(modulis_dotaz)
    #print(modulis_vypocteno)

    

# %%
