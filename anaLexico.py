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
tokens = ['ID','NUMBER','BLANK','PLUS','MINUS','MULT','SLASH','AEQL','EQL','LESSTHAN','MORETHAN','LPAR','RPAR','LKEY','RKEY','LSQLBRK','RSQLBRK','COMMA','DOT','SEMICOLON']

reservadas = { #Investigar como implementar palabras reservadas
    'int':'INT',
    'float':'FLOAT',
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'do':'DO',
    'func':'FUNC'
}
tokens = tokens+list(reservadas.values())
#Definir los tokens
t_ignore = '[\t\n]'
t_BLANK = '\s'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_SLASH = r'/'
t_AEQL = r'\='
t_EQL = r'\=\='
t_LESSTHAN = r'\<'
t_MORETHAN = r'\>'
t_LPAR = r'\('
t_RPAR = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LSQLBRK = r'\[' #Preguntar esto
t_RSQLBRK = r'\]'
t_COMMA = r'\,'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
#Detecta si es un id
def t_ID(t):
     r'[A-Za-z_][A-Za-z_0-9]*'
     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Detecta cuando es decimal
def t_FLOAT(t):
     r'\d+\.\d+'
     try:
        t.value = float(t.value)
     except ValueError:
        print("El valor del Float es muy grande %d",t.value)
        t.value = 0
     return t

#Detecta cuando es entero
def t_INT(t):
     r'0|[1-9][0-9]*'
     try:
        t.value = int(t.value)
     except ValueError:
        print("El valor del Int es muy grande %d",t.value)
        t.value = 0
     return t

#Detecta si hay un character que no es de los que definimos
def t_error(t):
    print("caracter ilegal '%s' " % t.value [0])
    t.lexer.skip(1)

file = sys.argv[1]
directorio = f'D:\deibo\Documents\CompiRepo\Compilador\Tests\{file} '  #Colocar el directorio para ver donde estara el archivo que se va a analizar
fp = codecs.open(directorio,"r")
cadena = fp. read()
fp.close()

#Se dice que lo de abajo es lo unico que se necesita para que jale
analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.token()       #35:04
    if not tok : break
    print(tok)