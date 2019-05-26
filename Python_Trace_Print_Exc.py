# Python Trace
# timeit — Measure execution time of small code snippets
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.
#
# print_exc(file=None). 
# Helper to print a traceback from the timed code.
# 
# Typical use:
# 

t = Timer(...)       # outside the try/except

try:
    t.timeit(...)    # or t.repeat(...)

except Exception:
    t.print_exc()
