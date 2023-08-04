# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    service_name:str
    
#loading the saved model
services=pickle.load(open('/models/services.pkl','rb'))
similarity=pickle.load(open('/models/similarity.pkl','rb'))

@app.post('/get_recommendations')
def get_recommendations(input_parameters:model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    service_name = input_dictionary['service_name']
    #service_name = "Request for issuance of PRO card"
    service_index = services[services['ServiceName'] == service_name].index[0]
    distances = similarity[service_index]
    service_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendations = services['ServiceName'].iloc[list(x[0] for x in service_list)].tolist()
    return recommendations
