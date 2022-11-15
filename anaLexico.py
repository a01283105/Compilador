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
tokens = ['ID','NUMBER','PLUS','MINUS','MULT','SLASH','AEQL','EQL','LESSTHAN','MORETHAN','LPAR','RPAR','LKEY','RKEY','LSQLBRK','RSQLBRK','COMMA','DOT','SEMICOLON']

reservadas = {
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
t_ignore = '\t'
t_PLUS = r'\+'
t_MINUS = r'\-'
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
t_LSQLBRK = r'\['
t_RSQLBRK = r'\]'
t_COMMA = r'\,'
t_DOT = r'\.'
t_SEMICOLON = r'\;'
#Detecta si es un id
def t_ID(t):
     r'[a-za-Z_] [a-za-Z0-9_]*'
     return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
     r'\d+'
     return t

#Detecta cuando es entero
def t_INT(t):
     r'\d+'
     try:
        t.value = int(t.value)
     except ValueError:
        print("El valor del Int es muy grande %d",t.value)
        t.value = 0
     return t
#Detecta cuando es decimal
def t_FLOAT(t):
     try:
        t.value = float(t.value)
     except ValueError:
        print("El valor del Float es muy grande %d",t.value)
        t.value = 0
     return t

#Detecta si hay un character que no es de los que definimos
def t_error(t):
    print("caracter ilegal '%s' " % t.value [0])
    t.lexer.skip(1)

def buscarFicheros (directorio):   # 42.10
     ficheros = []
     numArchivo = ''
     respuesta = False
     cont = 1
     for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

     for file in files:
         print(str(cont) + ". " + file)
         cont = cont+1

     while respuesta == False:
         numArchivo = input('\nNumero del test: ')  #Se cambio raw input por input
         for file in files:
             if file == files[int(numArchivo)-1]:
                 respuesta = True
                 break

     print("Has escogido \"%S\" \n") %files [int (numArchivo)-1]

     return files [int(numArchivo)-11]



directorio = 'D:\deibo\Documents\Compilador\Tests\ ' #Colocar el directorio para ver donde estara el archivo que se va a analizar
archivo = buscarFicheros(directorio) 
test = directorio + archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp. read()
fp.close()

#Se dice que lo de abajo es lo unico que se necesita para que jale
analizador = lex.lex()

analizador.input(cadena)

while True:
    tok = analizador.tokens()       #35:04
    if not tok : break
    print(tok)