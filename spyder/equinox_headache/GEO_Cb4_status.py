# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:01:59 2017

@author: mh70
"""


import requests
import xml.etree.ElementTree as ET
import uuid
import GEO_Cb4_common

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def replace_uuid_short(docum, string_to_replace):
    """V textu docum nahrad uuid,
    V pripade multiplicity left_string se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    uuid_str = uuid_str.replace("-", "")
    new_docum = docum.replace(string_to_replace, uuid_str)

    return new_docum

def batch_status(batch_id, url, host, authorization):
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cb4="http://cb4.creditinfosolutions.com/">
       <soapenv:Header/>
       <soapenv:Body>
          <cb4:BatchResponseStatus>
             <cb4:id>$batch_id</cb4:id>
          </cb4:BatchResponseStatus>
       </soapenv:Body>
    </soapenv:Envelope>
    """
    
    
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': '"http://cb4.creditinfosolutions.com/BatchResponseStatus"',
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
    
    
    body_new = body.replace("$batch_id", str(batch_id))
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    if response.status_code != 200:
        return ("response_error", None)
    
    tree = ET.fromstring(response.text)
    
    x  = tree.find('.//{' + ns_response + '}' + "State")
    if x is None:
        return ("response_error", None)
    
    state = x.text
    if not state == "Finished":
        return (state, None)
    
    response_info = tree.find('.//{' + ns_response + '}' + "ResponseInfo")
    ri_id = response_info.find('{' + ns_response + '}' + 'Id').text
    
    GEO_Cb4_common.wrt_f(label = 'batch check status request header',
                     msg = str(headers))
    GEO_Cb4_common.wrt_f(label = 'batch check status request', msg = body_new)
    GEO_Cb4_common.wrt_f(label = 'batch check status response',
                             msg = response.text)
    
    return (state, ri_id)
