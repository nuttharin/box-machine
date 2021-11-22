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
print(c)
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


@app.route("/machine/command/gasOutx" , methods = ['POST'])
def machineCommandGasOutx():
    # return jsonify({"data" : request.form['number_order']})    
    number_order = request.json['number_order']
    order_id = request.json['order_id']
    print(number_order)
    print(order_id)
    if number_order is None:
        return  jsonify({
                "status": "error",
                "statusCode": 200,
                "data" : "not have parameter ( number_order )"
            })
    else:        
        # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
        i = 1
        while i <= number_order :
            print("status write") 
            is_ok = True                   
            # is_ok = c.write_single_coil(0,1)
            # print(c)            
            # print(is_ok)
           
            if is_ok : 
                # api update
                # print("if is_ok")
                url = "http://"+getIpApi()+"/app/post/fromMachine/update/quality/gasOut"
                myobj = {
                            'order_id': order_id ,  
                            'quality' : i
                        }
                resJson = requests.post(url, data = myobj)
                # print(i)
                # print(number_order)
                # print(resJson.json()["statusCode"])

                if resJson.json()["statusCode"] == 201 : 
                    # print("update complete")
                    i+=1

                if i == number_order :
                    return  jsonify({
                            "status": "success",
                            "statusCode": 201,
                            "data" : "write_single_coil complete"
                        })
                # i+=1
            else :
                print("else is_ok")
                return  jsonify({
                    "status": "error",
                    "statusCode": 200,
                    "data" : "error write_single_coil"
                })
        
@app.route("/machine/command/gasInx" , methods = ['POST'])
def machineCommandGasInx():
    # return jsonify({"data" : request.form['number_order']})    
    number_order = request.json['number_order']
    order_id = request.json['order_id']
    print(number_order)
    print(order_id)
    if number_order is None:
        return  jsonify({
                "status": "error",
                "statusCode": 200,
                "data" : "not have parameter ( number_order )"
            })
    else:        
        # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
        i = 1
        while i <= number_order :
            print("status write") 
            is_ok = True                   
            # is_ok = c.write_single_coil(0,1)
            # print(c)            
            # print(is_ok)
           
            if is_ok : 
                # api update
                # print("if is_ok")
                url = "http://"+getIpApi()+"/app/post/fromMachine/update/quality/gasOut"
                myobj = {
                            'order_id': order_id ,  
                            'quality' : i
                        }
                resJson = requests.post(url, data = myobj)
                # print(i)
                # print(number_order)
                # print(resJson.json()["statusCode"])

                if resJson.json()["statusCode"] == 201 : 
                    # print("update complete")
                    i+=1

                if i == number_order :
                    return  jsonify({
                            "status": "success",
                            "statusCode": 201,
                            "data" : "write_single_coil complete"
                        })
                # i+=1
            else :
                print("else is_ok")
                return  jsonify({
                    "status": "error",
                    "statusCode": 200,
                    "data" : "error write_single_coil"
                })

@app.route("/machine/command/getVolume" , methods = ['POST'])
def machineCommandGetVolume():
    # return jsonify({"data" : request.form['number_order']})    
    command_str = request.json['command_str']
    coil_number = getCommandWrite(command_str)
    print(coil_number)
    print("status write coil") 
    is_ok = True                   
    is_ok = c.write_single_coil(0,coil_number)
    print(c)            
    print(is_ok)
    return jsonify({ 
            "status": "success",
            "statusCode": 201
        })



# @app.route("/machine/command/get/status/gasOut" , methods = ['POST'])
# def machineCommandGetstatusGasOut():
#     print("api => machine/command/get/statusCommand/gasOut") 
#     if not c.is_open():
        
#         #  register position at 102
#         regs = c.read_holding_registers(0, 0x66 )
# 	    print(regs)
#         time.sleep(2)
#         if regs:
#             print("reg ad 102 : "+str(regs))
            
#             return jsonify({ 
#                 "status": "success",
#                 "statusCode": 201,
#                 "data" : regs
#             })

#         else :
#             print("no success 2")
#             return jsonify({ 
#                 "status": "error",
#                 "statusCode": 200 ,
#                 "data" : "can't connect PLC"
#             }) 
#     else :
#         print("no success 1")
#         return jsonify({ 
#             "status": "error",
#             "statusCode": 200 ,
#             "data" : "can't connect PLC"
#         })
 
# @app.route("/machine/command/get/status/gasIn" , methods = ['POST'])
# def machineCommandGetstatusGasIn():
#     print("api => machine/command/get/statusCommand/gasIn") 
#     if c.is_open():
        
#         #  register position at 101
#         regs = c.read_holding_registers(0, 0x65 )
#         time.sleep(2)
#         if regs:
#             print("reg ad 101 : "+str(regs))
            
#             return jsonify({ 
#                 "status": "success",
#                 "statusCode": 201,
#                 "data" : regs
#             }) 
#         else :
#             print("no success")

#             return jsonify({ 
#                 "status": "error",
#                 "statusCode": 200 ,
#                 "data" : "can't connect PLC"
#             })
#     else :
#             print("no success")
#             return jsonify({ 
#                 "status": "error",
#                 "statusCode": 200 ,
#                 "data" : "can't connect PLC"
#             })

@app.route("/machine/command/gasInOut" , methods = ['POST'])
def machineCommandGetGasInOut():
    print("api => machine/command/get/statusCommand/gasInOut") 
    if c.is_open():        
        command_str_0 = 0
        command_str_1 = 0
        coil_number_1 = command_str_1                  
        is_ok = c.write_single_coil(command_str_0,coil_number_1)
        print(is_ok)
        checkLoop = True
        checkIn = False
        step1 = 0
        step2 = 0
        step3 = 0
        step4 = 0
        if is_ok :
            # check status gasIn
            while checkLoop :
                regs = c.read_holding_registers(0, 0x65 )
                if regs[101] == 1 :
		            # print("101=1")
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
                    if regs[102] == 1 :
			           
                        # GasIn Success
                        print("102=1")
                        checkIn = False
                        step2 = 1
                        checkLoop = False                    
                    else :
                        time.sleep(5)
            # Gas out
            checkLoop = True
            if checkIn == False :
                command_str_0 = 0
                command_str_1 = 1
                is_ok = c.write_single_coil(command_str_0,coil_number_1)
                # keep Gas tank
                while checkLoop :
                    regs = c.read_holding_registers(0, 0x65 )
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
                        if regs[102] == 1 :
                            # Gas Out success
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

@app.route("/machine/command/gasOut" , methods = ['POST'])
def machineCommandGasOut():
    print("api => /machine/command/gasOut") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    coil_number_1 = command_str_1
    is_ok = c.write_single_coil(0,1)
    regs = c.read_holding_registers(0, 0x65 )
    print("reg ad #0 to 9: "+str(regs))
    print(is_ok)
    c.close()
    print(c.is_open)
    checkLoop = True
    step1 = 0
    step2 = 0            
    print(is_ok)
    print(c.is_open)
    print(c1.is_open)
    i = 1
    if is_ok :
        while checkLoop :
	        print(i)
	        print(c.is_open)
            # i = i + 1
            regs = c.read_holding_registers(0, 0x65)
            print("reg ad #0 to 9: "+str(regs))
	        # regs = c.read_holding_registers(0, 0x65 )
            if regs:
	            print(regs[100])
                # c.close()
                if regs[100] == 1 :
                    print("101=1")
                    checkIn = True
                    step1 = 1
                    checkLoop = False                    
                else :
                    time.sleep(5)
        time.sleep(20)
        checkLoop = True

        if step1 == 1 :
            while checkLoop :
                print('\n s')
	            regs = c.read_holding_registers(0, 0x66 )
                print("reg ad #0 to 9: "+str(regs))
                # regs = c.read_holding_registers(0, 0x65 )
                if regs:
                   print(regs[101])
#            c.close()
                    if regs[100] == 0 :
                        print("101=0")
                        checkIn = True
                        step2 = 1
                        checkLoop = False
                    else :
                        time.sleep(5)
        
        if step1 == 1 and step2 == 1 :     
            print("success")
            return jsonify({ 
                "status": "success",
                "statusCode": 201
                
            })
    
    else :
        print("no success")

        return jsonify({ 
            "status": "error",
            "statusCode": 200 ,
            "data" : "can't connect PLC"
        })
      
@app.route("/machine/command/gasIn" , methods = ['POST'])
def machineCommandGasIn():
    print("api => /machine/command/gasIn") 
    command_str_0 = request.json['command_str_0']
    command_str_1 = request.json['command_str_1']
    coil_number_1 = command_str_1                  
    is_ok = c.write_single_coil(command_str_0,coil_number_1)
    print(is_ok)
    checkLoop = True
    step1 = 0
    step2 = 0            
    print(is_ok)
    if is_ok :
        while checkLoop :
            regs = c.read_holding_registers(0, 0x65 )
	        print(regs)
            if regs[101] == 1 :
                checkIn = True
                step1 = 1
                checkLoop = False                    
            else :
                time.sleep(5)
        time.sleep(20)
        checkLoop = True

        if step1 == 1 :
            while checkLoop :
                regs = c.read_holding_registers(0, 0x66 )
                if regs[102] == 1 :
                    # return gas success
                    checkIn = False
                    step2 = 1
                    checkLoop = False                    
                else :
                    time.sleep(5)
        
        if step1 == 1 and step2 == 1 :     
            print("success")
            return jsonify({ 
                "status": "success",
                "statusCode": 201
                
            })
    
    else :
        print("no success")

        return jsonify({ 
            "status": "error",
            "statusCode": 200 ,
            "data" : "can't connect PLC"
        })


if __name__ == "__main__":
    app.run(host= "172.20.10.3" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")
