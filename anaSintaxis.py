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

#<PROGRAMA>
def p_programa(p):
    '''programa : VAR SEMICOLON variable'''

def p_programa1(p):
    '''variable : varf FUNC SEMICOLON funciones
                | FUNC SEMICOLON funciones
    '''
def p_programa2(p):
    '''funciones : funcionF MAIN SEMICOLON maines
                | MAIN SEMICOLON maines
    '''
def p_programa3(p):
    '''maines : mainf empty
              | empty
    '''
def variable1(p):
    '''varf : tipo varp'''

def variable2(p):
    '''varp : ID array varpp
            | ID varpp
    '''

def variable3(p):
    '''varpp : AEQL exp varppp
             | varppp
    '''

def variable4(p):
    '''varppp : COMMA varp
              | empty
    '''

def p_tipo1(p):
    '''tipo : INT empty
            | FLOAT empty
    '''
def p_array(p):
    '''array : LBRK exp RBRK empty'''

def p_exp(p):
    '''exp : termino PLUS exp
           | termino MINUS exp
           | termino empty
    '''

def p_termino(p):
    '''termino : factor MULT termino
               | factor SLASH termino
               | factor empty
    '''

def p_factor(p):
    '''factor : termino PLUS exp
              | 
    '''
    

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
