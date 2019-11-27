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
# Code Version 2.7.5
# Description: Handling Stateful Objects: This example shows how to modify pickling behavior for a class.
# The TextReader class opens a text file, and returns the line number and line contents each time its readline() method is called.

class TextReader:
	"""Print and number lines in a text file."""

	def __init__(self, filename):
		self.filename = filename
		self.file = open(filename)
		self.lineno = 0

	def readline(self):
		self.lineno + = 1
		line = self.file.readline()
		if not line:
			return None
		if line.endswith('\n'):
			line = line[:-1]
		return "%i: %s" % (self.lineno, line)

	def __getstate__(self):
		# Copy the object's state from self.__dict__ which contains
		# all our instance attributes. Always use the dict.copy()
		# method to avoid modifying the original state.
		state = self.__dict__.copy()
		# Remove the unpicklable entries.
		del state['file']
		return state

	def __setstate__(self, state):
		# Restore instance attributes (i.e., filename and lineno).
		self.__dict__.update(state)
		# Restore the previously opened file's state. To do so, we need to
		# reopen it and read from it until the line count is restored.
		file = open(self.filename)
		for _ in range(self.lineno):
			file.readline()
		# Finally, save the file.
		self.file = file

reader = TextReader("hello.txt")
print(reader.readline())
print(reader.readline())
new_reader = pickle.loads(pickle.dumps(reader))
print(new_reader.readline())
