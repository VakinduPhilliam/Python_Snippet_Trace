# Python Trace
# timeit — Measure execution time of small code snippets
# This module provides a simple way to time small bits of Python code. It has both a Command-Line Interface as well as a callable one.
# It avoids a number of common traps for measuring execution times.
# It is possible to provide a setup statement that is executed only once at the beginning:
# This can be done using the Timer class and its methods:
 
import timeit

t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
t.timeit()

#
# OUTPUT:
#
# 0.3955516149999312
#

t.repeat()

#
# OUTPUT:
#
# [0.40193588800002544, 0.3960157959998014, 0.39594301399984033]
#