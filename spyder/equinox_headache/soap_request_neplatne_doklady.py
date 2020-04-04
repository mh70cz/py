# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:16:27 2017

@author: mh70

nahrad skutecnym heslem
PasswordText"></wsse:Password>
"""

import requests
import uuid

def replace_uuid(docum, left_string):
    """V textu docum nahrad uuid,
    ktere se nachazi bezprostredne za left_string, nahodnym uuid.
    V pripade multiplicity left_string se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    uuid_len = 36
    position = docum.find(left_string) + len(left_string)
    new_docum = "".join(
        (docum[:position], uuid_str, docum[position + uuid_len: ])
        )

    return new_docum



body = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mu="http://creditinfo.com/schemas/2012/09/MultiConnector">
   <SOAP-ENV:Header>
      <wsse:Security SOAP-ENV:mustUnderstand="0" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
         <wsse:UsernameToken>
            <wsse:Username>cis.admin</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText"></wsse:Password>
         </wsse:UsernameToken>
      </wsse:Security>
   </SOAP-ENV:Header>
   <SOAP-ENV:Body>
      <mu:Query>
         <mu:request>
            <mu:MessageId>96939647-d89f-40b8-a53c-f6f218365fe1</mu:MessageId>
            <mu:RequestXml>
               <RequestXml xmlns="http://creditinfo.com/schemas/2012/09/MultiConnector/Messages/Request">
                  <connector id="ad2133ec-9576-48e8-a8c2-fa3a9eabf4fd" useCache="true">
                     <data id="96939647-d89f-40b8-a53c-f6f218365fe1">
                        <request xsi:schemaLocation="http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/OpCze/Request" xmlns="http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/OpCze/Request" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
                           <DocumentNumber>111111111AB</DocumentNumber>
                           <DocumentType>0</DocumentType>
                        </request>
                     </data>
                  </connector>
               </RequestXml>
            </mu:RequestXml>
         </mu:request>
      </mu:Query>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

url="http://cishd-mc-app01/Testing/MultiConnector.svc"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/schemas/2012/09/MultiConnector/MultiConnectorService/Query"',
           'Content-Length': str(len(body)),
           'Host': 'cishd-mc-app01',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None    
}

body_tmp = replace_uuid(body, '<mu:MessageId>')
body_new = replace_uuid(body_tmp, '<data id="')

response = requests.post(url,data=body_new,headers=headers)
print(response)


"""
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/schemas/2012/09/MultiConnector/MultiConnectorService/Query"',
           'Content-Length': str(len(body)),
           'Host': 'cishd-mc-app01',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None
}
"""