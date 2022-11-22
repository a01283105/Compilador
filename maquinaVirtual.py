import ply.yacc as yacc
import os
import codecs
import re
import sys
from anaLexico import tokens
from sys import stdin
from cuad import *
import json

archivo = open("Necesario.json")
codigoOBJ = json.load(archivo)
archivo.close()
cuadruplos = codigoOBJ["Cuadruplos"]

contador = 0

LocalesInt = 2000
LocalesFlota = 7000
GlobalesInt = 12000
GlobalesFloat = 17000
TemporalesInt = 22000
TemporalesFloat = 27000
TemporalesPointers = 32000
ConstantesInt = 37000
ConstantesFloat = 42000
ConstantesString = 47000

localInt = []
localFloat = []
globalInt = []
globalFloat = []
temporalesInt = []
temporalesFloat = []
temporalesPointers = []
constantesInt = []
constantesFloat = []
constantesString = []

def tipoDefault(tipo: str):
        if tipo == 'int':
            return 0
        if tipo == 'float':
            return 0.0
        if tipo == 'string':
            return ""

for x in codigoOBJ["TablaV"]["global"]["var"]:
    ei = codigoOBJ["TablaV"]["global"]["var"][x]["tipo"]
    if ei == "int":
        globalInt.append(tipoDefault(ei))
    else:
        globalFloat.append(tipoDefault(ei))

for x in codigoOBJ["TablaC"]:
    ei = codigoOBJ["TablaC"][x]["tipo"]
    if ei == "int":
        constantesInt.append(int(x))
    elif ei == "float":
        constantesFloat.append(float(x))
    else:
        constantesString.append(x[1 : -1])

for x in codigoOBJ["TablaV"]:
    # print(codigoOBJ["TablaV"][x]["ContadorT"])
    for y in range(0,codigoOBJ["TablaV"][x]["ContadorT"]["int"]):
        temporalesInt.append(tipoDefault("int"))
    for z in range(0,codigoOBJ["TablaV"][x]["ContadorT"]["float"]):
        temporalesFloat.append(tipoDefault("float"))

for x in codigoOBJ["TablaV"]:
    if x == "global":
        continue
    cantidadInt = 0
    cantidadFloat = 0
    for y in codigoOBJ["TablaV"][x]["var"]:
        if codigoOBJ["TablaV"][x]["var"][y]["tipo"] == "int":
            cantidadInt += 1
        elif codigoOBJ["TablaV"][x]["var"][y]["tipo"] == "float":
            cantidadFloat += 1

    print(x,cantidadInt,cantidadFloat)
    while len(localInt) < cantidadInt:
        localInt.append(tipoDefault("int"))
    while len(localFloat) < cantidadFloat:
        localFloat.append(tipoDefault("float"))
    

def leer(direccion):
    if LocalesInt <= direccion and direccion < LocalesFlota:
        direccion -= LocalesInt
        #Meter todas asi similar
        return localInt[direccion]
    elif LocalesFlota <= direccion and direccion < GlobalesInt:
        direccion -= LocalesFlota
        #Meter todas asi similar
        return localFloat[direccion]
    elif GlobalesInt <= direccion and direccion < GlobalesFloat:
        direccion -= GlobalesInt
        return globalInt[direccion]
    elif GlobalesFloat <= direccion and direccion < TemporalesInt:
        direccion -= GlobalesFloat
        return globalFloat[direccion]
    elif TemporalesInt <= direccion and direccion < TemporalesFloat:
        direccion -= TemporalesInt
        #Meter todas asi similar
        return temporalesInt[direccion]
    elif TemporalesFloat <= direccion and direccion < TemporalesPointers:
        direccion -= TemporalesFloat
        #Meter todas asi similar
        return temporalesFloat[direccion]
    elif TemporalesPointers <= direccion and direccion < ConstantesInt:
        direccion -= TemporalesPointers
        #Meter todas asi similar
        return temporalesPointers[direccion]
    elif ConstantesInt <= direccion and direccion < ConstantesFloat:
        direccion -= ConstantesInt
        return constantesInt[direccion]
    elif ConstantesFloat <= direccion and direccion < ConstantesString:
        direccion -= ConstantesFloat
        return constantesFloat[direccion]
    elif ConstantesString <= direccion:
        direccion -= ConstantesString
        return constantesString[direccion]
    else:
        raise Exception("Intentaste buscar una direccion de memoria invalida: " + direccion)

def write(direccion, val):
    if LocalesInt <= direccion and direccion < LocalesFlota:
        direccion -= LocalesInt
        #Meter todas asi similar
        localInt[direccion] = val
    elif LocalesFlota <= direccion and direccion < GlobalesInt:
        direccion -= LocalesFlota
        #Meter todas asi similar
        localFloat[direccion] = val
    elif GlobalesInt <= direccion and direccion < GlobalesFloat:
        direccion -= GlobalesInt
        globalInt[direccion] = val
    elif GlobalesFloat <= direccion and direccion < TemporalesInt:
        direccion -= GlobalesFloat
        globalFloat[direccion] = val
    elif TemporalesInt <= direccion and direccion < TemporalesFloat:
        direccion -= TemporalesInt
        #Meter todas asi similar
        temporalesInt[direccion] = val
    elif TemporalesFloat <= direccion and direccion < TemporalesPointers:
        direccion -= TemporalesFloat
        #Meter todas asi similar
        temporalesFloat[direccion] = val
    elif TemporalesPointers <= direccion and direccion < ConstantesInt:
        direccion -= TemporalesPointers
        #Meter todas asi similar
        temporalesPointers[direccion] = val
    elif ConstantesInt <= direccion and direccion < ConstantesFloat:
        direccion -= ConstantesInt
        constantesInt[direccion] = val
    elif ConstantesFloat <= direccion and direccion < ConstantesString:
        direccion -= ConstantesFloat
        constantesFloat[direccion] = val
    elif ConstantesString <= direccion:
        direccion -= ConstantesString
        constantesString[direccion] = val
    else:
        raise Exception("Intentaste buscar una direccion de memoria invalida: " + direccion)

#Operaciones
def goto(cuad):
    global contador
    contador = cuad["temp"]

def gotoV(cuad):
    global contador
    temp = leer(cuad["op1"])
    if temp != 0: 
        contador = cuad["temp"]
    else:
        contador += 1

def gotoF(cuad):
    global contador
    temp = leer(cuad["op1"])
    if temp == 0: 
        contador = cuad["temp"]
    else:
        contador += 1

def mas(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = val1 + val2
    write(cuad["temp"],val)
    contador += 1

def menos(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = val1 - val2
    write(cuad["temp"],val)
    contador += 1

def por(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = val1 * val2
    write(cuad["temp"],val)
    contador += 1

def entre(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = val1 / val2
    write(cuad["temp"],val)
    contador += 1

def assignar(cuad):
    global contador
    val = leer(cuad["op1"])
    write(cuad["temp"],val)
    contador += 1

def igual(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 == val2:
        val = 1
    write(cuad["temp"],val)
    contador += 1

def menorque(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 < val2:
        val = 1
    write(cuad["temp"],val)
    contador += 1

def mayorque(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 > val2:
        val = 1
    write(cuad["temp"],val)
    contador += 1

def noigual(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 != val2:
        val = 1
    write(cuad["temp"],val)
    contador += 1

def yand(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 != 0 and val2 != 0:
        val = 1
    write(cuad["temp"],val)
    contador += 1

def yor(cuad):
    global contador
    val1 = leer(cuad["op1"])
    val2 = leer(cuad["op2"])
    val = 0
    if val1 != 0 or val2 != 0:
        val = 1
    write(cuad["temp"],val)
    contador += 1

# def retornar(cuad):
#     pass

def imprimir(cuad):
    global contador
    val = leer(cuad["temp"])
    print(val)
    contador += 1

operaciones = {
    'goto' : goto,
    'gotoV' : gotoV,
    'gotoF' : gotoF,
    '+' : mas,
    '-' : menos,
    '*' : por,
    '/' : entre,
    '=' : assignar,
    '==' : igual,
    '<' : menorque,
    '>' : mayorque,
    '!=' : noigual,
    'and' : yand,
    'or' : yor,
    # 'return' : retornar,
    'print' : imprimir
}

print("----Ejecucion de Programa----")
#Ejecucion
while contador < len(cuadruplos):
    actual = cuadruplos[contador]
    try:
        operaciones[actual["oper"]](actual)
    except KeyError:
        print("Error: Invalid operation", actual["oper"])
        exit(1)