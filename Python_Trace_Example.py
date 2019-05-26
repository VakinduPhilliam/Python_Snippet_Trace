# Python trace — Trace or track Python statement execution.
# The trace module allows you to trace program execution, generate annotated statement coverage listings, print caller/callee relationships
# and list functions executed during a program run. It can be used in another program or from the command line.
#
# A simple example demonstrating the use of the programmatic interface:
# 

import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.

tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

# run the new command using the given tracer

tracer.run('main()')

# make a report, placing output in the current directory

r = tracer.results()

r.write_results(show_missing=True, coverdir=".")
