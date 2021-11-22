from flask import Flask , jsonify , request
from flask_restful import Api ,Resource

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
is_ok = True
 
coil_return = 0
coil_receive = 1

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)



# @app.route("/test" , methods=['GET'])
# def test():
#     return jsonify({ 
#             "status": "success",
#             "statusCode": 201
#         })

@app.route("/test", methods=['POST'])
def test1():
    return  getIp()




# @app.route("/testplc", methods=['GET'])
# def testplc():
#     # c = ModbusClient(host=getIpPLC(),port=getPortPLC(),auto_open=True)
#     print(c)
#     is_ok = c.write_single_coil(0,1)
#     print(is_ok)
#     response = requests.post('http://192.168.1.132:8080/app/post/test1')
#     print(response.json())
#     data = response.json()
#     print(data["data"])
#     if is_ok:
#         return jsonify({
#             "status": "success",
#             "statusCode": 201,
#             "data" : True
#         })
#         # 192.168.1.132:8080/app/post/test1        
#     else:
#         return jsonify({
#             "status": "success",
#             "statusCode": 200,
#             "data" : False
#         })

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
        

# @app.route("/machine/command/test" , methods = ['POST'])
# def machineCommandTest():
#     # return jsonify({"data" : request.form['number_order']})    
#     print("api => /machine/command/test") 
#     command_str_0 = request.json['command_str_0']
#     command_str_1 = request.json['command_str_1']
#     coil_number_1 = command_str_1                  
#     is_ok = c.write_single_coil(command_str_0,coil_number_1)
#     print(c)            
#     print(is_ok)
#     if is_ok :
#         print("success")
    
#     else :
#         print("not success")

#     return jsonify({ 
#             "status": "success",
#             "statusCode": 201
#         })


# @app.route("/machine/command/gasOut" , methods = ['POST'])
# def machineCommandGasOut():
#     print("api => /machine/command/gasOut") 
#     command_str_0 = request.json['command_str_0']
#     command_str_1 = request.json['command_str_1']
#     coil_number_1 = command_str_1                  
#     is_ok = c.write_single_coil(command_str_0,coil_number_1)
#     checkLoop = True
#     step1 = 0
#     step2 = 0            
#     print(is_ok)
#     if is_ok :
#         while checkLoop :
#             regs = c.read_holding_registers(0, 0x66 )
#             if regs[101] == 1 :
#                 checkIn = True
#                 step1 = 1
#                 checkLoop = False                    
#             else :
#                 time.sleep(5)
#         time.sleep(20)
#         checkLoop = True

#         if step1 == 1 :
#             while checkLoop :
#                 print('s')
#                 regs = c.read_holding_registers(0, 0x66 )
#                 if regs[102] == 1 :
#                     # เอามาคืนแล้ว
#                     checkIn = False
#                     step2 = 1
#                     checkLoop = False                    
#                 else :
#                     time.sleep(5)
        
#         if step1 == 1 and step2 == 1 :     
#             print("success")
#             return jsonify({ 
#                 "status": "success",
#                 "statusCode": 201
                
#             })
    
#     else :
#         print("no success")

#         return jsonify({ 
#             "status": "error",
#             "statusCode": 200 ,
#             "data" : "can't connect PLC"
#         })
      
# @app.route("/machine/command/gasIn" , methods = ['POST'])
# def machineCommandGasIn():
#     print("api => /machine/command/gasIn") 
#     command_str_0 = request.json['command_str_0']
#     command_str_1 = request.json['command_str_1']
#     coil_number_1 = command_str_1                  
#     is_ok = c.write_single_coil(command_str_0,coil_number_1)
#     checkLoop = True
#     step1 = 0
#     step2 = 0            
#     print(is_ok)
#     if is_ok :
#         while checkLoop :
#             regs = c.read_holding_registers(0, 0x66 )
#             if regs[101] == 1 :
#                 checkIn = True
#                 step1 = 1
#                 checkLoop = False                    
#             else :
#                 time.sleep(5)
#         time.sleep(20)
#         checkLoop = True

#         if step1 == 1 :
#             while checkLoop :
#                 regs = c.read_holding_registers(0, 0x66 )
#                 if regs[102] == 1 :
#                     # เอามาคืนแล้ว
#                     checkIn = False
#                     step2 = 1
#                     checkLoop = False                    
#                 else :
#                     time.sleep(5)
        
#         if step1 == 1 and step2 == 1 :     
#             print("success")
#             return jsonify({ 
#                 "status": "success",
#                 "statusCode": 201
                
#             })
    
#     else :
#         print("no success")

#         return jsonify({ 
#             "status": "error",
#             "statusCode": 200 ,
#             "data" : "can't connect PLC"
#         })

# @app.route("/machine/command/gasInOut" , methods = ['POST'])
# def machineCommandGetGasInOut():
#     print("api => machine/command/get/statusCommand/gasInOut") 
#     if c.is_open():        
#         command_str_0 = 0
#         command_str_1 = 0
#         coil_number_1 = command_str_1                  
#         is_ok = c.write_single_coil(command_str_0,coil_number_1)
#         # print(is_ok)
#         checkLoop = True
#         checkIn = False
#         step1 = 0
#         step2 = 0
#         step3 = 0
#         step4 = 0
#         if is_ok :
#             # check status gasIn
#             while checkLoop :
#                 regs = c.read_holding_registers(0, 0x66 )
#                 if regs[101] == 1 :
#                    checkIn = True
#                    step1 = 1
#                    checkLoop = False                    
#                 else :
#                     time.sleep(5)
#             # รอเอาแก้เข้า
#             time.sleep(20)
#             checkLoop = True
#             if checkIn == True :
#                 while checkLoop :
#                     regs = c.read_holding_registers(0, 0x66 )
#                     if regs[102] == 1 :
#                         # เอามาคืนแล้ว
#                         checkIn = False
#                         step2 = 1
#                         checkLoop = False                    
#                     else :
#                         time.sleep(5)
#             # เอาถังออก
#             checkLoop = True
#             if checkIn == False :
#                 command_str_0 = 0
#                 command_str_1 = 1
#                 is_ok = c.write_single_coil(command_str_0,coil_number_1)
#                 # เอาแขนเข้าไปหยิบ
#                 while checkLoop :
#                     regs = c.read_holding_registers(0, 0x66 )
#                     if regs[101] == 1 :
#                         # แขนกำลังไปหยิบ
#                         checkIn = True
#                         step3 = 1
#                         checkLoop = False                    
#                     else :
#                         time.sleep(5)
#                 time.sleep(20)
#                 checkLoop = True
#                 if checkIn == True :
#                     while checkLoop :
#                         regs = c.read_holding_registers(0, 0x66 )
#                         if regs[102] == 1 :
#                             # หยิบมาให้แล้ว
#                             checkIn = False
#                             step4 = 1
#                             checkLoop = False                    
#                         else :
#                             time.sleep(5)
#             if step1 == 1 and step2 == 1 and step3 == 1 and step4 == 1 :
#                 print("success")
#                 return jsonify({ 
#                     "status": "error",
#                     "statusCode": 201 ,
#                     "data" : ""
#                 })

#         else :
#             print("no success")

#             return jsonify({ 
#                 "status": "error",
#                 "statusCode": 200 ,
#                 "data" : "can't connect PLC (is_ok)"
#             })

#     else :
#             print("no success")
#             return jsonify({ 
#                 "status": "error",
#                 "statusCode": 200 ,
#                 "data" : "can't connect PLC"
#             })

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
    # else :
    #         print("no success")
    #         return jsonify({ 
    #             "status": "error",
    #             "statusCode": 200 ,
    #             "data" : "can't connect PLC"
    #         })
  
# @app.route("/machine/command/get/status/gasOut" , methods = ['POST'])
# def machineCommandGetstatusGasOut():
#     print("api => machine/command/get/statusCommand/gasOut") 
#     if c.is_open():
        
#         #  register position at 102
#         regs = c.read_holding_registers(0, 0x66 )
#         time.sleep(2)
#         if regs:
#             print("reg ad 102 : "+str(regs))
            
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



# @app.route("/test" , methods = ['GET'])
# def testX():
#     print("api => machine/command/get/statusCommand/gasOut") 
#     x =  [0,0,0,0,0,0,0,0,0,0,1]
#     print(x[10])

#     checkLoop = True
        
#     # check status gasIn
#     while checkLoop :
#         # regs = c.read_holding_registers(0, 0x65 )
#         print(1)
#         checkLoop = False
#         time.sleep(5)

#     return jsonify({ 
#         "status": "error",
#         "statusCode": 200 ,
#         "data" : x
#     })  



























if __name__ == "__main__":
    app.run(host= "192.168.0.101" ,debug=True , port=5000)
    #app.run(host="192.168.250.12" ,debug=True , port=5000)

    # app.run(debug=True , port=5000)
print("start")