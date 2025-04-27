from nbt import nbt
import json

def readShipsFile(file):
    nbtfile = nbt.NBTFile(file,'rb')
    value = nbtfile["data"]["vs_pipeline"].value.decode("ascii")
    dic = json.loads(value)
    #ch = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '.', "'", ' '}  
    #print("".join([c for c in str(dic) if c not in ch]).replace('first', '').replace('second', ''))
    return dic

def writeShipsFile(file, dic):
    value = json.dumps(dic).replace(" ", "") #convert dict to string
    byte_value = value.encode("ascii") #convert string to bytes
    byte_array = bytearray(byte_value) #convert to byte array
    
    nbtfile = nbt.NBTFile(file,'rb') #read nbt file
    nbtfile["data"]["vs_pipeline"].value = byte_array #set value to byte array
    nbtfile.write_file()