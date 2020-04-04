# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:27:20 2017

@author: m.houska
"""


from lxml import etree
#import xml.dom.minidom as minidom


data = """
<Entity>

                              <RegistryNumber>2509396399</RegistryNumber>
                              <FullName>Úlfar Kári Ryan Þórsson Fitzgerald</FullName>
                              <Alias/>
                              <IsIndividual>true</IsIndividual>
                              <IsCurrent>true</IsCurrent>
                              <IsValid>true</IsValid>
                              <IsOpen>true</IsOpen>
                              <LegalAddress>Þúsundáraafmælisgata 53</LegalAddress>
                              <LegalZipCode>110</LegalZipCode>
                              <LegalZone>Reykjavík</LegalZone>
                              <PostalAddress/>
                              <PostalZipCode/>
                              <PostalZone/>
                              <IsatCategory/>
                              <IsatName/>
                              <VatNumber/>
                              <LastStatusChange>2017-09-14T15:56:21.45</LastStatusChange>
                              <IsatList>
                                 <IsatItem>
                                    <IsatNumber>-</IsatNumber>
                                    <IsatName>-</IsatName>
                                    <IsMain>true</IsMain>
                                 </IsatItem>
                              </IsatList>
                              <VatList>
                                 <VatItem>
                                    <VatNumber>-</VatNumber>
                                    <IsatNumber>-</IsatNumber>
                                    <IsatName>-</IsatName>
                                    <IsOpen>true</IsOpen>
                                    <IsMain>true</IsMain>
                                 </VatItem>
                              </VatList>




        
</Entity>
"""





tree = etree.fromstring(data)

tree.text = "\n  "

for idx, e in enumerate(tree):
    if idx + 1 < len(tree):        
        e.tail = "\n  "
    else:
        e.tail = "\n"
    if len(e) > 0:
        e.text = "\n    "
        for idx, e1 in enumerate(e):
            if idx + 1 < len(e):
                e1.tail = "\n    "
                if len(e1) > 0:
                    e1.text = "\n      "                    
                    for idx, e2 in enumerate(e1):
                        if idx + 1 < len(e1):
                            e2.tail = "\n      "
                        else:
                            e2.tail = "\n    "
            else:
                e1.tail = "\n  "
                if len(e1) > 0:
                    e1.text = "\n      "
                    for idx, e2 in enumerate(e1):
                        if idx + 1 < len(e1):
                            e2.tail = "\n      "
                        else:
                            e2.tail = "\n    "
                

tree_out = etree.tostring(tree, method="html", encoding="utf-8")

tree_out_dec = tree_out.decode("utf-8") #kovnertuj "bin string" do čitelného stringu
print(tree_out_dec)

#with open("out.xml", "w", encoding="utf-8") as wf:
#    wf.write(tree_out_dec)

# prettyxml z xml.dom.minidom nefunguje uspokojivě
#tree_out_parse = minidom.parseString(tree_out)
#tree_out_pretty =  tree_out_parse.toprettyxml(indent=' ', newl='')
#print(tree_out_pretty)