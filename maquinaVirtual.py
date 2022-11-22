import ply.yacc as yacc
import os
import codecs
import re
import sys
from anaLexico import tokens
from sys import stdin
from cuad import *
import json

archivo = open("Necesario.json")
tablaV = json.load(archivo)
archivo.close()

