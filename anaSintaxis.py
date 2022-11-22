import ply.yacc as yacc
import os
import codecs
import re
import sys
from anaLexico import tokens
from sys import stdin
from cuad import *

# Tabla de match
# {
# "tipo1": {
#    "tipo2": {
#         "operando": "tipo de salida"
#         }
#    }
# }
# ejemplo de llamada
# tablaTipos["tipo1"]["tipo2"]["operador"]

watcherT = ""
watcherF = "global"
tablaTipos = {}

tablaTipos["int"] = {"int": {}, "float": {}, "bool": {}}
tablaTipos["float"] = {"int": {}, "float": {}, "bool": {}}
tablaTipos["bool"] = {"int": {}, "float": {}, "bool": {}}

tablaTipos["int"]["int"]["="] = "int"
tablaTipos["int"]["int"]["+"] = "int"
tablaTipos["int"]["int"]["-"] = "int"
tablaTipos["int"]["int"]["*"] = "int"
tablaTipos["int"]["int"]["/"] = "float"
tablaTipos["int"]["int"]["=="] = "int"
tablaTipos["int"]["int"]["!="] = "int"
tablaTipos["int"]["int"]["<"] = "int"
tablaTipos["int"]["int"][">"] = "int"
tablaTipos["int"]["int"]["and"] = "int"
tablaTipos["int"]["int"]["or"] = "int"

tablaTipos["int"]["float"]["="] = "float"
tablaTipos["int"]["float"]["+"] = "float"
tablaTipos["int"]["float"]["-"] = "float"
tablaTipos["int"]["float"]["*"] = "float"
tablaTipos["int"]["float"]["/"] = "float"
tablaTipos["int"]["float"]["=="] = "int"
tablaTipos["int"]["float"]["!="] = "int"
tablaTipos["int"]["float"]["<"] = "int"
tablaTipos["int"]["float"][">"] = "int"
tablaTipos["int"]["float"]["and"] = "error"
tablaTipos["int"]["float"]["or"] = "error"

# tablaTipos["int"]["bool"]["="] = "error"
# tablaTipos["int"]["bool"]["+"] = "error"
# tablaTipos["int"]["bool"]["-"] = "error"
# tablaTipos["int"]["bool"]["*"] = "error"
# tablaTipos["int"]["bool"]["/"] = "error"
# tablaTipos["int"]["bool"]["=="] = "bool"
# tablaTipos["int"]["bool"]["!="] = "bool"
# tablaTipos["int"]["bool"]["<"] = "error"
# tablaTipos["int"]["bool"][">"] = "error"

tablaTipos["float"]["int"]["="] = "float"
tablaTipos["float"]["int"]["+"] = "float"
tablaTipos["float"]["int"]["-"] = "float"
tablaTipos["float"]["int"]["*"] = "float"
tablaTipos["float"]["int"]["/"] = "float"
tablaTipos["float"]["int"]["=="] = "int"
tablaTipos["float"]["int"]["!="] = "int"
tablaTipos["float"]["int"]["<"] = "int"
tablaTipos["float"]["int"][">"] = "int"
tablaTipos["float"]["int"]["and"] = "error"
tablaTipos["float"]["int"]["or"] = "error"

tablaTipos["float"]["float"]["="] = "float"
tablaTipos["float"]["float"]["+"] = "float"
tablaTipos["float"]["float"]["-"] = "float"
tablaTipos["float"]["float"]["*"] = "float"
tablaTipos["float"]["float"]["/"] = "float"
tablaTipos["float"]["float"]["=="] = "int"
tablaTipos["float"]["float"]["!="] = "int"
tablaTipos["float"]["float"]["<"] = "int"
tablaTipos["float"]["float"][">"] = "int"
tablaTipos["float"]["float"]["and"] = "error"
tablaTipos["float"]["float"]["or"] = "error"

# tablaTipos["float"]["bool"]["="] = "error"
# tablaTipos["float"]["bool"]["+"] = "error"
# tablaTipos["float"]["bool"]["-"] = "error"
# tablaTipos["float"]["bool"]["*"] = "error"
# tablaTipos["float"]["bool"]["/"] = "error"
# tablaTipos["float"]["bool"]["=="] = "bool"
# tablaTipos["float"]["bool"]["!="] = "bool"
# tablaTipos["float"]["bool"]["<"] = "error"
# tablaTipos["float"]["bool"][">"] = "error"

# tablaTipos["bool"]["int"]["="] = "error"
# tablaTipos["bool"]["int"]["+"] = "error"
# tablaTipos["bool"]["int"]["-"] = "error"
# tablaTipos["bool"]["int"]["*"] = "error"
# tablaTipos["bool"]["int"]["/"] = "error"
# tablaTipos["bool"]["int"]["=="] = "bool"
# tablaTipos["bool"]["int"]["!="] = "bool"
# tablaTipos["bool"]["int"]["<"] = "error"
# tablaTipos["bool"]["int"][">"] = "error"

# tablaTipos["bool"]["float"]["="] = "error"
# tablaTipos["bool"]["float"]["+"] = "error"
# tablaTipos["bool"]["float"]["-"] = "error"
# tablaTipos["bool"]["float"]["*"] = "error"
# tablaTipos["bool"]["float"]["/"] = "error"
# tablaTipos["bool"]["float"]["=="] = "bool"
# tablaTipos["bool"]["float"]["!="] = "bool"
# tablaTipos["bool"]["float"]["<"] = "error"
# tablaTipos["bool"]["float"][">"] = "error"

# tablaTipos["bool"]["bool"]["="] = "bool"
# tablaTipos["bool"]["bool"]["+"] = "error"
# tablaTipos["bool"]["bool"]["-"] = "error"
# tablaTipos["bool"]["bool"]["*"] = "error"
# tablaTipos["bool"]["bool"]["/"] = "error"
# tablaTipos["bool"]["bool"]["=="] = "bool"
# tablaTipos["bool"]["bool"]["!="] = "bool"
# tablaTipos["bool"]["bool"]["<"] = "error"
# tablaTipos["bool"]["bool"][">"] = "error"


# precedence = (    #Preguntar que es precedence
#     ('right', 'AEQL'),
#     ('left', 'EQL','LESSTHAN', 'MORETHAN', 'NOTEQL'), #No se si este hay que ponerlo
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'MULT', 'SLASH'),
#     ('left', 'LPAR', 'RPAR')
# )

stackOperandos = []
stackOperadores = []
stackSaltos = []
stackTipos = []
cuadruplos = []
#Contador de cuadruplos
contador = 0

tablaV = {"global":{"type":"void","var":{}}}

#<PROGRAMA>
def p_programa(p):
    '''programa : VAR SEMICOLON variable FUNC SEMICOLON funciones MAIN SEMICOLON maines debug'''

def p_debug(p):
    ''' debug : 
    '''
    cont = 0
    print(tablaV)
    print(stackOperadores)
    print(stackOperandos)
    print(stackSaltos)
    print(stackTipos)
    for x in cuadruplos:
        print(cont)
        x.mistring()
        cont += 1

def p_programa1(p):
    '''variable : varf 
                | empty
    '''

def p_programa2(p):
    '''funciones : funcionf 
                | empty
    '''

def p_programa3(p):
    '''maines : mainf
              | empty
    '''
#Var
def p_variable1(p):
    '''varf : tipo varp'''

def p_variable2(p):
    '''varp : ID array varpp
            | ID varid varpp
    '''

def p_varid(p):
    ''' varid :
    '''
    if p[-1] not in tablaV[watcherF]["var"]:
        tablaV[watcherF]["var"][p[-1]] = {"tipo" : watcherT}
    else:
        print("La variable ya existe")
        sys.exit(1)

def p_variable3(p):
    '''varpp : varppp
    '''

def p_variable4(p):
    '''varppp : COMMA varp
              | SEMICOLON varpppp empty
    '''

def p_variable5(p):
    '''varpppp : varf
               | empty
    '''
#Tipo
def p_tipo(p):
    '''tipo : INT funciontipo
            | FLOAT funciontipo
    '''

#Array
def p_array(p):
    '''array : LBRK exp RBRK'''
#Exp
def p_exp(p):
    '''exp : termino cuadexp auxexp
    '''

def p_cuadexp(p):
    '''cuadexp :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperadores) != 0:
        if stackOperadores[-1] == '+':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == '-':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1

def p_auxexp(p):
    '''auxexp : PLUS meteopdores exp
              | MINUS meteopdores exp
              | empty
    '''
#Termino
def p_termino(p):
    '''termino : factor cuadtermino auxtermino
    '''

def p_cuadtermino(p):
    '''cuadtermino :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperadores) != 0:
        if stackOperadores[-1] == '*':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == '/':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1

def p_auxtermino(p):
    '''auxtermino : MULT meteopdores termino
                  | SLASH meteopdores termino
                  | empty
    '''
#Factor
def p_factor(p):
    '''factor : LPAR expresionandor RPAR
              | varcte
    '''
#Varcte
def p_varcte(p):
    '''varcte : ID meteopandos
              | NUMFLOAT meteconst
              | NUMINT meteconst
              | llamafunc
    '''

def p_meteconst(p):
    '''meteconst :
    '''
    global stackOperandos,stackTipos
    if isinstance(p[-1],int):
        stackOperandos.append(p[-1])
        stackTipos.append("int")
    elif isinstance(p[-1],float):
        stackOperandos.append(p[-1])
        stackTipos.append("float")
        

#Llamafunc

def p_llamafunc1(p):
    '''llamafunc : ID LPAR llamafuncp
    '''

def p_llamafunc2(p):
    '''llamafuncp : llamafuncpp
                 | llamafuncpppp
    '''

def p_llamafunc3(p):
    '''llamafuncpp : tipo ID llamafuncppp 
    '''
def p_llamafunc4(p):
    '''llamafuncppp : COMMA llamafuncpp
                    | llamafuncpppp
    '''
def p_llamafunc5(p):
    '''llamafuncpppp : RPAR 
    '''

#FUNCION
def p_funcion1(p):
    '''funcionf : VOID funciontipo ID funcionid LPAR funcionp RPAR bloque SEMICOLON funcionpppp
                | tipo ID funcionid LPAR funcionp RPAR bloque RETURN LPAR exp RPAR SEMICOLON funcionpppp
    '''

def p_funciontipo(p):
    ''' funciontipo :
    '''
    global watcherT 
    watcherT = p[-1]

def p_funcionName(p):
    ''' funcionid : 
    '''
    global watcherF
    watcherF = p[-1]
    if p[-1] not in tablaV :
        if watcherT == "void" :
            tablaV[p[-1]] = {"type":"void","var":{}}
        else :
            tablaV[p[-1]] = {"type":watcherT,"var":{}}
    else:
        print("Esta funcion ya fue declarada")
        sys.exit(1)
def p_funcion3(p):
    '''funcionp : funcionpp
                | empty
    '''

def p_funcion4(p):
    '''funcionpp : tipo ID varid funcionppp
    '''

def p_funcion5(p):
    '''funcionppp : COMMA funcionpp
                  | empty
    '''

def p_funcion6(p):
    '''funcionpppp : funcionf
                   | empty
    '''
#BLOQUE
def p_bloque1(p):
    '''bloque : LKEY bloquep
              | LKEY bloqueppp
    '''

def p_bloque2(p):
    '''bloquep : estatuto bloquepp
    '''

def p_bloque3(p):
    '''bloquepp : bloquep
                | bloqueppp
    '''

def p_bloque4(p):
    '''bloqueppp : RKEY
    '''
#Estatuto
def p_estatuto(p):
    '''estatuto : asignacion
                | condif
                | condwhile
                | conddowhile
                | escritura
                | llamafunc SEMICOLON
    '''
#Asignacion
def p_asignacion(p):
    '''asignacion : ID array asignacionp
                  | ID meteopandos asignacionp
    '''

def p_asignacion2(p):
    '''asignacionp : AEQL meteopdores expresionandor cuadass SEMICOLON 
    '''

def p_expresionandor(p):
    '''expresionandor : expresion cuadexpresionandor auxandor
    '''

def p_cuadexpresionandor(p):
    '''cuadexpresionandor :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperadores) != 0:
        if stackOperadores[-1] == 'and':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == 'or':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1

def p_auxandor(p):
    '''auxandor : AND meteopdores expresionandor
                | OR meteopdores expresionandor
                | empty
    '''

def p_cuadass(p):
    ''' cuadass :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    oper = stackOperadores.pop()
    operd = stackOperandos.pop()
    operi = stackOperandos.pop()
    tipod = stackTipos.pop()
    tipoi = stackTipos.pop()
    if tipoi != tipod:
        print("El tipo no es el mismo")
        sys.exit(1)
    else:
        dat = cuad(oper,operd,None,operi)
        cuadruplos.append(dat)
        contador += 1

#Mete operadores
def p_meteopdores(p):
    ''' meteopdores :
    '''
    global stackOperadores
    stackOperadores.append(p[-1])

def p_meteopandos(p):
    ''' meteopandos :
    '''
    global stackOperandos, stackTipos
    if p[-1] in tablaV[watcherF]["var"]:
        stackOperandos.append(p[-1])
        stackTipos.append(tablaV[watcherF]["var"][p[-1]]["tipo"])
    elif p[-1] in tablaV["global"]["var"]:
        stackOperandos.append(p[-1])
        stackTipos.append(tablaV["global"]["var"][p[-1]]["tipo"])
    else:
        print("Esta variable no existe")
        sys.exit(1)

#Escritura
def p_escritura1(p):
    '''escritura : PRINT meteopdores LPAR escriturap
    '''

def p_escritura2(p):
    '''escriturap : expresion cuadescritura escriturapp
                  | STRING escriturapp
    '''

def p_cuadescritura(p):
    '''cuadescritura :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperadores) != 0:
        if stackOperadores[-1] == 'print':
            oper = stackOperadores.pop()
            operi = stackOperandos.pop()
            cuadruplos.append(cuad(oper,None,None,operi))
            stackTipos.pop()
            contador += 1

def p_escritura3(p):
    '''escriturapp : COMMA escriturap
                   | RPAR SEMICOLON
    '''
#Condif
def p_condif1(p):
    '''condif : IF LPAR expresion cuadcondif RPAR bloque condifp cuadrellenoif
    '''

def p_cuadcondif(p):
    '''cuadcondif :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperandos) != 0:
        if stackTipos[-1] == 'int':
            stackTipos.pop()
            cuadruplos.append(cuad("gotoF",stackOperandos.pop(),None, None))
            stackSaltos.append(contador)
            contador += 1

def p_cuadrellenoif(p):
    '''cuadrellenoif :
    '''
    salto = stackSaltos.pop()
    cuadruplos[salto].temp = contador


def p_condif2(p):
    '''condifp : ELSE cuadconifelse bloque SEMICOLON
               | SEMICOLON
    '''

def p_cuadconifelse(p):
    '''cuadconifelse :
    '''
    global contador
    cuadruplos.append(cuad("goto",None, None, None))
    salto = stackSaltos.pop()
    stackSaltos.append(contador)
    contador += 1
    cuadruplos[salto].temp = contador

#Condwhile
def p_condwhile(p):
    '''condwhile : WHILE LPAR guardarsal expresion quadcondwhile RPAR bloque rellenocondwhile SEMICOLON
    '''

def p_guardarsal(p):
    '''guardarsal :
    '''
    stackSaltos.append(contador)

def p_quadcondwhile(p):
    '''quadcondwhile :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperandos) != 0:
        if stackTipos[-1] == 'int':
            stackTipos.pop()
            cuadruplos.append(cuad("gotoF",stackOperandos.pop(),None, None))
            stackSaltos.append(contador)
            contador += 1
        
def p_rellenocondwhile(p):
    '''rellenocondwhile :
    '''
    global contador
    saltof = stackSaltos.pop()
    saltorev = stackSaltos.pop()
    cuadruplos.append(cuad("goto",None, None, saltorev))
    contador += 1
    cuadruplos[saltof].temp = contador

#Conddowhile
def p_conddowhile(p):
    '''conddowhile : DO guardardowhile bloque WHILE LPAR expresion quadconddowhile RPAR SEMICOLON
    '''

def p_guardardowhile(p):
    '''guardardowhile :
    '''
    stackSaltos.append(contador)

def p_quadconddowhile(p):
    '''quadconddowhile :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperandos) != 0:
        if stackTipos[-1] == 'int':
            stackTipos.pop()
            cuadruplos.append(cuad("gotoV",stackOperandos.pop(),None, stackSaltos.pop()))
            contador += 1

#Expresion
def p_expresion1(p):
    '''expresion : exp cuadexpresion expresionp 
    '''
def p_cuadexpresion(p):
    '''cuadexpresion :
    '''
    global stackOperadores,stackOperandos,stackTipos,cuadruplos,contador
    if len(stackOperadores) != 0:
        if stackOperadores[-1] == '>':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == '<':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == '==':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
        elif stackOperadores[-1] == '!=':
            oper = stackOperadores.pop()
            operd = stackOperandos.pop()
            operi = stackOperandos.pop()
            tipod = stackTipos.pop()
            tipoi = stackTipos.pop()
            if tablaTipos[tipoi][tipod][oper] != "error":
                stackTipos.append(tablaTipos[tipoi][tipod][oper])
                cuadruplos.append(cuad(oper,operi,operd,"t"+str(contador)))
                stackOperandos.append("t"+str(contador))
                contador += 1
def p_expresion2(p):
    '''expresionp : MORETHAN meteopdores expresion
                  | LESSTHAN meteopdores expresion
                  | EQL meteopdores expresion
                  | NOTEQL meteopdores expresion
                  | empty
    '''


def p_main(p):
    '''mainf : bloque SEMICOLON
    '''

def p_error(p):
    print("Error de Sintaxis",p)
    print("error en la linea "+ str(p.lineno))


def p_empty(p):
     'empty :'
     p[0] = None
     pass

# file = sys.argv[1]
# directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
# fp = codecs.open(directorio,"r")
# cadena = fp. read()
# fp.close()

parser = yacc.yacc()
 
# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)


if __name__ == '__main__':
    if(len(sys.argv) > 1):
            file = sys.argv[1]
            try:
                f = open(file, 'r')
                data = f.read()
                f.close()
                if (yacc.parse(data, tracking=True) == "PROGRAMA COMPILADO"):
                    print("Sintaxis valida")
            except EOFError:
                print(EOFError)
    else:
        print("No existe el archivo")

