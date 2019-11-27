# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research topic: Pickle Module
# Code Version: Example code 2.4
# Pickling without a file
# Understanding Python Pickling with example, https://www.geeksforgeeks.org/understanding-python-pickling-example/

# initializing data to be stored in db

Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak',
'age' : 21, 'pay' : 40000}
Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}

# database
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

# For storing
b = pickle.dumps(db)	 # type(b) gives <class 'bytes'>

# For loading
myEntry = pickle.loads(b)
print(myEntry)

