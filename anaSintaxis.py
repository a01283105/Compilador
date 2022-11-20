import ply.yacc as yacc
import os
import codecs
import re
import sys
from anaLexico import tokens
from sys import stdin

#tokens Pasados= ['ID','NUMBER','PLUS','MINUS','MULT','SLASH',
#'AEQL','EQL','LESSTHAN','MORETHAN','LPAR','RPAR','LKEY','RKEY','LSQLBRK','RSQLBRK','COMMA','DOT','SEMICOLON']

precedence = (    #Preguntar que es precedence
    ('right', 'AEQL'),
    ('left', 'EQL','LESSTHAN', 'MORETHAN', 'NOTEQL'), #No se si este hay que ponerlo
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'SLASH'),
    ('left', 'LPAR', 'RPAR')
)

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
    '''maines : mainf
              | empty
    '''
#Var
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
              | SEMICOLON varpppp empty
    '''

def p_variable5(p):
    '''varpppp : varf
               | empty
    '''
#Tipo
def p_tipo(p):
    '''tipo : INT
            | FLOAT
    '''
#Array
def p_array(p):
    '''array : LBRK exp RBRK'''
#Exp
def p_exp(p):
    '''exp : termino PLUS exp
           | termino MINUS exp
           | termino empty
    '''
#Termino
def p_termino(p):
    '''termino : factor MULT termino
               | factor SLASH termino
               | factor empty
    '''
#Factor
def p_factor(p):
    '''factor : LPAR exp RPAR
              | PLUS varcte
              | MINUS varcte
              | varcte
    '''
#Varcte
def p_varcte(p):
    '''varcte : ID
              | NUMFLOAT
              | NUMINT
              | llamafunc
    '''
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
    '''funcionf : VOID ID LPAR funcionp RPAR bloque SEMICOLON
                | tipo ID LPAR funcionp RPAR bloque RETURN LPAR exp RPAR SEMICOLON funcionpppp
    '''

def p_funcion3(p):
    '''funcionp : funcionpp
                | empty
    '''

def p_funcion4(p):
    '''funcionpp : tipo ID funcionppp
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
                  | ID asignacionp
    '''

def p_asignacion2(p):
    '''asignacionp : AEQL exp SEMICOLON
    '''
#Escritura
def p_escritura1(p):
    '''escritura : PRINT LPAR escriturap
    '''

def p_escritura2(p):
    '''escriturap : exp escriturapp
                  | STRING escriturapp
    '''

def p_escritura3(p):
    '''escriturapp : COMMA escriturap
                   | RPAR SEMICOLON
    '''
#Condif
def p_condif1(p):
    '''condif : IF LPAR expresion RPAR bloque condifp
    '''

def p_condif2(p):
    '''condifp : ELSE bloque SEMICOLON
               | SEMICOLON
    '''
#Condwhile
def p_condwhile(p):
    '''condwhile : WHILE LPAR expresion RPAR bloque SEMICOLON
    '''
#Conddowhile
def p_conddowhile(p):
    '''conddowhile : DO bloque WHILE LPAR expresion RPAR SEMICOLON
    '''
#Expresion
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

