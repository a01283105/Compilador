import codecs
#----------------#Libreria del Sistema Operativo#----------------#
import os
import re
#----------------#Systema#----------------#
import sys

import ply.lex as lex
#----------------#Tokens#----------------#
tokens = ['ID','NUMINT','NUMFLOAT','STRING','PLUS','MINUS','MULT','SLASH','AEQL','EQL','LESSTHAN','NOTEQL','MORETHAN','AND','OR','LPAR','RPAR','LKEY','RKEY','LBRK','RBRK','COMMA','SEMICOLON']

#----------------#Palabras Reservadas#----------------#
reservadas = { 
    'int':'INT',
    'float':'FLOAT',
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'do':'DO',
    'func':'FUNC',
    'print':'PRINT',
    'var':'VAR',
    'func':'FUNC',
    'main':'MAIN',
    'void' : 'VOID',
    'return' : 'RETURN',
    'and' : 'AND',
    'or' : 'OR'
}

#----------------#Juntar tokens y reservadas#----------------#
tokens = tokens+list(reservadas.values())
#----------------#Definicion de Tokens#----------------#
t_ignore = ' '
t_STRING = r'"(.*?)"'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_SLASH = r'\/'
t_AEQL = r'\='
t_EQL = r'\=='
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_NOTEQL = r'\!='
t_LPAR = r'\('
t_RPAR = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LBRK = r'\['
t_RBRK = r'\]'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

#----------------#Detecta cuando es flotante#----------------#
def t_NUMFLOAT(t):
     r'[+-]?[0-9]+\.[0-9]+'
     t.value = float(t.value)
     return t

#----------------#Detecta cuando es entero#----------------#
def t_NUMINT(t):
     r'[-]?[0-9]+'
     t.value = int(t.value)
     return t

#----------------#Detecta si es un id#----------------#
def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value, 'ID')
     return t

#----------------#Detecta una nueva linea#----------------#
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#----------------#Detecta si hay un character que no es de los que definimos----------------#
def t_error(t):
    print("Character ilegal '%s' " % t.value [0])
    t.lexer.skip(1)

#----------------#Por si se tiene que correr individual#----------------#
# file = sys.argv[1]
# directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
# fp = codecs.open(directorio,"r")
# cadena = fp. read()
# fp.close()

#----------------#Funcion para crear el lexer#----------------#
analizador = lex.lex()

#----------------#Por si se tiene que corren individual#----------------#
# analizador.input(cadena)

# while True:
#     tok = analizador.token()
#     if not tok : break
#     print(tok)