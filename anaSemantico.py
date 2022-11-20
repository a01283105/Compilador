# txt = " "
# cont = 0
# def incrementaContador():
#     global cont
#     cont+=1
#     return "%d"%cont


# class Nodo():
#     pass

# class programa(Nodo):
#     '''programa : VAR SEMICOLON variable'''

# class programa1(Nodo):
#     '''variable : varf FUNC SEMICOLON funciones
#                 | FUNC SEMICOLON funciones
#     '''

# class programa2(Nodo):
#     '''funciones : funcionf MAIN SEMICOLON maines
#                 | MAIN SEMICOLON maines
#     '''

# class programa3(Nodo):
#     '''maines : mainf
#               | empty
#     '''
# #Var
# class variable1(Nodo):
#     '''varf : tipo varp'''

# class variable2(Nodo):
#     '''varp : ID array varpp
#             | ID varpp
#     '''

# class variable3(Nodo):
#     '''varpp : AEQL exp varppp
#              | varppp
#     '''

# class variable4(Nodo):
#     '''varppp : COMMA varp
#               | SEMICOLON varpppp empty
#     '''

# class variable5(Nodo):
#     '''varpppp : varf
#                | empty
#     '''
# #Tipo
# class tipo(Nodo):
#     '''tipo : INT
#             | FLOAT
#     '''
# #Array
# class array(Nodo):
#     '''array : LBRK exp RBRK'''
# #Exp
# class exp(Nodo):
#     '''exp : termino PLUS exp
#            | termino MINUS exp
#            | termino empty
#     '''
# #Termino
# class termino(Nodo):
#     '''termino : factor MULT termino
#                | factor SLASH termino
#                | factor empty
#     '''
# #Factor
# class factor(Nodo):
#     '''factor : LPAR exp RPAR
#               | PLUS varcte
#               | MINUS varcte
#               | varcte
#     '''
# #Varcte
# class varcte(Nodo):
#     '''varcte : ID
#               | NUMFLOAT
#               | NUMINT
#     '''
# #FUNCION
# class funcion1(Nodo):
#     '''funcionf : VOID ID LPAR funcionp RPAR bloque SEMICOLON
#                 | tipo ID LPAR funcionp RPAR bloque RETURN LPAR exp RPAR SEMICOLON funcionpppp
#     '''

# class funcion3(Nodo):
#     '''funcionp : funcionpp
#                 | empty
#     '''

# class funcion4(Nodo):
#     '''funcionpp : tipo ID funcionppp
#     '''

# class funcion5(Nodo):
#     '''funcionppp : COMMA funcionpp
#                   | empty
#     '''

# class funcion6(Nodo):
#     '''funcionpppp : funcionf
#                    | empty
#     '''
# #BLOQUE
# class bloque1(Nodo):
#     '''bloque : LKEY bloquep
#               | LKEY bloqueppp
#     '''

# class bloque2(Nodo):
#     '''bloquep : estatuto bloquepp
#     '''

# class bloque3(Nodo):
#     '''bloquepp : bloquep
#                 | bloqueppp
#     '''

# class bloque4(Nodo):
#     '''bloqueppp : RKEY
#     '''
# #Estatuto
# class estatuto(Nodo):
#     '''estatuto : asignacion
#                 | condif
#                 | condwhile
#                 | conddowhile
#                 | escritura
#     '''
# #Asignacion
# class asignacion(Nodo):
#     '''asignacion : ID AEQL exp SEMICOLON
#     '''
# #Escritura
# class escritura1(Nodo):
#     '''escritura : PRINT LPAR escriturap
#     '''

# class escritura2(Nodo):
#     '''escriturap : exp escriturapp
#                   | STRING escriturapp
#     '''

# class escritura3(Nodo):
#     '''escriturapp : COMMA escriturap
#                    | RPAR SEMICOLON
#     '''
# #Condif
# class condif1(Nodo):
#     '''condif : IF LPAR expresion RPAR bloque condifp
#     '''

# class condif2(Nodo):
#     '''condifp : ELSE bloque SEMICOLON
#                | SEMICOLON
#     '''
# #Condwhile
# class condwhile(Nodo):
#     '''condwhile : WHILE LPAR expresion RPAR bloque SEMICOLON
#     '''
# #Conddowhile
# class conddowhile(Nodo):
#     '''conddowhile : DO bloque WHILE LPAR expresion RPAR SEMICOLON
#     '''
# #Expresion
# class expresion1(Nodo):
#     '''expresion : exp expresionp
#     '''

# class expresion2(Nodo):
#     '''expresionp : MORETHAN expresionpp
#                   | LESSTHAN expresionpp
#                   | EQL expresionpp
#                   | NOTEQL expresionpp
#     '''

# class expresion3(Nodo):
#     '''expresionpp : exp
#     '''

# class main(Nodo):
#     '''mainf : bloque SEMICOLON
#     '''

# class error(Nodo):
#     print("Error de Sintaxis",p)
#     print("error en la linea "+ str(p.lineno))


# class empty(Nodo):
#      'empty :'
#      pass