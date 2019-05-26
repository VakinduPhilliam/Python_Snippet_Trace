# Python Trace
# timeit — Measure execution time of small code snippets
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.
# The following examples show how to time expressions that contain multiple lines.
# Here we compare the cost of using hasattr() vs. try/except to test for missing and present object attributes:

import timeit

# attribute is missing

s = """\
    try:
        str.__bool__
    except AttributeError:
        pass
    """

 timeit.timeit(stmt=s, number=100000)

#
# OUTPUT:
#
# 0.9138244460009446
#

s = "if hasattr(str, '__bool__'): pass"

timeit.timeit(stmt=s, number=100000)

#
# OUTPUT:
#
# 0.5829014980008651
#

# attribute is present

 s = """\

    try:
        int.__bool__
    except AttributeError:
        pass
    """

timeit.timeit(stmt=s, number=100000)

#
# OUTPUT:
#
# 0.04215312199994514
#

s = "if hasattr(int, '__bool__'): pass"

timeit.timeit(stmt=s, number=100000)

#
# OUTPUT:
#
# 0.08588060699912603
#
