# Introduction to Python

Python was created by [Guido Van Rossum](https://gvanrossum.github.io/) in late 1980s for the experimental [Amoeba operating system](<https://en.wikipedia.org/wiki/Amoeba_(operating_system)>). The version 1.0 of Python was released in 1994. Version 2.0 was release in October 2000, and version 3 was released in December 2008 to fix many design problems with the language. One of the major issues was that version 3 was mostly incompatible with version 2, and, therefore, it broke many scripts in Python 2. The name comes from the BBC TV show [Monty Python's Flying Circus](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus).

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

One important feature of the language is that Python is typeless, that is, the variables don't have a _type_: _int_, or _float_:

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

A very convinient way to create a configuration file for your application is with the `ConfigParser` module. It can create a file that is similar to Windows _ini_ file. The configuration file looks like

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

It's very common to pass passwords for applications like a database via environment variables. For example when using a CI/CD pipeline in Gitlab or GitHub, one set a series of environment variables to the pipeline. But during development, it's necessary to have a similar way to pass passwords (or any other key-value pair) to the application, and that is the reason to use _dotenv_. Dotenv reads a `.env` file, and export the content to shell environment.

Let's create a sample `.env` file, read it, and use the key-value pair on our application. Create a `.env` file on the root of your project

```
me@myserver:~/Work/repo2preservica$ cat .env
## Preservica Username
PRESERVICA_USERNAME="joe.doe@example.com"

## Preservica Password
PRESERVICA_PASSWORD="abc123def456"

me@myserver:~/Work/repo2preservica$
```

If the `.env` file contains only the variables necessary, then it's enough just to call the method

```Python
from dotenv import load_dotenv
(...)
    # load environment variables for 'python-dotenv
    load_dotenv()
```

But if the you want to read just one of the variables, then you can use the method `environ` from the the `os` module

```Python
import os
(...)
    load_dotenv()

    api_passwd = os.environ['ARCHIVERA_API_PW']
```

The method will raise a `KeyError` exception if for any reaseon the variable is not set.

## Executing Commands

To execute a program from your script, maybe it's easier if you assemble the command to be execute, with all its parameters first, then execute the command, and, finally, check the output

```Python
import subprocess
(...)
    # 1. Prepare the parameters for the command
    droid_exec_path = os.path.join(droid_config['droid_dir'], droid_config['droid_bin'])
    droid_bag_path = os.path.join(bag_path, "data")

    # 2. Assemble the command line to be executed
    droid_cmd = f"{droid_exec_path} -a {droid_bag_path} --recurse -p {acc_number}.droid"
    (...)

        # 3. Execute the program.
        result = subprocess.run(droid_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        result.check_returncode()
    (...)
```

We create `droid_exec_path` by joining the directory with the executable name, here we are using the function `join` that handles the path separator that is OS dependent, that is, Windows (`\`) and Linux (`/`) have different path separators

```Python
#
# Linux
>>> import os
>>> droid_dir = "/opt/LibraryApps/droid-binary-6.5-bin-with-jre"
>>> droid_bin = "droid.sh"
>>> droid_exec_path = os.path.join(droid_dir, droid_bin)
>>> print(f"droid_exec_path = '{droid_exec_path}'")
droid_exec_path = '/opt/LibraryApps/droid-binary-6.5-bin-with-jre/droid.sh'
#
# Windows
>>> import os
>>> droid_dir = "C:\LibraryApps\droid-binary-6.5-bin-win32-with-jre"
>>> droid_bin = "droid.bat"
>>> droid_exec_path = os.path.join(droid_dir, droid_bin)
>>> print(f"droid_exec_path = '{droid_exec_path}'")
droid_exec_path = 'C:\LibraryApps\droid-binary-6.5-bin-win32-with-jre\droid.bat'
>>>
```

Before executing the command we assemble the full command line, include the parameters, (`-a`, `--recurse`, etc.). Next we [execute the command](https://docs.python.org/3.10/library/subprocess.html#using-the-subprocess-module)

```Python
result = subprocess.run(droid_cmd, stdout=subprocess.PIPE,
         stderr=subprocess.STDOUT, text=True)
```

Where:

- `stdout=subprocess.PIPE`: we are capturing the output of the command,
- `stderr=subprocess.STDOUT`: we are redirecting error messages to the standard output device,
- `text=True`: makes `stdout` available as a string, instead of a [byte sequence](https://docs.python.org/3.10/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview).

To talk about the return of the `subprocess.run`, the `result` above, let's see a simple example

```Python
# A very simple script:
# PS C:\Users\garcm0b\Work> cat .\hello_python.py
# print('hello from a python script')

# First we build the command line, and here, how to set the full path to the
# script: home_dir (~) + Work + hello_python.py
>>> import os
>>> import subprocess
>>> ppp = os.path.join(os.path.expanduser('~'), 'Work', 'hello_python.py')
>>> ppp
'C:\\Users\\garcm0b\\Work\\hello_python.py'
>>>
>>> my_cmd = "python.exe " + ppp
>>> subprocess.run(my_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
CompletedProcess(args='python.exe C:\\Users\\garcm0b\\Work\\hello_python.py', returncode=0, stdout='hello from a python script\n')
>>>
# Running the command again, and capturing the result.
>>> result = subprocess.run(my_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
>>> print(result.returncode)
0
>>>
>>> print(result.stdout)
hello from a python script

>>>
```

The important part is the `returncode` above: if it's "0," then the command was successful. Any other number means an error occurred. [Windows](https://learn.microsoft.com/en-us/windows/win32/debug/system-error-codes--0-499-) and [Linux](http://www.virtsync.com/c-error-codes-include-errno) have different meaning for the error number.

## Logging

## Date

Python has objects for [_date_, _time_ and _datetime_](https://docs.python.org/3.10/library/datetime.html#):

```Python
>>> moon_landing = DT.date(1969, 7, 20)
>>> moon_landing.isoformat()
'1969-07-20'
>>>
>>> moon_landing.strftime("%a, %d %B %Y")
'Sun, 20 July 1969'
>>>
>>> DT.date.today()
datetime.date(2023, 1, 1)
>>>
```

To create a _time_ object

```Python
>>> DT.time(14, 30)
datetime.time(14, 30)
>>> DT.time(14, 30).isoformat()
'14:30:00'
>>>
```

And finally, a _datetime_ object with different formating

```Python
>>> import datetime as DT
>>> DT.datetime.now()
datetime.datetime(2023, 1, 1, 15, 4, 5, 96075)
>>> DT.datetime.now().isoformat()
'2023-01-01T15:04:15.094031'
>>> DT.datetime.now().strftime("%a, %d %B %Y")
'Sun, 01 January 2023'
>>> DT.datetime.now().strftime("%a, %d %B %Y, %H:%M:%S")
'Sun, 01 January 2023, 15:28:15'
>>>
```

Together with the methods `date`, `time`, `datetime`, we also using other methods like `today`, `now`, and, [`strftime`](https://docs.python.org/3.10/library/datetime.html#strftime-and-strptime-behavior) to format the presentation of the objects. Also note that [ISO format](https://www.iso.org/iso-8601-date-and-time-format.html) is a standard way to present date and time information.

> Date and time objects can be [_aware_ or _naive_](https://docs.python.org/3.10/library/datetime.html#aware-and-naive-objects) regarding timezone information. An _aware_ object can have information of timezone and _day light saving_, and, as such, it's not open to interpretations.

OnNe intesting use of date manipulation is creation of custome file names, for example, with the date that you run a anti-virus check:

```Python
>>> import datetime as DT
>>> av_run_date = DT.datetime.today().strftime("%Y%m%d")
>>> print(av_run_date)
20230101
>>>
>>> av_log_file = f"av_scan_{av_run_date}.txt"
>>> print(av_log_file)
av_scan_20230101.txt
>>>
```

Another very common use o dates is to calculate the difference between two dates. For example if a product is expired or not. Consider the following example:

```Python
>>> import datetime as DT
>>> made_dt = DT.date.fromisoformat('2022-12-22')
>>> today = DT.date.today()
>>> good_day = (expire_dt - today).days
>>>
>>> if good_day > 0:
...     print(f"Still valid for '{good_day}' {good_day == 1 and 'day' or 'days'}")
...
Still valid for '22' days
>>>
```

We can even use _weeks_ for some calculations

```Python
>>> nn_weeks = 3
>>> in_future = today + DT.timedelta(weeks=nn_weeks)
>>> in_future.strftime("%a, %d %B %Y, %H:%M:%S")
'Tue, 24 January 2023, 00:00:00'
>>>
```

> If your application does a lot of dates and timezone manipulations, or durations calculations, maybe you should consider the library _pendulum_: [https://pendulum.eustace.io/](https://pendulum.eustace.io/), which seems to be much more friendlier that the Python native classes.

## Jinja2

Python has a very good templating system called [_Jinja_](https://palletsprojects.com/p/jinja/).

To install use the usual `pip` command inside a virtual environment

```
(venv) PS C:\Users\garcm0b\Work\Introduction_Python> pip install -U jinja2
```

As first example, consider the following example

```Python
>>> import jinja2 as J2
>>> environment = J2.Environment()
>>> template = environment.from_string("Hi {{ name }}, how are you?")
>>> template.render(name="Joe")
'Hi Joe, how are you?'
>>>
```

A simple example of Jinja would be convert a table in a text file into a configuration file. Sometimes you receive a list with hostnames and IP addresses, and need to create a series of configuration files. Consider the example in the `templates` folder. There are three folder: `in`, `out` and `temps.` On the folder `in`, there is an input file with three machines:

```
(venv) PS C:\Users\garcm0b\Work\Introduction_Python\examples\templates\in> cat .\hosts.txt
atta, 192.168.56.10
flik, 192.168.56.11
hopper, 192.168.56.12
```

And we want to generate three configuration files for [Icinga](https://icinga.com/) monitoring system in the output directory `out.` The "recipe" is the _template_ in the `temps` folder:

```
(venv) PS C:\Users\garcm0b\Work\Introduction_Python\examples\templates\temps> cat .\hostconfig.j2
/**
* Simple Icinga host configuration file
*/

object Host "{{ hostname }}" {
    check_command = "hostalive"
    address = "{{ ip_addr }}"
}
(venv) PS C:\Users\garcm0b\Work\Introduction_Python\examples\templates\temps>
```

Finally a Python script to tie everything

```Python
(venv) PS C:\Users\garcm0b\Work\Introduction_Python\examples\templates> cat .\hostsconfig.py
(...)
#
# Import the module
import jinja2 as J2


def main():
    #
    # The 'Environment' object stores all configuration
    environment = J2.Environment(loader=J2.FileSystemLoader("temps/"))
    template = environment.get_template("hostconfig.j2")

(...)
        content = template.render(hostname=hostname, ip_addr=ip_addr)

if __name__ == "__main__":

    main()
(venv) PS C:\Users\garcm0b\Work\Introduction_Python\examples\templates>
```
