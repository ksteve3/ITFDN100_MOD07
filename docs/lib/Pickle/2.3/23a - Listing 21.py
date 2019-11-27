# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research topic: Pickle Module
# Code Version: Example code 2.3a Listing 21
# Description: This tutorial is going to cover the pickle module, which is a
# part of your standard library with your installation of Python.
# Reference: Python Pickle Module for saving Objects by serialization,
# https://pythonprogramming.net/python-pickle-module-save-objects-serialization/
# Related tutorials: Saving Classifiers with NLTK,
# https://pythonprogramming.net/pickle-classifier-save-nltk-tutorial/
#
#
# import pickle
#
# example_dict = {1:"6",2:"2",3:"f"}
#
# pickle_out = open("dict.pickle","wb")
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()
#
# pickle_in = open("dict.pickle","rb")
# example_dict = pickle.load(pickle_in)
#
# print(example_dict)
# print(example_dict[3])
#
# #Through saving the serialized object, it's nature is included, so we
# # don't have to worry about loading things "as" strings, dictionaries, lists, etc.
