import json

jsonCommandWrite = {
    "ServoON_X" : 116,
    "X_JogPlus" :	117,
    "X_JogMinus" : 118,
    "ServoON_Y" : 119,
    "Y_JogPlus" : 120,
    "Y_JogMinus" : 121,
    "CyclinderLong_Extend" : 122,
    "CyclinderLong_Retract" : 123,
    "CyclinderShort_Extend" : 124,
    "CyclinderShort_Retract" : 125,
    "Gripper_Clamp" : 126,
    "Gripper_Unclamp"	: 127,
    "Door_Gas_tank" : 128,
    "test" : 1
}

def getCommandWrite(str):
    return jsonCommandWrite[str]


# print(getCommandWrite("ServoON_X"))