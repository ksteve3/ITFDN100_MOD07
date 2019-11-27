# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Research Exception Handling & Pickling in Python
# ChangeLog (Who,When,What):
# Kstevens,11-20-19,Modified code to complete assignment 7
# ------------------------------------------------------------------------ #
# Research source: Python Tutorial: Using Try/Except Blocks for Error Handling,
# https://www.youtube.com/watch?v=NIWwJbo-9_8
# Research source (other/related to above): code_snippets/Exceptions/,
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Exceptions
# Research topic: Exception Handling
# Code Version 7.1
# Example description: Fixes the code errors in example 7.1 to achieve the requested Output
# Requirements described in Example 7.1 in Assignment07.docx or on the my
# GitHub Webpage @ https://ksteve3.github.io/ITFDN100-Mod07/ under Example 7.1 Output Requirements


try:
    file = open('testfile.txt')

except Exception:
    print('Sorry this file does not exist')

# else:
#     print(file.read())
#     file.close()
#
# finally:
#     print('Closing File/Database...')  # Indicates completion of "something that needs to get done" by displaying
#     # final closeout message/ final closeout step(s) executed to user regardless if the code is successful or not.