 # Title

 
 Dev: KStevens
 
 Date: 11.20.2019
 
 GitHub Markdown // Index.md Template 
 
  Reference: https://www.youtube.com/watch?v=4IkIdXJBC6o&feature=youtu.be, 1:23:24
  

## Structured Error Handling (Try-Except)
When you are programming, you fix your bugs immediately and make sure the code
runs smoothly. However, it often happens that other people introduce new bugs
when they use your program.

### Raising Custom Errors
Python automatically generates errors based on conditions defined by the
Python Runtime. However, you can also "raise" errors based on custom
conditions (Listing 13).

```
# ------------------------------------------------- #
# Title: Listing 13
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# KStevens,11.20.2019,Created Script
# ------------------------------------------------- #
try:
 new_file_name = input("Enter the name of the file you want to make: ")
 if new_file_name.isnumeric():
 raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
 print("There was a non-specific error!")
print("Built-In Python error info: ")
 print(e, e.__doc__, type(e), sep='\n')
```
#### Listing 13

![Github pages test image](https://ksteve3.github.io/ITFnd100-Mod07/Snips/test%20github%20image.PNG "Github pages test image")
#### Figure 13/ Github Test page. The Github Test page image.

![Remote images](https://i.ytimg.com/vi/l3oPTo4vCXI/maxresdefault.jpg "Remote images")
#### Remote images/ Github Test page. The Remote image.



```



