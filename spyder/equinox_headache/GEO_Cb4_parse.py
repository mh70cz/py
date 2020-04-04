#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:18:27 2017

@author: mh70
"""

import base64
import zipfile
import io
import xml.etree.ElementTree as ET
from GEO_Cb4_common import MyBusinessException



#class MyBusinessException(Exception):
#    pass

def unzip_result_xml(batch_response_chunk_result):
    buffer = base64.b64decode(batch_response_chunk_result)
    z = zipfile.ZipFile(io.BytesIO(buffer))
    out = z.read(z.infolist()[0]) # Reads the data from the first file
    z.close()
    
    xml_txt = out.decode(encoding="utf-8")
    return xml_txt

def parse_result(xml_txt):
    tree = ET.fromstring(xml_txt)
        
    ns_response =  "http://cb4.creditinfosolutions.com/BatchUploader/Batch"

    #//Commands/Command/ReportStatus
    
    command = tree.find('.//{' + ns_response + '}' + "Commands" +
                        '/{' + ns_response + '}' + "Command")
    
    report_status = command.find('.//{' + ns_response + '}' + "ReportStatus")
    
    #try:
    if report_status.text == "ReportStatus.DataNotFound":
        raise MyBusinessException("Subject not found")
    if report_status.text != "ReportStatus.Ok":
        raise MyBusinessException("Wrong ReportStatus")

    personal_data = tree.find('.//{' + ns_response + '}' + "PersonalData")    
    personal_data_parts = [("Firstname", "Name"),
                           ("Surname", "Surname"),
                           ("Gender", "Gender"),
                           ("BirthDate", "DateOfBirth")
                           ]
    result = dict()
    for pdp in personal_data_parts:
        pdp_element = personal_data.find('.//{' + ns_response + '}' + pdp[0])
        if pdp_element is None:
            break
        result[pdp[1]] = pdp_element.text
    
    
    addresses = tree.find('.//{' + ns_response + '}' + "Addresses")
    
    address_types = ["PermanentResidence", "Factual", "Postal"]
    address_parts = ["Country", "City", "Street", "PostalCode"]
    out_address = dict()
    for at in address_types:
        at_element = addresses.find('.//{' + ns_response + '}' + at)
        if at_element is None:
            break
        out_sub_address = dict()
        for ap in address_parts:
            elem = at_element.find('.//{' + ns_response + '}' + ap)
            if elem is None:
                break
            out_sub_address[ap] = elem.text
        out_address[at] = out_sub_address
    result["Addresses"] = out_address
    
        
    phone_elem = tree.find('.//{' + ns_response + '}' + "Contacts" +
                      '/{' + ns_response + '}' + "Phone")
    cell_phone_elem = tree.find('.//{' + ns_response + '}' + "Contacts" +
                      '/{' + ns_response + '}' + "CellPhone")
    if not phone_elem is None:
        result["Phone"] = phone_elem.text
    if not cell_phone_elem is None:
        result["CellPhone"]  = cell_phone_elem.text
        
    return result
      

#    except MyBusinessException as e:
#        print(e)
#        #return None
#        raise
