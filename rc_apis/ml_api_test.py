# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:09:03 2023

@author: user
"""

import json
import requests
url='http://127.0.0.1:8000/get_recommendations'
input_data_for_model={
     'service_name':'Request to extend a provisional registration certificate for a national commercial ship'}

 
input_json=json.dumps(input_data_for_model)
response=requests.post(url,data=input_json)
print(response.text)