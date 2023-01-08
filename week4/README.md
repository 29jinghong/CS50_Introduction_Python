# exceptions
execptions are things that can go wrong in your code.

## SyntaxError
this is one of the execptions in python which is when you have some thing in your code thats not folloing the syntax of python.

example:

```python
print("hello world)
```

output: `SynntaxError: unterminated string literal(detected at line 1)`

## ValueError
this is a error that happens when the value of some thing goes wrong


example:

input: `cat`
```python
x int(input("what is x: "))
print(f"x is {x}")
```
output: `ValueError: invalid literal for int() with base 10: 'cat'`

## try
this is the key work that makes the program try some thing and chekc it it works nor not.

## except
this is a key word that indicats what happens if try dont work.

example:

input: `cat`
 
```python
try:
    x = int(input("what is x? "))
exept ValueError:
    print("x is not an intiger.")
```
output: `x is not an intiger`

