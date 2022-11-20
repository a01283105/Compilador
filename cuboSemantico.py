
import sys
from enum import Enum


class Operadores(Enum):
    SUMA = '+'
    RESTA = '-'
    MULTIPLICACION = '*'
    DIVISION = '/'
    MAYORQUE = '>'
    MENORQUE = '<'
    NOIGUAL = '!='
    IGUAL = '=='
    ASIGNACION = '='
    RETURN = 'return'

class cuboSemantico:
    def __init__(self):
        self.cuboSemantico = {
            #Operadores de operaciones
            Operadores.SUMA: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'string'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'string'
                },
                'string': {
                    'int': 'string',
                    'float': 'string',
                    'string': 'string'
                }
            },
            Operadores.RESTA: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            Operadores.MULTIPLICACION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },

            Operadores.DIVISION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            #Operadores Booleanos
            Operadores.MAYORQUE: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },

            Operadores.MENORQUE: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            Operadores.IGUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            },
            Operadores.NOIGUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'err',
                    'string': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'bool'
                }
            },
            #De asignacion
            Operadores.ASIGNACION: {
                'int': {
                    'int': 'int',
                    'float': 'int',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            }, #Return
            Operadores.RETURN: {
                'int': {
                    'int': 'int',
                    'float': 'err',
                    'string': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            }
        }      
        #Funcion
        def semantics(self, opIzquierda, opDerecha, operador):
            '''
            Will determine if given two types of variables and an operador, the operation will be valid or not
            :param opIzquierda: type of left variable of operation
            :param opDerecha: type of right variable of operation
            :param operador: operador given for the operation
            '''
            if 'err' not in self.cuboSemantico[opIzquierda][opDerecha][operador]:
                return self.cuboSemantico[opIzquierda][opDerecha][operador]
            raise TypeError("Unable to apply operador {} to types {} and {}".format(operador, opIzquierda, opDerecha))