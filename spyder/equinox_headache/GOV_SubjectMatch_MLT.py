import requests
import xml.etree.ElementTree as ET
import uuid
import json

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# requests lib is built on top of urllib3, which has nothing to do with 
# the standard library’s urllib.request. 
# They are, however, both built on top of the standard library’s http.client. 

# https://stackoverflow.com/questions/27981545/  ? modern version of libraries:
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


subjects = [
        ("514744M", "Frank", "Portelli", "304, Villa Portelli, Triq San Pawl"),
        ("100254M", "Mario", "De Giorgio", "22, Immaculate Conception, Triq il-Poeta Nazzjonali, Zebbug (Malta)"),
        ("100254M", "Mario", "Degiorgio", "22, Immaculate Conception, Triq il-Poeta Nazzjonali, Zebbug"),
        ("1000649M", "Annunziata", "Azzopardi", "133, Triq il-Kullegg, Rabat (Malta)"),
        ("1000649M", "Annunziata", "Azzopardi", "133, Triq il-Kullegg, Rabat"),
        ("1000744M", "Antonia", "Zammit", "153, Barcellona, Triq John Borg, Birkirkara"),
        ("1000050M", "Francis", "Borg", "166, Triq l-Izbark tal-Francizi, MELLIEHA"),
        ("10026M", "Carmel", "Vella", "70, Triq il-Kullegg l-Antik, Sliema"),
        ("100169M", "Carmela", "Gauci", "85, Chez Nous, Triq il-Wied, Mosta")
         ]

# ("", "", "", "")

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



body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
xmlns:mul="http://creditinfo.com/schemas/2012/09/MultiConnector" 
xmlns:req="http://creditinfo.com/schemas/2012/09/MultiConnector/Messages/Request" 
xmlns:bee="http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/GOV/BeeSubjectMatch/Request">
      
     <soapenv:Header>
     <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
        <wsse:UsernameToken>
           <wsse:Username>cis.admin</wsse:Username>
           <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">Heslo123456</wsse:Password>
        </wsse:UsernameToken>
     </wsse:Security>
  </soapenv:Header>
  
   <soapenv:Body>
      <mul:Query>
         <!--Optional:-->
         <mul:request>
            <mul:MessageId>ed6c3001-c157-412c-a8c5-59cc2db627d2</mul:MessageId>
            <mul:RequestXml>
               <mul:RequestXml>
                  <req:connector id="4414168e-5498-4613-bf90-12a7f64ee44a">
                     <req:data id="89eca3a6-1c44-4a0a-ac8b-474d2a455e05">
                        <bee:request>
                           <bee:DecisionWorkflow>MLT</bee:DecisionWorkflow>
                           <bee:RequestData>
                              <bee:Country>MLT</bee:Country>
                              <bee:UniqueId></bee:UniqueId>
                               <bee:Name></bee:Name>
                              <bee:Surname></bee:Surname>
                              <bee:Address></bee:Address>
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

url="https://cishd-mc-app01/Testing3/MultiConnector.svc"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/schemas/2012/09/MultiConnector/MultiConnectorService/Query"',
           'Content-Length': str(len(body)),
           'Host': 'cishd-mc-app01',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None    
}

ns_response = "http://creditinfo.com/schemas/2012/09/MultiConnector/Connectors/GOV/BeeSubjectMatch/Response"

rsp_details_elms = [
        ("Idregno"),
        ("FullName"),
        ("Surname"),
        ("OtherSurname"),
        ("Name"),
        ("OtherName"),
        ("Middlenames"),
        ("Address"),
        ("Postcode"),
        ("City"),
        ("YearOfBirth"),
        ("Age"),
        ("ReportDate"),
        ("ReportId")
        ]

rsp_request_elms = [
        ("UniqueId"),
        ("Name"),
        ("Surname"),
        ("Address")
        ]

rsp_match_elms = [
        ("Flag"),
        ("Name"),
        ("Surname"),
        ("Address")
        ]

#response_out_lst = list()
response_out_dict = dict()

        
def parse_value(element, subelement_names):
    parsed_dict = dict()
    for element_name in subelement_names:
        x = element.find('.//{' + ns_response + '}' + element_name)
        if not x is None:
            parsed_dict[element_name] = x.text
    return parsed_dict 




i = 0
for subject in subjects:
        
    body_new = body.replace('<bee:UniqueId></bee:UniqueId>',
                            '<bee:UniqueId>' + subject[0] + '</bee:UniqueId>')
    body_new = body_new.replace('<bee:Name></bee:Name>',
                            '<bee:Name>' + subject[1] + '</bee:Name>')
    body_new = body_new.replace('<bee:Surname></bee:Surname>',
                            '<bee:Surname>' + subject[2] + '</bee:Surname>')
    body_new = body_new.replace('<bee:Address></bee:Address>',
                            '<bee:Address>' + subject[3] + '</bee:Address>')    
    
    body_new = replace_uuid(body_new, '<mul:MessageId>')
    body_new = replace_uuid(body_new, '<req:data id="')
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    # verify=False is required for SSL if there is no certificate
    #print(response)    
    tree = ET.fromstring(response.text) 
    rsp_details = tree.find('.//{' + ns_response + '}' + 'ResponseDetails')
    rsp_request = tree.find('.//{' + ns_response + '}' + 'Request')
    rsp_match = tree.find('.//{' + ns_response + '}' + 'Match')
    
    out_details = parse_value(rsp_details, rsp_details_elms)
    out_request = parse_value(rsp_request, rsp_request_elms)
    out_match = parse_value(rsp_match, rsp_match_elms)
                                                    
    
    response_out = {
            "request": out_request,
            "details": out_details,
            "match": out_match            
            }

        
    #response_out_lst.append(json.dumps(response_out))
    response_out_dict[i] = response_out    
    i += 1
    
print(json.dumps(response_out_dict))    
