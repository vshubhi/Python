"""
Sorting a dictionary: 

Dictionaries cannot be sorted directly, 
but you can create a sorted list of keys or 
key-value pairs using the sorted() function:
"""
my_dict = {"a":26, "b": 25, "z":1, "y":2, "x":3} 
sorted_keys = sorted(my_dict.keys())
sorted_items = sorted(my_dict.items(), key=lambda x: x[1])
