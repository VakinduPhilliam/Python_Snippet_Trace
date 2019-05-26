# Python Traceback Stack
# traceback — Print or retrieve a stack traceback.
# This module provides a standard interface to extract, format and print stack traces of Python programs.
# It exactly mimics the behavior of the Python interpreter when it prints a stack trace.
# This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.
# The module uses traceback objects — this is the object type that is stored in the sys.last_traceback variable and returned as the third item from
# sys.exc_info().
#
# The following example demonstrates the different ways to print and format the exception and traceback:
# 

import sys, traceback

def lumberjack():
    bright_side_of_death()

def bright_side_of_death():
    return tuple()[0]

try:
    lumberjack()

except IndexError:
    exc_type, exc_value, exc_traceback = sys.exc_info()

    print("*** print_tb:")
    traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

    print("*** print_exception:")

    # exc_type below is ignored on 3.5 and later
    traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print("*** print_exc:")

    traceback.print_exc(limit=2, file=sys.stdout)

    print("*** format_exc, first and last line:")

    formatted_lines = traceback.format_exc().splitlines()

    print(formatted_lines[0])
    print(formatted_lines[-1])
    print("*** format_exception:")

    # exc_type below is ignored on 3.5 and later

    print(repr(traceback.format_exception(exc_type, exc_value,
                                          exc_traceback)))
    print("*** extract_tb:")
    print(repr(traceback.extract_tb(exc_traceback)))

    print("*** format_tb:")
    print(repr(traceback.format_tb(exc_traceback)))

    print("*** tb_lineno:", exc_traceback.tb_lineno)
