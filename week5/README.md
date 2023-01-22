# Libraries
libraries are bits of code written by you or others which you can use in your program.
you can use libararies to share functions or features with others as “modules”.

## Random
random is a libery that comes with python and you can import it by:

```python
import random
```

### random.choice
you can use `random.choice` to genrate a random item based on whats inside the input.

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```
output: 50%`heads` 50%`tails`

### random.randint
`random.randint` will generate a random number between a and b.

```python
import random

number = random.randint(1, 10)
print(number)
```
output: will generate `a number between 1-10`

## Statistics
Statistics is a libery filled with math functions for example `statistics.mean` and all other functions.

### statistics.mean
this is a function that takes 2 number and output the mean of the two number.
```python
import statistics

print(statistics.mean([100, 90]))
```
output: `95`

## Command-Line-arguments
Command-Line-arguments allows you take in arguments from the command line.

example:
input:`python3 hello.py jinghong`
```python
import sys

print("hello, my name is", sys.argv[1])
```
output:`hello, my name is jinghong`

you can also inprove this code by addint a gardian for it.

```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```
This will tell the user if the user have entered too few arguments.

## Slice
Slice is a command that allows us to take a list and tell the compiler where we want the compiler to consider the start of the list and the end of the list.
Example:
```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```
the slice over here helps alot with sepreting the two part of the code and finding the user name.

## Packages
One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. These are third-party libraries, implemented as a folder, “packages”.

for example cow say is a package you can install with pip instaler.

example: 
```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
```

## API
APIs or “application program interfaces” allow you to connect to the code of others.

```python
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
```
this is a simple code that request to the websited `itunes.apples.come` and saves that response as the variable response.

## Making Your Own Libraries
you can simply make your own libary by useing the def function and save the file next to the file you want to import that libary for example if you made a file called `hallo.py` and have the function `say_hello` in it, and you have a nother file called `names.py` this is how you import it.

```python
from hello import say_hello
print(hello.say_hello("jinghong"))
```
this will import and work based on your code in hallo.py