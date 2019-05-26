# Python Traceback Stack
# traceback — Print or retrieve a stack traceback.
# This module provides a standard interface to extract, format and print stack traces of Python programs.
# It exactly mimics the behavior of the Python interpreter when it prints a stack trace.
# This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.
# The module uses traceback objects — this is the object type that is stored in the sys.last_traceback variable and returned as the third item from
# sys.exc_info().
#
# The following example shows the different ways to print and format the stack:
# 

import traceback

def another_function():
        lumberstack()

def lumberstack():
        traceback.print_stack()

        print(repr(traceback.extract_stack()))
         print(repr(traceback.format_stack()))

another_function()
