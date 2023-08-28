"""
Sorting a dictionary: 

Dictionaries cannot be sorted directly, 
but you can create a sorted list of keys or 
key-value pairs using the sorted() function:
"""

sorted_keys = sorted(my_dict.keys())
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
