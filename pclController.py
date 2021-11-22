from pyModbusTCP.client import ModbusClient
from env import *

def testPCL():
    c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
    print(c)
    is_ok = c.write_single_coil(0,1)
    print(is_ok)
    if is_ok:
        return "is ok"
    else:
        return "is not ok"
