# -*- coding: utf-8 -*-
"""
https://docs.python.org/3/library/dis.html
Disassembler for Python bytecode
"""

import dis

def myfunc():
    a = 1
    b = 2
    c = a + b
    print(c)
    
dis.dis(myfunc)    

"""
bytecode = dis.Bytecode(myfunc)
for instr in bytecode:
    print(instr.opname)
"""
    