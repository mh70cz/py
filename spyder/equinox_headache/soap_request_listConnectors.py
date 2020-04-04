# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:23:39 2017

@author: mh70

nahrad skutecnym heslem
PasswordText"></wsse:Password>

"""

# -*- coding: utf-8 -*-



import requests
import xml.etree.ElementTree as ET




body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:mul="http://creditinfo.com/schemas/2012/09/MultiConnector">
   <soapenv:Header>
      <wsse:Security soapenv:mustUnderstand="0" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
         <wsse:UsernameToken>
            <wsse:Username>cis.admin</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Heslo123456</wsse:Password>
         </wsse:UsernameToken>
      </wsse:Security>
 </soapenv:Header>
   <soapenv:Body>
      <mul:ListConnectors>
         <!--Optional:-->
         <mul:request>
            <mul:MessageId>324db159-f261-4991-9600-8bf5086282c6</mul:MessageId>

         </mul:request>
      </mul:ListConnectors>
   </soapenv:Body>
</soapenv:Envelope>"""

url="http://cishd-mc-app01/Testing/MultiConnector.svc"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/schemas/2012/09/MultiConnector/MultiConnectorService/ListConnectors"',
           'Content-Length': str(len(body)),
           'Host': 'cishd-mc-app01',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None    
}

response = requests.post(url,data=body,headers=headers)
print(response)

tree = ET.fromstring(response.text)
x = tree.find('.//{http://creditinfo.com/schemas/2012/09/MultiConnector}Description') #first

conns = tree.find('.//{http://creditinfo.com/schemas/2012/09/MultiConnector}Connectors')
conns_info = conns.findall('.//{http://creditinfo.com/schemas/2012/09/MultiConnector}ConnectorInfo')

connector_lst = list()

for con in conns_info:
    description = con.find('.//{http://creditinfo.com/schemas/2012/09/MultiConnector}Description').text
    id = con.find('.//{http://creditinfo.com/schemas/2012/09/MultiConnector}Id').text
    print(description + " " + id)

    connector_lst.append((description, id))

""" export to xlsx
import pandas as pd
connector_df = pd.DataFrame(connector_lst)
connector_df.to_excel("conn.xlsx", header=False, index=False)
"""

