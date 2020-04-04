"""  xxx """
from lxml import etree

os_type = "Win" # Win | Linux


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
        # elems_to_insert = []
        # annotations_to_insert = []
        for documentation in documentations:
            att = documentation.attrib
            if att.get(xml_lang, None) in ["cs", "en", "sk"]:
                # print(documentation.text)
                pass

            elif att.get(xml_lang, None) is None:
                txt = documentation.text
                # comment = etree.Comment(txt)
                # annotations_to_insert.append(txt)

                # annotation.insert(0, comment)
                # documentation.getparent().remove(documentation)
                # print("delelted: " + str(txt))
        text_to_append_raw = "<xs:documentation><!-- " + txt + "-->\r</xs:documentation>"
        text_to_append = etree.XML(text_to_append_raw)        
        annotation.append(text_to_append)


    #tree.write(open('output.xml', 'wb'))
    tree.write(open(f_name_out, 'wb'), encoding='utf-8', xml_declaration=True, pretty_print=True)

def reformat():
    """ přidej odřádkování za '-->'  """
    if os_type == "Linux":
        with open('output.xml') as f:
            read_data = f.read()

        write_data = read_data.replace("--><", "-->\r<")

        with open("output_ref.xml", "w") as wf:
            wf.write(write_data)
    elif os_type == "Win":
        # zatím nefunguje
        pass

main()
reformat()
