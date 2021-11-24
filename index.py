from flask import Flask , jsonify , request
from flask_restful import Api


from env import *
from pclController import *
from command import *
from pyModbusTCP.client import ModbusClient
import requests
import time
import socket



app = Flask(__name__)
api = Api(app)
c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
c1 = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
is_ok = True
 
coil_return = 0
coil_receive = 1

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)











 

@app.route("/test" , methods = ['GET'])
def testX():
    print("api => machine/command/get/statusCommand/gasOut") 
    x =  [0,0,0,0,0,0,0,0,0,0,1]
    print(x[10])

    checkLoop = True
        
    # check status gasIn
    while checkLoop :
        # regs = c.read_holding_registers(0, 0x65 )
        print(1)
        checkLoop = False
        time.sleep(5)

    return jsonify({ 
        "status": "error",
        "statusCode": 200 ,
        "data" : x
    })  



@app.route("/machine/command/gasOut" , methods = ['POST'])
def machineCommandGasOut():
    print("api => /machine/command/gasOut") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    order_id =  request.json['order_id']
    quality = request.json['quality']
    print(quality)
    if quality == 1 :
        print("111111")
        # coil_number_1 = command_str_1
        # is_ok = c.write_single_coil(0,1)
        is_ok = c.write_single_coil(command_str_0,command_str_1)
        c.close()
        # print(c.is_open)
        checkLoop = True
        step1 = 0
        step2 = 0            
        # print(is_ok)
        # print(c.is_open)
        # print(c1.is_open)
        i = 1
        if is_ok :
            while checkLoop :
                # print(i)
                # i = i + 1
                # print(c.is_open)
                regs = c.read_holding_registers(0, 0x66 )
                # print("reg ad #0 to 9: "+str(regs))
                # regs = c.read_holding_registers(0, 0x65 )
                if regs:
                    # print(regs[100])
                    # c.close()
                    if regs[101] == 1 :
                        print("101 = 1")
                        checkIn = True
                        step1 = 1
                        checkLoop = False                    
                    else :
                        time.sleep(7)
            time.sleep(20)
            checkLoop = True
            if step1 == 1 :
                while checkLoop :
                    regs = c.read_holding_registers(0, 0x66 )
                    if regs :
                        print(regs[101])
                        # c.close()
                        if regs[101] == 0 :
                            print("100 = 0")
                            checkIn = True
                            step2 = 1
                            checkLoop = False
                        else :
                            time.sleep(7 )
                    else :
                        return jsonify({ 
                            "status": "error",
                            "statusCode": 200 ,
                            "data" : "can't connect PLC read_holding_registers "
                        })
            
            if step1 == 1 and step2 == 1 :     
                print("success")
                return jsonify({ 
                    "status": "success",
                    "statusCode": 201 ,
                    "data" : "command complete"              
                })
        
        else :
            print("no success")
            return jsonify({ 
                "status": "error",
                "statusCode": 200 ,
                "data" : "can't connect PLC"
            })
    else :
        print("else")
        x = 0
        while x < quality :
            # coil_number_1 = command_str_1
            # is_ok = c.write_single_coil(0,1)
            is_ok = c.write_single_coil(command_str_0,command_str_1)
            c.close()
            # print(c.is_open)
            checkLoop = True
            step1 = 0
            step2 = 0            
            # print(is_ok)
            # print(c.is_open)
            # print(c1.is_open)
            i = 1
            if is_ok :
                while checkLoop :
                    # print(i)
                    # i = i + 1
                    # print(c.is_open)
                    regs = c.read_holding_registers(0, 0x66 )
                    # print("reg ad #0 to 9: "+str(regs))
                    # regs = c.read_holding_registers(0, 0x65 )
                    if regs:
                        print(regs[100])
                        print(regs[101])
                        # c.close()
                        if regs[101] == 1 :
                            print("101 = 1")
                            checkIn = True
                            step1 = 1
                            checkLoop = False                    
                        else :
                            time.sleep(7)
                time.sleep(20)
                checkLoop = True
                if step1 == 1 :
                    while checkLoop :
                        regs = c.read_holding_registers(0, 0x66 )
                        if regs :
                            print(regs[101])
                            # c.close()
                            if regs[101] == 0 :
                                print("101 = 0")
                                checkIn = True
                                step2 = 1
                                checkLoop = False
                            else :
                                time.sleep(7 )
                        else :
                            return jsonify({ 
                                "status": "error",
                                "statusCode": 200 ,
                                "data" : "can't connect PLC read_holding_registers "
                            })
                # if step2 = 1  

                # if step1 == 1 and step2 == 1 :     
                #     print("success")
                #     return jsonify({ 
                #         "status": "success",
                #         "statusCode": 201 ,
                #         "data" : "command complete"              
                #     })
            
            else :
                print("no success")
                return jsonify({ 
                    "status": "error",
                    "statusCode": 200 ,
                    "data" : "can't connect PLC"
                })
            x= x+1
            print("x")
            print(x)

    return jsonify({ 
        "status": "success",
        "statusCode": 201 ,
        "data" : "command complete"              
    })

      
@app.route("/machine/command/gasIn" , methods = ['POST'])
def machineCommandGasIn():
    print("api => /machine/command/gasIn") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    order_id =  request.json['order_id']

    # coil_number_1 = command_str_1
    # is_ok = c.write_single_coil(0,1)
    is_ok = c.write_single_coil(command_str_0,command_str_1)
    c.close()
    # print(c.is_open)
    checkLoop = True
    step1 = 0
    step2 = 0            
    print(is_ok)
    # print(c.is_open)
    # print(c1.is_open)
    i = 1
    if is_ok :
        while checkLoop :
	        # print(i)
            # i = i + 1
	        # print(c.is_open)
            regs = c.read_holding_registers(0, 0x66 )
            print("reg ad #0 to 9: "+str(regs))
	        # regs = c.read_holding_registers(0, 0x65 )
            if regs:
	            # print(regs[100])
                # print(regs[101])
                # c.close()
                if regs[100] == 1 :
       	            print("100 = 1")
                    checkIn = True
                    step1 = 1
                    checkLoop = False                    
                else :
                    time.sleep(7)
        time.sleep(20)
        checkLoop = True
        if step1 == 1 :
            while checkLoop :
                regs = c.read_holding_registers(0, 0x66 )
                if regs :
                    print(regs[100])
                    print(regs[101])
                    # c.close()
                    if regs[100] == 0 :
                        print("100 = 0")
                        checkIn = True
                        step2 = 1
                        checkLoop = False
                    else :
                        time.sleep(7 )
                else :
                    return jsonify({ 
                        "status": "error",
                        "statusCode": 200 ,
                        "data" : "can't connect PLC read_holding_registers "
                    })
        
        if step1 == 1 and step2 == 1 :     
            print("success")
            return jsonify({ 
                "status": "success",
                "statusCode": 201 ,
                "data" : "command complete"              
            })
    
    else :
        print("no success")
        return jsonify({ 
            "status": "error",
            "statusCode": 200 ,
            "data" : "can't connect PLC"
        })

@app.route("/machine/command/gasInOut" , methods = ['POST'])
def machineCommandGetGasInOut():
    print("api => machine/command/get/statusCommand/gasInOut") 
    # order_id =  request.json['order_id']
    
    if True:        
        command_str_0 = 0
        command_str_1 = 1
        coil_number_1 = command_str_1                  
        is_ok = c.write_single_coil(command_str_0,coil_number_1)
        print(is_ok)
        checkLoop = True
        checkIn = False
        step1 = 0
        step2 = 0
        step3 = 0
        step4 = 0
        if is_ok :# check status gasIn
            while checkLoop :
                regs = c.read_holding_registers(0, 0x66 )
                print(regs[100])
                print(regs[101])
                print("-------")
                if regs:
                    if regs[100] == 1 :
                        print("100=1")
                        checkIn = True
                        step1 = 1
                        checkLoop = False                    
                    else :
                        time.sleep(5)
            # wait Gas In
            time.sleep(20)
            checkLoop = True
            if checkIn == True :
                while checkLoop :
                    regs = c.read_holding_registers(0, 0x66 )
                        # print(regs[100])
                        # print(regs[101])
                        # print("-------")
                    if regs:
                        if regs[100] == 0 :                        
                            # GasIn Success
                            print("100=0")
                            checkIn = False
                            step2 = 1
                            checkLoop = False                    
                        else :
                            time.sleep(5)
            # Gas out
            print("in")
            checkLoop = True
            if checkIn == False :
                command_str_0 = 1
                command_str_1 = 1
                is_ok = c.write_single_coil(command_str_0,coil_number_1)
                # keep Gas tank
                while checkLoop :
                    regs = c.read_holding_registers(0, 0x66 )
                        # print(regs[100])
                        # print(regs[101])
                        # print("-------")
                    if regs:
                        if regs[101] == 1 :
                            # keepping Gas tank
                            checkIn = True
                            step3 = 1
                            checkLoop = False                    
                        else :
                            time.sleep(5)
                time.sleep(20)
                checkLoop = True
                if checkIn == True :
                    while checkLoop :
                        regs = c.read_holding_registers(0, 0x66 )
                        print(regs[101])
                        if regs:
                            if regs[101] == 0 :
                                # Gas Out successs
                                checkIn = False
                                step4 = 1
                                checkLoop = False                    
                            else :
                                time.sleep(5)
            if step1 == 1 and step2 == 1 and step3 == 1 and step4 == 1 :
                print("success")
                return jsonify({ 
                    "status": "error",
                    "statusCode": 201 ,
                    "data" : ""
                })
        else :
            print("no success")
            return jsonify({ 
                "status": "error",
                "statusCode": 200 ,
                "data" : "can't connect PLC (is_ok)"
            })  
    else :
        print("no success")
        return jsonify({ 
            "status": "error",
            "statusCode": 200 ,
            "data" : "can't connect PLC"
        })

if __name__ == "__main__":
    app.run(host= "172.20.10.4" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")