#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:36:29 2017 

@author: mh70
"""

from lxml import etree

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

def indent_element(e, ind):
    if len(e) > 0:
        e.text = "\n" + ind * " "
        for idx, e1 in enumerate(e):
            if idx + 1 < len(e):
                e1.tail = "\n" + (ind ) * " "
                indent_element(e1, ind + 2)
            else:
                e1.tail = "\n" + (ind - 2) * " "
                indent_element(e1, ind + 2)
    
    

tree = etree.fromstring(data)
tree.text = "\n  "

for idx, e in enumerate(tree):
    if idx + 1 < len(tree):        
        e.tail = "\n  "
    else:
        e.tail = "\n"
        
    if len(e) > 0:
        indent_element(e, 4)
                

tree_out = etree.tostring(tree, method="html", encoding="utf-8")

tree_out_dec = tree_out.decode("utf-8") #kovnertuj "bin string" do čitelného stringu
print(tree_out_dec)