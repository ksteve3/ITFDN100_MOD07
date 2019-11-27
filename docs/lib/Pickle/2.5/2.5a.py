# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Reference: “Pickle — Python Object Serialization - GeeksforGeeks”
# (GeeksforGeeks, June 8, 2017) <https://www.geeksforgeeks.org/pickle-python-object-serialization/> accessed November 24, 2019.
# Research topic: Pickeling Module
# Code Version 2.7.1
# Description:pickle.dump(obj, file, protocol = None, *, fix_imports = True)
# This function is equivalent to Pickler(file, protocol).dump(obj). This is used to write a
# pickled representation of obj to the open file object file.
# The optional protocol argument is an integer that tells the pickler to use the given protocol.
# The supported protocols are 0 to HIGHEST_PROTOCOL. If not specified, the default is DEFAULT_PROTOCOL.
# If a negative number is specified, HIGHEST_PROTOCOL is selected.
#
# If fix_imports is true and protocol is less than 3, pickle will try to map the new Python
# 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.

# Python program to illustrate
# pickle.dump()
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
	print 'WRITING: %s (%s)' % (o.name, o.name_backwards)
	pickle.dump(o, out_s)
	out_s.flush()
