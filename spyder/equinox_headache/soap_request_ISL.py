# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:16:27 2017

@author: mh70
nahrad skutecnym heslem
PasswordText"></wsse:Password>

"""

import requests




body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:mul="http://creditinfo.com/schemas/2012/09/MultiConnector" 
xmlns:req="http://creditinfo.com/schemas/2012/09/MultiConnector/Messages/Request" 
xmlns:bee="http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/GOV/BeeSubjectMatch/Request">
<soapenv:Header>
      <wsse:Security soapenv:mustUnderstand="0" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
         <wsse:UsernameToken>
            <wsse:Username>cis.admin</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText"></wsse:Password>
         </wsse:UsernameToken>
      </wsse:Security>
 </soapenv:Header>
   <soapenv:Body>
      <mul:Query>
         <!--Optional:-->
         <mul:request>
            <mul:MessageId>f33c5345-3a8c-498b-8ed5-558b3f4e6209</mul:MessageId>
            <mul:RequestXml>
               <mul:RequestXml>
                  <req:connector id="4414168e-5498-4613-bf90-12a7f64ee44a">
                     <req:data id="af76183b-789a-4b9b-9a61-b95ff0ac871f">
                        <bee:request>
                           <bee:DecisionWorkflow>ISL</bee:DecisionWorkflow>
                           <bee:RequestData>
                              <bee:Country>ISL</bee:Country>
                              <bee:UniqueId>2601353689</bee:UniqueId>
                               <bee:Name>Lóa</bee:Name>
                              <bee:Surname>de Fontenay</bee:Surname>
						<!--  <FullName>Lísbet Lóa Ákadóttir le Sage de Fontenay</FullName> -->
                              
                              <bee:Address>Benduloftsgata 88 Kópavogi</bee:Address> 
						<!-- missing ZipCode-->
                                                         
                           </bee:RequestData>
                        </bee:request>
                     </req:data>
                  </req:connector>
               </mul:RequestXml>
            </mul:RequestXml>
         </mul:request>
      </mul:Query>
   </soapenv:Body>
</soapenv:Envelope>"""

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

response = requests.post(url,data=body,headers=headers)
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