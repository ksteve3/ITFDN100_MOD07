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
# Code Version 2.7.2
# Description:pickle.dumps(obj, protocol = None, *, fix_imports = True)
# This function returns the pickled representation of the object as a bytes object.

# Python program to illustrate
#Picle.dumps()
import pickle

data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
data_string = pickle.dumps(data)
print 'PICKLE:', data_string
