"""  konvertuje obsah elemntů xs:documentation bez xml:lang do komentářů """
from lxml import etree

f_name_in = "TradeRegisterListRequest_orig.xsd"
f_name_out = "TradeRegisterListRequest.xsd"

def main():
    tree = etree.parse(f_name_in)
    root = tree.getroot()
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema',}
    annotations = root.findall(".//xs:annotation", namespaces)
    xml_lang = '{http://www.w3.org/XML/1998/namespace}lang'

    for annotation in annotations:
        documentations = annotation.findall("./xs:documentation", namespaces)
        for documentation in documentations:
            att = documentation.attrib
            if att.get(xml_lang, None) in ["cs", "en", "sk"]:
                # print(documentation.text)
                pass

            elif att.get(xml_lang, None) is None:
                txt = documentation.text
                comment = etree.Comment(txt)
                documentation.getparent().remove(documentation)
                # print("delelted: " + str(txt))
                #annotation.insert(0, comment)
                annotation.append(comment)

    rough_bin_string = etree.tostring(root, encoding="utf-8",
                                      xml_declaration=True, pretty_print=True)

    format_xml(rough_bin_string)

    # with open(f_name_out, "wb") as wf:
    #     wf.write(rough_bin_string)
    #     #tree.write(open('output.xml', 'wb'))
    #tree.write(open(f_name_out, 'wb'), encoding='utf-8', xml_declaration=True, pretty_print=True)

def format_xml(xml_bin_string):
    """ přidání Comment elementu do xs:annotation nepřidá nový řádek
    tato procedura doformátuje a zapíše do souboru"""
    output = ""
    lenght = 0
    s = xml_bin_string.decode("utf-8")
    s = s.replace("--><", "-->\n<")
    s = s.split("\n")
    for line in s:
        #print(line)
        if "<xs:annotation>" in line:
            lenght = len(line) - 15
        elif ("</xs:annotation>" in line) and (len(line) < 19):
            line = str(lenght * " ") + line
        output += line + "\n"
    with open(f_name_out, "w", encoding="utf-8") as wf:
        wf.write(output)

main()
