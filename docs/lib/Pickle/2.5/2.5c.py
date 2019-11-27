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
# Code Version 2.7.3
# Description:pickle.load(file, *, fix_imports = True, encoding = “ASCII”, errors = “strict”)
# This function is equivalent to Unpickler(file).load(). This function is used to read a pickled
# object representation from the open file object file and return the reconstituted object hierarchy specified.


import pickle
from StringIO import StringIO


class SimpleObject(object):

    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return


data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

# Simulate a file with StringIO
out_s = StringIO()

# Write to the stream
for o in data:
    print
    'WRITING: %s (%s)' % (o.name, o.name_backwards)
    pickle.dump(o, out_s)
    out_s.flush()

# Set up a read-able stream
in_s = StringIO(out_s.getvalue())

# Read the data
while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print
        'READ: %s (%s)' % (o.name, o.name_backwards)
