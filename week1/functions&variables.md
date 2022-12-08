# functions and variables

## intro
every program ends with .py to empenment that that program is writen in python.

the first program write is hello, world whitch is a simple program that just prints hello, world on to the screen but its alos very famous because its the most simple stuff and it could not go wrong:

in the programing world we use CLI interfae more which is more powerful than the classic click and open interface.

```python
print("hello, world")
```
output: `hello, world`
## python hello.py

if you write a code in a file like 

```python
print("hello, world") 
```
output:`hello, world`

you would need to use some thing called interpreter to run it since your computer only understand 0s and 1s, how the interpreter works is that it transtats the code from top to bottm into 0s and 1s, but depend on what interperter you use it translats it deferently, so you would need to put the type of interperter you use in front to let the computer know what to use, thats why type "python hello.py" to run the hello.py file.

## functions
 a function is an action of a verb that lets you do someting in the program.
the print function prints what ever is inputed into it.

## arguments
a argument is an input to a function that influences its behavior.
### example:
```python
print("hello, world")
```
output: `hello, world`

here the inputed "hello, world" is an argument which changes whats printed to the screen.

some functions dont just take in one arguments but two three four five onward.
### example:
```python
name = jinghong
print("hello,", name)
```
output: `hello, jinghong`

this passes in two arguments into print and prints"hello, jinghong"

there is two ways of printing "hello jinghong" one is concatenation, and the other is passing in two argument. you can concatenate useing the "+" sign and passing two arguments useing the "," sign, they both work the same so any way is fine.

## side effects
a side effect can be visual, it can be audio, and in the case of
```python
print("hello, world") 
```
output:`hello, world`

its something that appears on the screen.

## bugs
bugs are just mistakes, its just someting you can solve.

for example if you forgot to put a closing printeces,
```python
print("hello, word
```
output: `SyntaxError: '(' was never closed`
which brings up a syntaxerror.

## return values
inputs are like if you ask question to some one and they give you answer that answer here is a return value and also an input from the user.

## variables
variables is where you store data for example if you user give you his/her name, you would need a variable called name to store that so you can use it later.

in python an equal sign is basicaly assining a value from the right to left for 
### example:
```python
name = "jinghong"
```
this assines the value "jinghong" into the variable name.

## comments 
are basicaly notes you write in the code to remind you/other people about whats the function of this code or what is needed for this code.

you use the "#" to write comments in python.

## pseudocode(sudocode)
this is how you describ the steps for your program to do just like a recepy for a cake, your code should folow the steps.

## print function
print(object(s), sep=separator, end=end, file=file, flush=flush)

here is the entire script for the python print function.
### object(s):
you pass in zero or many objects in the front 

### sep=separator:
this is how the print separets two argument for example if you input two argument like h and i it will print "h i" because the defult is " " an empty space.

### end=end:
this is how the print function ends, like what is put at the end, the defult is a "\n" which means creat a new line.

### file=file:
Optional. An object with a write method. Default is sys.stdout

### flush=flush:
Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is False

inside the print function you can also add f in the frent to make it a format string, 
### example:
```python
name = "jinghong"
print(f"hi {name}")
```
output: `hi jinghong`

this is a format string wich formats the name into "jinghong"

### formating numbers:
input: `1000`
```python
print(f"{z:,}")
```
output: `1,000`

### ways to do rounding:
```python
x = float(2)
y = float(3)
z = x/y
print(f"{z:.2f}")
```
output: `0.67`

## parameters
the parameters is just arguments you passed in a function, which the parameter passed in the print function is called positional parameter, which means positional in the sense that the first thing you pass to the print function get printed first the second thing you pass to print function after a comma get printed seocnd and so forth.
there is named parameters now too, named SEP separatpr, or END the ending for the line. they are named parameters because they are optional and you can pass them in at the end of your print funciton and it will apply to all inside the print function.

## str
its an short term for string, which is a data type that stores words.
which also contains alot of functions that can be applyed to it.
for example:

split function:
input:` jinghong` 
```python
name = name.strip()
```
output: `jinghong`

title function:
input:`jinghong`
```python
name = name.title()
```
output:`Jinghong`

### split function:
input: 'jinghong wang'
```python
first, last = name.split(" ")
```
output:

`first == jinghong`  
  
`last == wang`

## Int
int is a short version to say intiger, which contains numbers with no decimal point.

you would need to translate the input into a int befor doing any kind of caculation.

there is deferent types of caculations you can do including but not limited to:
+"plus, adds the number together."
/"divide, divides the left number by the right."
*"times, times the two number."
%"mod, this dives the left with the right number and gets the remnder"

## float
float is called floating point, which is numbers that contains a decimal.
can do the same kind of caculations at intiger.

### functions:
round(number[, ndigits])

### number:
this is the number you want to round.
### ndigits:
the digits you want to round to for example if you want 0.16 to round to 0.2 then you would use 1 to round to the ten'th place.


## interactive mode
in interactive mode you can write lines of python code and inmmediately execute it.
you can activite it by typeing "python" into the command promp.

## def
def is how you make your own function.
you initalise the funcion with "def" "(name of function)" any thing inside "()" is the input for the function, and end with":"
you can also assing defuilt value to the function just incase if the user dident input any thing. you can assing it by equal inside the "()".
should look like this
### Example
```python
def hello(to = "world"):
    print("hi,", to)
```
output: `hi world`

and any thing thats indented after the ":" is considered inside the function.

how to use the function created:

### Example
```python
hello("jinghong")
```
output: `hi, jinghong`

reasons why you want to use the def function is to first not have to repeat your self, seocnd you could just use the function any where.

you alwast need to define the functions above useing the function

## tips

because of how the code works from top to bottom if you try to use a function befor you initalise it it will cause some proble so you coule make the entire code into an main function and just call that function at the end 
### Example:
input:`jinghong`

```python
def main():
    print("hello, world!")
    name = input()
    hello(name)

def hello(to):
    print(f "hello, {to}")
    
main()
```

output: 

`hello, world!`

`hello, jinghong`
## scope
scope is when a variable only existing in the context in where its been defined

so if you define name inside hello() function you cant use it outside of that function unless you define it again outside the function

## return
this is a way that you could ask the function to return you value, for example if you want to make a caculator thats a function you can input one number and ask it to return the square of that number.

### Example: 
input: `4`

```python
def square(num):
    return (num*num)
```

output: `16`
