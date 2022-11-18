import ply.yacc as yacc
import os
import codecs
import re
import sys
from anaLexico import tokens
from sys import stdin

#tokens Pasados= ['ID','NUMBER','PLUS','MINUS','MULT','SLASH',
#'AEQL','EQL','LESSTHAN','MORETHAN','LPAR','RPAR','LKEY','RKEY','LSQLBRK','RSQLBRK','COMMA','DOT','SEMICOLON']

# precedence = (    #Preguntar que es precedence
#     ('right', 'AEQL'),
#     ('left', 'EQL','LESSTHAN', 'MORETHAN'), #No se si este hay que ponerlo
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'MULT', 'SLASH'),
#     ('left', 'LPAR', 'RPAR')
# )

# def p_programa(p):
#     'programa : VAR SEMICOLON variable'
#     print("program")
#     p[0] = p[3]

# def p_programa1(p):
#     'variable : vari funciones'
#     print("program1")
#     p[0] = p[1],p[2]

# def p_programa2(p):
#     'variable : FUNC SEMICOLON funciones'
#     print("program2")
#     p[0] = p[3]

# def p_programa3(p):
#     'funciones : '
#     print("program2")
#     p[0] = p[3]

def p_tipo1(p):
    'tipo : INT'
    print("tipo1")
    p[0] = p[1]

def p_tipo2(p):
    'tipo : FLOAT'
    print("tipo2")
    p[0] = p[1]

def p_empty(p):
     'empty :'
     pass

file = sys.argv[1]
directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
fp = codecs.open(directorio,"r")
cadena = fp. read()
fp.close()

parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
