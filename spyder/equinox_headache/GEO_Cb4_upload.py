# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:10:56 2017

@author: mh70
"""

import requests
import xml.etree.ElementTree as ET
import uuid
import GEO_Cb4_common
from GEO_Cb4_common import MyBusinessException

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#class MyBusinessException(Exception):
#    pass

def replace_uuid_short(docum, string_to_replace):
    """V textu docum nahrad uuid,
    V pripade multiplicity se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    uuid_str = uuid_str.replace("-", "")
    new_docum = docum.replace(string_to_replace, uuid_str)

    return new_docum

def upload(national_id, url, host, authorization):

    body = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><BatchUpload xmlns="http://cb4.creditinfosolutions.com/"><data><Batch xmlns="http://cb4.creditinfosolutions.com/BatchUploader/Batch">           
        <Header>
            <!-- <Identifier> #NGUID# (guid without "-") </Identifier> -->
            <Identifier>$ident1</Identifier>
            
            <Subscriber>AdminSubscriber</Subscriber>
            <SubscriberUnit>AdminSubscriberUnit</SubscriberUnit>
        </Header>
        <Commands>
            <Command identifier="$ident2">
                <Cis.CB4.Projects.GE.CIG.Reports.Body.Products.PersonalInformation>
                    <NationalID>$national_id</NationalID>
                </Cis.CB4.Projects.GE.CIG.Reports.Body.Products.PersonalInformation>
            </Command>
        </Commands>
    </Batch></data></BatchUpload></soap:Body></soap:Envelope>
    """
    
    
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': '"http://cb4.creditinfosolutions.com/BatchUpload"',
               'Content-Length': str(len(body)),
               'Host': 'getest.creditinfosolutions.com',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
               'Authorization': 'Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE=',
               'Accept': None
               }
    
    headers['Host'] = host
    headers['Authorization'] = authorization
    #url="https://getest.creditinfosolutions.com/WebService/Service.asmx"
    
    ns_response = "http://cb4.creditinfosolutions.com/BatchUploader/Batch"
    
    batch_id = "" #BatchId
    
    
    
    body_new = replace_uuid_short(body, "$ident1") #Identifier
    body_new = replace_uuid_short(body_new, "$ident2") #Command identifier
    body_new = body_new.replace("$national_id", str(national_id)) 

    try:    
        response = requests.post(url,data=body_new, headers=headers, verify=False)    
        if response.status_code != 200:
            raise MyBusinessException("Wrong/No response when uploading a batch")
        
        tree = ET.fromstring(response.text)
        
        x  = tree.find('.//{' + ns_response + '}' + "BatchId")
        if x is None:
            raise MyBusinessException("Wrong response when uploading a batch")
        batch_id = x.text
        
        GEO_Cb4_common.wrt_f(label = 'batch upload request header',
                             msg = str(headers))
        GEO_Cb4_common.wrt_f(label = 'batch upload request', msg = body_new)
        GEO_Cb4_common.wrt_f(label = 'batch upload response',
                             msg = response.text)
        
        return batch_id

    except MyBusinessException as e:
        #print(e)
        raise

