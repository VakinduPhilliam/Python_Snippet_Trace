# Python Traceback Stack
# traceback — Print or retrieve a stack traceback.
# This module provides a standard interface to extract, format and print stack traces of Python programs.
# It exactly mimics the behavior of the Python interpreter when it prints a stack trace.
# This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.
# The module uses traceback objects — this is the object type that is stored in the sys.last_traceback variable and returned as the third item from
# sys.exc_info().
#
# This simple example implements a basic read-eval-print loop, similar to (but less useful than) the standard Python interactive interpreter loop.
# For a more complete implementation of the interpreter loop, refer to the code module.
# 

import sys, traceback

def run_user_code(envdir):
    source = input(">>> ")

    try:
        exec(source, envdir)

    except Exception:
        print("Exception in user code:")
        print("-"*60)

        traceback.print_exc(file=sys.stdout)
        print("-"*60)

envdir = {}

while True:
    run_user_code(envdir)
