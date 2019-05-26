# Python Traceback Stack
# traceback — Print or retrieve a stack traceback.
# This module provides a standard interface to extract, format and print stack traces of Python programs.
# It exactly mimics the behavior of the Python interpreter when it prints a stack trace.
# This is useful when you want to print stack traces under program control, such as in a “wrapper” around the interpreter.
# The module uses traceback objects — this is the object type that is stored in the sys.last_traceback variable and returned as the third item from
# sys.exc_info().
#
# This last example demonstrates the final few formatting functions:
# 

import traceback

traceback.format_list([('spam.py', 3, '<module>', 'spam.eggs()'),
                           ('eggs.py', 42, 'eggs', 'return "bacon"')])

#
# OUTPUT:
#
# ['  File "spam.py", line 3, in <module>\n    spam.eggs()\n',
# '  File "eggs.py", line 42, in eggs\n    return "bacon"\n']

an_error = IndexError('tuple index out of range')

traceback.format_exception_only(type(an_error), an_error)

# OUTPUT: '['IndexError: tuple index out of range\n']'
