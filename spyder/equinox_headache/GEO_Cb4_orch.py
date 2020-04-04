# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:15:36 2017

@author: mh70
"""

import GEO_Cb4_upload
import GEO_Cb4_status
import GEO_Cb4_result
import GEO_Cb4_parse
import GEO_Cb4_common
from GEO_Cb4_common import MyBusinessException
import time
import json


#url = "https://getest.creditinfosolutions.com/WebService/Service.asmx"
# authorization = "Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE="
#host = 'getest.creditinfosolutions.com'

url = "http://appcb4/GE.CIG/Dev/WebService/Service.asmx"
host = 'appcb4'
authorization = "Basic QWRtaW46MTIzNA=="


#class MyBusinessException(Exception):
#    pass

national_id = "321322333" 
#  01011024331  01001003356 "01012002417"  "01011024334" 
# "91012002412" - not found
# "01011024335"   ?

#appcb4/GE.CIG/Dev "911111879"  911112879 911113879 321322333 995564444 



GEO_Cb4_common.wrt_f(msg = 'national_id: ' + str(national_id),
                     header = True)

try:
    batch_id = GEO_Cb4_upload.upload(national_id, url, host, authorization) # odešli batch a vrať jeho Id 
    
    #zjištuj stav dokud není Finished, 
    #pak vrať ResponseInfo.Id (ri_id) pro vyzvednutí výsledku
    state = ""    
    counter = 1
    while state != "Finished":          
        if counter > 30:
            raise MyBusinessException("Batch not finished in a given time limit")
            #break
        if counter < 4:
            time.sleep(0.5)
        else:
            time.sleep(5) 
        state, ri_id = GEO_Cb4_status.batch_status(batch_id, url, host, authorization)
        print("iteration: " + str(counter) + " batch is: " + str(state))
        counter += 1

    # vyzvedni výsledek
    batch_response_chunk_result = GEO_Cb4_result.batch_result(ri_id, url, host, authorization)
    
    #dekoduj z Base64 a odzipuj
    xml_txt = GEO_Cb4_parse.unzip_result_xml(batch_response_chunk_result)
    #print(xml_txt)
    
    #proveď parsing 
    result = GEO_Cb4_parse.parse_result(xml_txt)
    
#    if result is None:
#        raise MyBusinessException("no result")
    
    result_json = json.dumps(result, ensure_ascii=False)    
    print(result_json)
    
    GEO_Cb4_common.wrt_f(msg = result_json)

except MyBusinessException as e:
    print(e)
 
 