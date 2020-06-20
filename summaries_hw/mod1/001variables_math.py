# Comments (ignored by python)
"""
This is a multiline comment, Python ignores this too.

Variables, Command Line, Math
By Calvin Wong

Summary of topics we discussed (probably good idea to know what each is):
"""


"""
If you're in Python, you need to run quit() to be able to use Terminal commands.
The way you know you're in Python is if you see the >>> at the bottom.

Terminal commands

ls:                     on Mac or bash, this lists all the files in the current directory
dir:                    for Command Prompt (windows), lists all files in the directory
cd <location>:          change directory to that location
python (or python3):    starts python
python <file.py>:       runs python on the file
"""



"""Terminal vs text editor: The terminal runs python INTERACTIVELY, loading .py is
 NOT interactive because it knows you've already typed up the Python.

>>> ((2 + 3) * 2)
10

This literally gives the result back because it is meant to be interactive and
tells you what the result of that line is.
Imagine if you typed something and nothing was output, like so:

>>> 1 + 1

>>> "Hello?"

>>> "Is this working?"

as you can see, that would seem not very interactive if you type line after line and
get nothing back during interactive mode. However, assignment statements are an exception,
so for example:

>>> x = 3

>>> x
3

In contrast, when you load a .py file using "python file.py" it's not interactive, so it will run
through the code but not display anything unless you tell it to print a value.

This is why print even exists, because otherwise if we had a huge python file of 100s
of lines of code each printing out a line, the terminal could get messy.

This is why the creators made print(), to specify when we want to print something
while it's not interactive.

Thus,

(((3+5)*3)/3))

in the .py file doesn't get printed, for the same reason if you wrote

1 + 1

in the .py file it wouldn't be printed."""



"Strings" == 'Strings' # True
# For strings, single quotes or double quotes are the same in Python
"String" + " Concatenation"
"String Multiplication" * 3

x = "valued at " # Variables, assigning variables a value

"""How values are displayed in the terminal versus when you use a .py file"""
print() # can be used in both terminal and .py files to display whatever is inside print

""" Math """
34 # Integers
21.3 # Floats

""" Converting between strings, ints, and floats """
int(32.5)
float(32)
str(34)
# Play around with the above, what happens if you put in strings instead of numbers?

""" Math Operations """
+ - * ** / // % ()

""" In Place Operators """
x += "$34" # equivalent to x = x + "$34"

-= *= /= //= %= **=
