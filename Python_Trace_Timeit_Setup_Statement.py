# Python Trace
# timeit — Measure execution time of small code snippets
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.
# It is possible to provide a setup statement that is executed only once at the beginning:

import timeit

timeit.timeit('char in text', setup='text = "sample string"; char = "g"')

#
# OUTPUT:
#
# 0.41440500499993504
#

timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"')

#
# OUTPUT:
#
# 1.7246671520006203
#