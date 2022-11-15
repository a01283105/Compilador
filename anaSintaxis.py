import ply.yacc as yacc
import os
import codecs
import re
from anaLexico.py import tokens
from sys import stdin

precedence = (
    (),
    ()
)