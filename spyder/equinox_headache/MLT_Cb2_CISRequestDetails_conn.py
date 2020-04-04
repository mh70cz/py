# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:16:27 2017

@author: mh70

"""

import requests
import xml.etree.ElementTree as ET
import uuid

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# requests lib is built on top of urllib3, which has nothing to do with 
# the standard library’s urllib.request. 
# They are, however, both built on top of the standard library’s http.client. 

# https://stackoverflow.com/questions/27981545/  ? modern version of libraries:
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)




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



body = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Header>
     <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <wsse:UsernameToken>
           <wsse:Username>cis.admin</wsse:Username>
           <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Heslo123456</wsse:Password>
        </wsse:UsernameToken>
     </wsse:Security>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
     <Query xmlns="http://creditinfo.com/schemas/2012/09/MultiConnector">
        <request xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
           <MessageId>d98c9495-5dea-46a4-8f65-ecf0748a1108</MessageId>
           <RequestXml>
              <RequestXml xmlns="http://creditinfo.com/schemas/2012/09/MultiConnector/Messages/Request">
                 <connector id="96939647-d89f-40b8-a53c-f6f218365fe8">
                    <data id="62493823-3c62-4738-ade7-c37826705428">
                       <request xmlns="http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/MLT/Cb2/CISRequestDetails/Request">
						      <Idregno>514744M</Idregno>
                       </request>
                    </data>
                 </connector>
              </RequestXml>
           </RequestXml>
           <Timeout i:nil="true"/>
        </request>
     </Query>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""

url="https://cishd-mc-app01/Testing/MultiConnector.svc"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/schemas/2012/09/MultiConnector/MultiConnectorService/Query"',
           'Content-Length': str(len(body)),
           'Host': 'cishd-mc-app01',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None    
}

ns_response = "http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/MLT/Cb2/CISRequestDetails/Response"

elem_names = [
        ("idregno", "Idregno"),
        ("fullname", "FullName"),
        ("surname", "Surname"),
        ("othersurname", "OtherSurname"),
        ("name", "Name"),
        ("othername", "OtherName"),
        ("middlenames", "Middlenames"),
        ("address", "Address"),
        ("postcode", "Postcode"),
        ("city", "City"),
        ("YearOfBirth", "YearOfBirth"),
        ("Age", "Age"),
        ("reportdate", "ReportDate"),
        ("report_id", "ReportId")
        ]

response_conn_lst = list()

def map_elements(elem_name_src, elem_name_dst):
    #x = tree.find('.//' + elem_name_src)
    x = tree.find('.//{' + ns_response + '}' + elem_name_src)
    # 
    if not(type(x) == type(None)):
        response_row[elem_name_dst] = x.text

        

idregnos = [
        "514744M", "1000048M", "1000049M", "1000050M", "1000144M", "1000247M",
        "1000649M", "1000744M", "100169M", "10017G", "10026M", "100254M"
        ]
#idregnos = ["8936925"]

for idregno in idregnos:
        
    body_new = body.replace('<Idregno>514744M</Idregno>',
                            '<Idregno>' + idregno + '</Idregno>')
    
    body_new = replace_uuid(body_new, '<MessageId>')
    body_new = replace_uuid(body_new, '<data id="')
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    # verify=False is required for SSL if there is no certificate
    #print(response)    
    tree = ET.fromstring(response.text) 
    
    response_row = dict()
    
    for elem_name in elem_names:
        map_elements(elem_name[1], elem_name[1])
        
    response_conn_lst.append(response_row)




    

