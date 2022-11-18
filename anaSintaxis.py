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
    '''funciones : funcionf MAIN SEMICOLON maines
                | MAIN SEMICOLON maines
    '''
def p_programa3(p):
    '''maines : mainf empty
              | empty
    '''
def p_variable1(p):
    '''varf : tipo varp'''

def p_variable2(p):
    '''varp : ID array varpp
            | ID varpp
    '''

def p_variable3(p):
    '''varpp : AEQL exp varppp
             | varppp
    '''

def p_variable4(p):
    '''varppp : COMMA varp
              | empty
    '''

def p_tipo(p):
    '''tipo : INT 
            | FLOAT 
    '''
def p_array(p):
    '''array : LBRK exp RBRK '''

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
    '''factor : LPAR exp RPAR 
              | PLUS varcte 
              | MINUS varcte 
              | varcte 
    '''

def p_varcte(p):
    '''varcte : ID
              | NUMFLOAT
              | NUMINT
    '''

def p_funcion1(p):
    '''funcionf : VOID funcionp
                | tipo funcionp
    '''

def p_funcion2(p):
    '''funcionp : ID LPAR funcionpp
    '''

def p_funcion3(p):
    '''funcionpp : tipo ID funcionppp
                | funcionpppp
    '''

def p_funcion4(p):
    '''funcionppp : COMMA funcionpp
                  | funcionpppp
    '''

def p_funcion5(p):
    '''funcionpppp : RPAR bloque
    '''

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

def p_estatuto(p):
    '''estatuto : asignacion
                | condif
                | conwhile
                | conddowhile
                | escritura
    '''

def p_asignacion(p):
    '''asignacion : ID AEQL exp 
    '''

def p_escritura1(p):
    '''escritura : PRINT LPAR escriturap
    '''

def p_escritura2(p):
    '''escriturap : expresion escriturapp
                  | STRING escriturapp
    '''

def p_escritura3(p):
    '''escriturapp : COMMA escriturap
                   | RPAR 
    '''

def p_condif1(p):
    '''condif : IF LPAR expresion RPAR bloque condifp
    '''

def p_condif2(p):
    '''condifp : ELSE bloque
               | empty
    '''

def p_condwhile(p):
    '''condwhile : WHILE LPAR expresion RPAR bloque
    '''

def p_conddowhile(p):
    '''conddowhile : DO bloque WHILE LPAR expresion RPAR
    '''
def p_expresion1(p):
    '''expresion : exp expresionp
    '''

def p_expresion2(p):
    '''expresionp : MORETHAN expresionpp
                  | LESSTHAN expresionpp
                  | EQL expresionpp
                  | NOTEQL expresionpp
    '''

def p_expresion3(p):
    '''expresionpp : exp
    '''

def p_main(p):
    '''mainf : bloque
    '''

def p_empty(p):
     'empty :'
     pass

# file = sys.argv[1]
# directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
# fp = codecs.open(directorio,"r")
# cadena = fp. read()
# fp.close()

parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
