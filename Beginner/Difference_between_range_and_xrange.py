"""
Difference between range and xrange (Python 2 only): 
In Python 2, range and xrange are both used to generate
a sequence of numbers, but they behave differently in terms 
of memory usage. range creates a list of all the numbers in 
the specified range, while xrange generates the numbers on-the-fly, 
using less memory. However, in Python 3, xrange has been removed, 
and range behaves like Python 2's xrange.
"""