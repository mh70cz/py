# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:16:27 2017

@author: mh70

"""

import requests
import xml.etree.ElementTree as ET



body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cig="CIG_DDD">
   <soapenv:Header/>
   <soapenv:Body>
      <cig:CISRequestDetails>
         <cig:UserName>allit</cig:UserName>
         <cig:Password>123456</cig:Password>
      	<cig:Query></cig:Query>          
</cig:CISRequestDetails>

   </soapenv:Body>
</soapenv:Envelope>"""

url="http://test.creditinfo.com.mt/WebService/ddd.asmx"
headers = {'Accept-Encoding': 'gzip,deflate',
           'Content-Type': 'text/xml;charset=UTF-8',
           'SOAPAction': '"CIG_DDD/CISRequestDetails"',
           'Content-Length': str(len(body)),
           'Host': 'test.creditinfo.com.mt',
           'Connection': 'Keep-Alive',
           'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
           'Accept': None    
}

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

response_lst_test = list()

def map_elements(elem_name_src, elem_name_dst):
    x = tree.find('.//' + elem_name_src)
    if not(type(x) == type(None)):
        response_row[elem_name_dst] = x.text

        

idregnos = [
        "514744M", "1000048M", "1000049M", "1000050M", "1000144M", "1000247M",
        "1000649M", "1000744M", "100169M", "10017G", "10026M", "100254M"
        ]
#idregnos = ["514744M"]

for idregno in idregnos:
        
    body_new = body.replace('<cig:Query></cig:Query>',
                            '<cig:Query>' + idregno + '</cig:Query>')
    response = requests.post(url,data=body_new, headers=headers)
    #print(response)    
    tree = ET.fromstring(response.text) 
    
    response_row = dict()
    
    for elem_name in elem_names:
        map_elements(elem_name[0], elem_name[1])
        
    response_lst_test.append(response_row)


def returnNotMatches(a, b):
    return [[x for x in a if x not in b], [x for x in b if x not in a]]

    

