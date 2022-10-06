# Introduction to Python

Python was created by [Guido Van Rossum](https://gvanrossum.github.io/) in late 1980s for the experimental [Amoeba operating system](https://en.wikipedia.org/wiki/Amoeba_(operating_system)). The version 1.0 of Python was released in 1994. Version 2.0 was release in October 2000, and version 3 was released in December 2008 to fix many design problems with the language. One of the major issues was that version 3 was mostly incompatible with version 2, and, therefore, it broke many scripts in Python 2. The name comes from the BBC TV show [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus).

## Installing Python

If you are using any fairly recent version of Linux or macOS, there are great chances that you already have Python installed on your computer. Just open the terminal and type `python` or `python3,` and you should see the Python prompt

```
mgarcia@jammy:~$ python3
Python 3.10.6 (main, Aug 10 2022, 11:40:04) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

On Microsoft Windows, there is an installer provided by [Python itself](https://www.python.org/downloads/), but, probably, the easiest way is to install via the Microsoft Store.

## The Zen of Python

A quick guide for _pythonic_ scripts

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
```

## Python Basic Elements

Python has all the basic types that you would expect: numeric types, like [int, float, and complex](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex). The text type is [`str`](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). There is very powerful and useful mapping type, [`dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict). Plus sequence types like [lists, tuples, ranges](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range). And much more. 

Bolleans are implemented as a subtype of integers. Integers have [unlimited precision](https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic). Floating point numbers are implemented using _double_ in C. For those curious, information about precision and internal representation on your system, you check with `sys.float_info`:

```Python
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>>
```
### Numbers in Python

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Simple examples of simple operations

```Python
>>> 2 + 2
4
>>> 2 + 2 * 2
6
>>> (2 + 2) * 2
8
>>> 3**2 + 4**2 # The famous "3", "4" and "5" triangle
25
>>> 2**8 # 2 raised to 8th power
256
>>> 17 / 3 # Divisions always return a float number
5.666666666666667
>>> 17 % 3 # remainder of the division
2
>>> 17 // 3 # floor of the division (integer part)
5
>>> divmod(17,3) # Or how to get floor and remainder with a single function.
(5, 2)
>>>
>>> x = 3.5
>>> int(x) # Convert a number from float to int
3
>>> y = 5
>>> float(y) # Convert a int to float
5.0
>>>
```

You can also define variables in Python

```Python
>>> tax = 12.5/100 # 12.5%
>>> price = 125.50
>>> price * tax
15.6875
>>> price + _
141.1875
>>>
>>> round(_, 2)
141.19
>>>
```
The last printed value is assigned to variable `_`, which can be convinient when usin Python as a desk calculator.

> Some people use the `_` as a way of saying that a function returns a value, but we don't care
> ```Python
> _ = my_func(my_parameter)
> ```
> But this is just a convention.

The real and imaginary part of a complex number are of type _float_

```Python
>>> real = 5
>>> imag = 3
>>> z = complex(real, imag)
>>> z.real
5.0
>>> z.imag
3.0
>>> z
(5+3j)
>>> z.conjugate()
(5-3j)
>>>
```

Adding a `'j'` or `'J'` to a number, converts it to complex type

```Python
>>> c = 3j
>>> c
3j
>>> c.real
0.0
>>> c.imag
3.0
>>>
```
### Strings

Textual data in Python is handled with `str` objects, or _strings_. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways:

* Single quotes: `'allows embedded "double" quotes'`
* Double quotes: `"allows embedded 'single' quotes"`
* Triple quoted: `'''Three single quotes''', """Three double quotes"""`

The double quotes offers the advantage when writing a message that already include a single quote:

```Python
>>> "he doesn't like garlic"
"he doesn't like garlic"
>>>
```

Triple quotes allow space in the string

```Python
>>> """he
... doesn't
... like
... garlic"""
"he \ndoesn't \nlike\ngarlic"
>>>
```

Note that the line breaks are encoded as `\n`.

> The backslash character can create problems when dealing with Windows path, like a user named Nancy
> ```
> C:\Users\nancy\Downloads
> ```
> In this case, declare the string as _raw_ to prevent the `\n` of her name to be interpreted as line break:
>```
> r'C:\Users\nancy\Downloads'
>```

### Lists

### Dictionaries

## Control Flow

* range
* if ... elif ... else
* for
* while

## Functions

Declaring functions with `def` and using _docstring_.

## Input and Output

Reading and writing files.

## Errors and Exceptions

Capturing exceptions

## Modules

Importing modules

## Brief Tour to Standard Library

Basic interactions with the OS.

Paths in Windows.

## Development Environments

### Virtual Environment

> On Ubuntu system it's necessary to install `python3-venv` package.

Using `venv.`

### JupyterLab

Installing JupyterLab

Starting Jupyterlab

### VS Code

Installing VScode and extra packages

Selecting the interpreter

## What's Next

* Data Science

* Web Development

* AI

