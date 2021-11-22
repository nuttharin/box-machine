from flask import Flask , jsonify , request
from flask_restful import Api

from env import *
from funtionApi import *

from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests
import time
import socket


updateStatusMachine(13)
