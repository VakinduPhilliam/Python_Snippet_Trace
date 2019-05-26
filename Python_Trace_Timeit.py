# Python Trace
# timeit — Measure execution time of small code snippets
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.
#
# Examples:
#

import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

#
# OUTPUT:
#
# 0.3018611848820001
#

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

#
# OUTPUT:
#
# 0.2727368790656328
#

timeit.timeit('"-".join(map(str, range(100)))', number=10000)

#
# OUTPUT:
#
# 0.23702679807320237
#