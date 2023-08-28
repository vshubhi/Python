"""
List comprehension: A list comprehension is a concise way to create lists in Python. 
It consists of an expression followed by at least one for clause and can include 
optional if clauses. It applies the expression to each item in the input sequence 
(or sequences) and filters the results based on the conditions specified. 
For example:
"""

squares = [x**2 for x in range(10) if x % 2 == 0]
