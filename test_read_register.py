from pyModbusTCP.client import ModbusClient
from env import *
from pclController import *

import time



c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
is_ok = True

if not c.is_open():
    if not c.open():
        print("unable to connect to SERVER_HOST:")

    # if open() is ok, read register (modbus function 0x03)
    if c.is_open():
        # read 10 registers at address 0, store result in regs list
        regs = c.read_holding_registers(100, 10)
        # if success display registers
        if regs:
            print("reg ad #0 to 9: "+str(regs))

    # sleep 2s before next polling
    time.sleep(2)