from flask import Flask , jsonify , request
from flask_restful import Api

from env import *
from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests
import time
import socket



def updateStatusMachine(status , order_id) :
    #return ip
    url = "http://localhost:8080/"
    myobj = {
        'status': 0 ,
        'order_id' : 52
    }
    resJson = requests.post(url, data = myobj)
    # print(i)
    # print(number_order)

    if resJson :
        if resJson.json()["statusCode"] == 201 :
            return True 
        else : 
            return False
    else :
        return jsonify({ 
            "status": "success",
            "statusCode": 201 ,
            "data" : "command complete"              
        })


