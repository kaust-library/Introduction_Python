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

A quick reminder of Python. First numbers, than strings

```Python
>>> c = 300_000_000_00 # speed of light in vacum in SI units (m/s).
>>> ff = 5.678 # float number
>>> zz = 3 + 4j # complex number
>>> hello = "hello world!"
>>> hello.upper() # Basic string functions
'HELLO WORLD!'
>>> hello[2:4] # String slicing.
'll'
>>>
>>> if vv > 10:
...     print('more than 10')
... else:
...     print('not more than 10')
...
not more than 10
>>>
>>> for ii in range(5):
...     print(f"{ii}", end=",")
...
0,1,2,3,4,>>>
>>>
>>> numbers = range(1, 16) # Create a list from 1 to 15
>>> list(numbers)    
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
>>> 
>>> [ nn*nn for nn in numbers] # List comprehension
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
```
One important feature of the language is that Python is typeless, that is, the variables don't have a _type_:  _int_, or _float_:

```Python
>>> x = 'hello'
>>>
>>> x = 42
```

The variable `x` can be an _int_ or a _text_. 


### Python on Ubuntu Systems

On Ubuntu system it's necessary to install `python3-venv` package. And if you are not going to install old Python2, than, it's a good idea to install the package `python-is-python3,` just so that the `python` command invokes `python3` instead of an error message.

Using `venv.`

## Config Parser

A very convinient way to create a configuration file for your application is with the `ConfigParser` module. It can create a file that is similar to  Windows _ini_ file. The configuration file looks like

```
[ACCESSION]
accession_id = 000_000_0000

[BAGGER]
# You can specify a comma separated list of directories as source: dir1, dir2, ...
source_dir = C:\Users\joe\Work\boat_trip_pictures, C:\Users\joe\Work\my_event_1
# Using Python ExtendedInterpolation to use the 'accession_id' as target directory
dest_dir = C:\Users\joe\Work\${ACCESSION:accession_id}

[CLAMAV]
av_dir = C:\Program Files\ClamAV
av_update = freshclam.exe
av_clamav = clamscan.exe
av_logs_root = C:\Users\Desktop\john\clamscanlogs\clamAVlog
quarantine_days = 30
# Doesn't actually run the AV command, just print it.
run_it = no
(...)
```

You can create sections, use comments to make easier to users to understand your configuration, use different types of data, like numbers or logical values, and, even, interpolate values from one section to another.

To read the configuration file, you use the `ConfigParser` module

```Python
import configparser
(...)
   # Creating a configparser object
    config = configparser.ConfigParser(
        interpolation=configparser.ExtendedInterpolation()
    )
    config.read(config_file)
(...)

    # Reading values
    acc_number = config['ACCESSION']['accession_id']

    # Using a convenience function to read a boolean value
    if config['CLAMAV'].getboolean('run_it'):
        (...)
```

The extended interpolation presents a more natural interpolation, more natural in the sense that is similar to environment variables in Linux. The biggest advantage of the extended interpolation is to enable to fetch values from other sections. In the configuration file defined above, we used the `accession_id` defined in the `ACCESSION` section, to define a directory in the `BAGGER` section

```Python
[ACCESSION]
accession_id = 000_000_0000

[BAGGER]
(...)
dest_dir = C:\Users\joe\Work\${ACCESSION:accession_id}
```

## Dot Env

## Executing Commands

## Logging

## Clock

## Jinja2

## Type Hinting

