# Python Basics

A reminder of Python basics

## Comparisons

There are eight comparisons operations in Python. Comparisons can be chained in a natural way like _10 < x < 20_, instead of _x > 10 and 20 >= x_

| Operator | Meaning |
| ---------|---------|
| `<` | Strictly less than |
| `<=` | less than or equal |
| `>` | Strictly greater than |
| `>=` | greater than or equal |
| `==` | equal |
| `!=` | not equal |
| `is` | object identity |
| `is not` | negate object identity |


## Numbers in Python

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
#### Numerical Comparison

Using the table above for numeric comparison we can create an example to check if a variable is inside a range

```Python
>>> temp = 23
>>> if temp > 30:
...     print("It's too hot outside.")
... elif 30 >= temp > 20:
...     print("Nice temperature. Time to enjoy the weather!")
... else:
...     print("Better stay inside the house")
... 
Nice temperature. Time to enjoy the weather!
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

#### String Slicing

An important concept is the string slicing, that is, taking only a certain part of string. For example

```Python
>>> word = "Python"
>>> # The first character of a string
>>> word[0]
'P'
>>> # Taking part of a string
>>> word[2:5]
'tho'
>>> 
```
#### Some String Methods

Here we present some methods for basic string manipulation


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
