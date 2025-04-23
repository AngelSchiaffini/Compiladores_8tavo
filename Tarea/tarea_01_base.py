# Author: A01748203 José Ángel Schiaffini Rodríguez

from delta import Compiler, Phase


source = '#b101'

c = Compiler('program')
c.realize(source, Phase.SEMANTIC_ANALYSIS)
print(c.parse_tree_str)
#print(c.result)