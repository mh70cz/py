"""
rollback čehosi -  od Václava D. 2017-11-06
"""

import requests

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


body = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:cb5="http://creditinfo.com/CB5">
    <SOAP-ENV:Header/>
    <SOAP-ENV:Body>
        <cb5:RollbackBatch>
            <cb5:batchIdentifier>{batchIdentifier}</cb5:batchIdentifier>
            <cb5:rollbackReason>InvalidOrFakeData</cb5:rollbackReason>
            <cb5:reasonMessage>Rolled back due to Payment Incident reupload when PI code have changed</cb5:reasonMessage>
        </cb5:RollbackBatch>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""
    
url="https://ws.kib.lv/WsBackOffice/service.svc"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"http://creditinfo.com/CB5/IBackOfficePublicService/RollbackBatch"',
           'Content-Length': str(len(body)),
           'Host': 'ws.kib.lv',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Authorization': 'Basic ', #'Basic hashed(name+pass)' e.g. 'Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE='
           'Accept': None
           }

    
    
    
for batchIdentifier in ['SEB_20161231_C_PCRP_3_XML']:
    response = requests.post(url,data=body.replace('{batchIdentifier}',batchIdentifier), headers=headers, verify=False)    
    print(response.text)
    if response.status_code != 200:
        print("problem with response" + str(batchIdentifier))