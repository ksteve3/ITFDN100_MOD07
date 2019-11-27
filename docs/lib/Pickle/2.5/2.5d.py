# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Reference: “Pickle — Python Object Serialization - GeeksforGeeks”
# (GeeksforGeeks, June 8, 2017) <https://www.geeksforgeeks.org/pickle-python-object-serialization/>
# accessed November 24, 2019.
# Research topic: Pickeling Module
# Code Version 2.7.4
# Description: pickle.loads(bytes_object, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
# This function is used to read a pickled object representation from a bytes object and return
# the reconstituted object hierarchy specified.

# Python program to illustrate
# pickle.loads()

import pickle
import pprint

data1 = [ { 'a':'A', 'b':2, 'c':3.0 } ]
print 'BEFORE:',
pprint.pprint(data1)

data1_string = pickle.dumps(data1)

data2 = pickle.loads(data1_string)
print 'AFTER:',
pprint.pprint(data2)

print 'SAME?:', (data1 is data2)
print 'EQUAL?:', (data1 == data2)
