import ply.yacc as yacc
import os
import codecs
import re
from anaLexico import tokens
from sys import stdin

#tokens Pasados= ['ID','NUMBER','PLUS','MINUS','MULT','SLASH',
#'AEQL','EQL','LESSTHAN','MORETHAN','LPAR','RPAR','LKEY','RKEY','LSQLBRK','RSQLBRK','COMMA','DOT','SEMICOLON']

precedence = (    #Preguntar que es precedence
    ('right', 'AEQL'),
    ('left', 'EQL','LESSTHAN', 'MORETHAN'), #No se si este hay que ponerlo
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'SLASH'),
    ('left', 'LPAR', 'RPAR')
)

def p_program(p):
    '''program = block'''
    print("program")
    #p[0] = program(p[1], "program")

def p_constDecl(p):
    '''constDecl = CONST constAssignmentList'''
    #p[0] = constDecl(p[2])
    print("constDecl")

def p_constDeclEmpty(p):
    '''constDecl = empty'''
    #p[0] = null()
    print("NULL")

def p_constAssignmentList(p):
    '''ID = NUMBER '''
    print("constAssignmentList 1")

def p_constAssignmentList2(p):
    '''constAssignmentList : constAssignmentList, ID = NUMBER '''
    print("constAssignmentList 2")

def varDecl1(p):
    ''' varDecl = VAR ID ;'''
    print("varDecl1")

def varDeclEmpty(p):
    ''' varDecl = empty'''
    print("NULL")

def identList1(p):
    '''identList : ID'''
    print("identList 1")

def identList2(p):
    '''identList : identList, ID'''
    print("identList 2")

def procDecl1(p):
    '''procDecl : procDecl , ID'''
    print("procDecl 1")

def procDeclEmpty(p):
    '''procDecl : empty'''
    print("NULL")

def statement1(p):
    '''statement : ID UPDATE expression'''
    print("statement1")

def statement2(p):
    '''statement : CALL ID'''
    print("statement2")

def statement3(p):
    '''statement : BEGIN statementList END'''
    print("statement3")

def statement4(p):
    '''statement : ID condition THEN statement'''
    print("statement4")

def statement5(p):
    '''statement : WHILE condition DO statement'''
    print("statement5")

def statementEmpty(p):
    '''statement : empty'''
    print("NULL")

def statementList1(p):
    '''statementList : statement'''
    print("statementList 1")

def statementList2(p):
    '''statementList : statementList ; statement'''
    print("statementList ")

#No agregue el de condition 1 y 2

def p_relation1(p):
    '''relation : ASSIGN'''
    print("relation 1")

def p_relation2(p):
    '''relation : NE'''
    print("relation 2")

def p_relation3(p):
    '''relation : LT'''
    print("relation 3")

def p_relation4(p):
    '''relation : GT'''
    print("relation 4")

def p_relation5(p):
    '''relation : LTE'''
    print("relation 5")

def p_relation6(p):
    '''relation : GTE'''
    print("relation 6")

def p_expression1(p):
    ''' expression : term'''
    print("expression 1")

def p_expression2(p):
    ''' expression : addingOperator term'''
    print("expression 2")

def p_expression3(p):
    ''' expression : expression addingOperator term'''
    print("expression 3")

def p_term1(p):
    '''term : factor'''
    print("term 1")

def p_term2(p):
    '''term : term multiplyingOperator factor'''
    print("term 2")

def p_multiplyingOperator1(p):
    ''' multiplyingOperator : TIMES'''
    print("multiplyingOperator 1")

def p_multiplyingOperator2(p):
    ''' multiplyingOperator : DIVIDE'''
    print("multiplyingOperator 2")

