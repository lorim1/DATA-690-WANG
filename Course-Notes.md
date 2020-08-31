#  Chapter 2 Notes
### Each part broken into sections
## Chapter 2.1
- Python is an interpreted language
- There are areas of code that will prompt a response before continuing to run
- .py is the extention for running python programs

## Chapter 2.2
- Can run the IPython shell with ipython command
- Return or Enter key can execute statements
- Python statements are meant to be "pretty-printed" aka more readable
- Jupyter notebook is an interactive document for code, text data visualizations and other output
- Jupyter uses kernels, which are implementations of the Jupyter computing protocol
- Object introspection - question mark (?) before or after a variable will displacy general information about the object
- Using ?? will also show the functions source code (if possible)

### Useful keyboard shortcuts
- Ctrl-P or up-arrow = Search backward in command history for commands starting with currently entered text
- Ctrl-N or down-arrow = Search forward in command history for commands starting with currently entered text
- Ctrl-R = Readline-style reverse history search (partial matching)
- Ctrl-Shift-V = Paste text from clipboard
- Ctrl-C = Interrupt currently executing code
- Ctrl-A = Move cursor to beginning of line
- Ctrl-E = Move cursor to end of line
- Ctrl-K = Delete text from cursor until end of line
- Ctrl-U = Discard all text on current line
- Ctrl-F = Move cursor forward one character
- Ctrl-B = Move cursor back one character
- Ctrl-L = Clear screen

### IPython Magic Commands
- %quickref = Display the IPython Quick Reference Card
- %debug = Enter the interactive debugger at the bottom of the last exception traceback
- %hist = Print command input (and optionally output) history
- %pdb = Automatically enter debugger after any exception
- %paste = Execute preformatted Python code from clipboard
- %cpaste = Open a special prompt for manually pasting Python code to be executed
- %reset = Delete all variables/names defined in interactive namespace
- %page OBJECT = Pretty-print the object and display it through a pager
- %run script.py = Run a Python script inside IPython
- %prun statement = Execute statement with cProfile and report the profiler output
- %time statement = Report the execution time of a single statement
- %timeit statement = Run a statement multiple times to compute an ensemble average execution time; useful for timing code with very short execution time
- %who, %who_ls, %whos = Display variables defined in interactive namespace, with varying levels of information/ verbosity
- %xdel variable = Delete a variable and attempt to clear any references to the object in the IPython internals

### Chapter 2.3
- Python is an object oriented programming
- #" is ignored by the interpreter, use for comments
- Python differs other languages because object references have no associated type with them

### Binary Operators
- a + b Add a and b
- a - b Subtract b from a
- a * b Multiply a by b
- a / b Divide a by b
- a // b Floor-divide a by b, dropping any fractional remainder
- a ** b Raise a to the b power
- a & b True if both a and b are True; for integers, take the bitwise AND
-	a | b True if either a or b is True; for integers, take the bitwise OR
-	a ^ b For booleans, True if a or b is True, but not both; for integers, take the bitwise EXCLUSIVE-OR
- a == b True if a equals b
- a != b True if a is not equal to b
- a <= b, a < b True if a is less than (less than or equal) to b
- a > b, a >= b True if a is greater than (greater than or equal) to b
- a is b True if a and b reference the same Python object
- a is not b True if a and b reference different Python objects

## Chapter 2.4

### Standard Python types
- None = The Python “null” value (only one instance of the None object exists)
- str = String type; holds Unicode (UTF-8 encoded) strings
- bytes = Raw ASCII bytes (or Unicode encoded as bytes)
- float = Double-precision (64-bit) floating-point number (note there is no separate double type)
- bool = A True or False value
- int = Arbitrary precision signed integer

## Chapter 2.5

### Datatime format specification
- %Y = Four-digit year
- %y = Two-digit year 
- %m = Two-digit month [01, 12] 
- %d = Two-digit day [01, 31] 
- %H = Hour (24-hour clock) [00, 23] 
- %I = Hour (12-hour clock) [01, 12] 
- %M = Two-digit minute [00, 59] 
- %S = Second [00, 61] (seconds 60, 61 account for leap seconds) 
- %w = Weekday as integer [0 (Sunday), 6] 
- %U = Week number of the year [00, 53]; Sunday is considered the first day of the week, and days before the first Sunday of the year are “week 0” 
- %W = Week number of the year [00, 53]; Monday is considered the first day of the week, and days before the first Monday of the year are “week 0” 
- %z = UTC time zone offset as +HHMM or -HHMM; empty if time zone naive 
- %F = Shortcut for %Y-%m-%d (e.g., 2012-4-18) 
- %D = Shortcut for %m/%d/%y (e.g., 04/18/12)
