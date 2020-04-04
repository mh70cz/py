# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:05:14 2017

@author: mh70
"""

import json

for s in sablony:

    #s_json = json.dumps(s)
    
    fname =  "./sablony/" + str(s['id']) + ".json"
                               
    with open(fname, 'w', encoding='utf-8') as outfile:
        json.dump(s, outfile, ensure_ascii=False)



"""
r = {'is_claimed': 'True', 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5
type(r) #Output str
type(loaded_r) #Output dict

....

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)



"""