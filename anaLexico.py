#Funciona para las palabras
import codecs
#Significa la libreria del sistema operativo
import os
#Las siguientes es para ver si funciona el analizador lexico
import re
import sys

import ply.lex as lex

#Se utiliza para comentar en python

#Tokens
tokens = ['ID','NUMINT','NUMFLOAT','STRING','PLUS','MINUS','MULT','SLASH','AEQL','EQL','LESSTHAN','NOTEQL','MORETHAN','LPAR','RPAR','LKEY','RKEY','LBRK','RBRK','COMMA','SEMICOLON']

reservadas = { #Investigar como implementar palabras reservadas
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
    'return' : 'RETURN'
}
tokens = tokens+list(reservadas.values())
#Definir los tokens
t_ignore = ' '
# t_BLANK = '\s'   Si se usa agregar a tokens
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
t_LBRK = r'\[' #Preguntar esto
t_RBRK = r'\]'
t_COMMA = r'\,'
# t_DOT = r'\.'    Si se usa agregar a tokens
t_SEMICOLON = r'\;'

#Detecta cuando es decimal
def t_NUMFLOAT(t):
     r'[+-]?[0-9]+\.[0-9]+'
     t.value = float(t.value)
     return t

#Detecta cuando es entero
def t_NUMINT(t):
     r'\d+'
     t.value = int(t.value)
     return t

#Detecta si es un id
def t_ID(t):
     r'[a-zA-Z][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value, 'ID')
     return t

def t_STRING(t):
    r'\".*\"'
    return t

#Detecta una nueva linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

#Detecta si hay un character que no es de los que definimos
def t_error(t):
    print("Character ilegal '%s' " % t.value [0])
    t.lexer.skip(1)

# file = sys.argv[1]
# directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
# fp = codecs.open(directorio,"r")
# cadena = fp. read()
# fp.close()

#Es necesario para que jale
analizador = lex.lex()
# En el caso de que tenga que meter mas abrir
# analizador.input(cadena)

# while True:
#     tok = analizador.token()       #35:04
#     if not tok : break
#     print(tok)