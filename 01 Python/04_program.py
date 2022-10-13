import mymodule
mymodule.func_in_module()
# needs to be local
# --> this is inside the 04_mymodule.py file

# __pycache__ folder created --> when you run a program in python 
# the interpreter compiles it to byte code first --> 
# stores that in the __pycache__ folder

import mymodule as mm
mm.func_in_module()

from mymodule import func_in_module
func_in_module()
# just imports that specific function