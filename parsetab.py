
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AEQL BLANK COMMA DO DOT ELSE EQL FLOAT FUNC ID IF INT LBRK LESSTHAN LKEY LPAR MAIN MINUS MORETHAN MULT NUMFLOAT NUMINT PLUS PRINT RBRK RKEY RPAR SEMICOLON SLASH VAR WHILEtipo : INTtipo : FLOATempty :'
    
_lr_action_items = {'INT':([0,],[2,]),'FLOAT':([0,],[3,]),'$end':([1,2,3,],[0,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tipo':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> tipo","S'",1,None,None,None),
  ('tipo -> INT','tipo',1,'p_tipo1','anaSintaxis.py',41),
  ('tipo -> FLOAT','tipo',1,'p_tipo2','anaSintaxis.py',46),
  ('empty -> <empty>','empty',0,'p_empty','anaSintaxis.py',51),
]