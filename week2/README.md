# Conditionals

## Indentations
since there is no parentheses that indecates where every thing ends we use indentations to indicate where the line start and where the line ends for example if i want to ask if x is 1 then do the blow i need to write it this way

### example:
```python
x = 1
if x == 1 :
    print("x is 1!")
```
output: `x is 1!`

## tips
you can simplify some of the if statenment with exchange them with elif.

## elif
this is a way to simplyfy some if statenments, which will not trigger if a if have a true or false answer. if there is a true retruned then stop asking the question.

### example:
input `3`
```python
y = int(input())
if y == 2:
    print("y is 2")
elif y == 3:
    print("y is 3")
elif y == 4:
    print("y is 4")
```
output `y is 3`

this is an great example for show, since the input is 3 it will pass through the first if statenment but it will stop at the second elif wich will print out `y is 3` but since we are useing elif now we will not go to the third question wich will help alot if you have thousent lines of code.

## else
this is a statenment that would happen if all the if statenment or all elif statenment is false. its usally used to end an if/elif statnment.

## or
this is a key word to ask two question at the same time, for example if you want to ask if the sentence start with an a or start with an z.

### example:
```python
word = "zero"
if word.startwith("z") or word.startwith("a"):
    print("the word start with an a or a z")
else:
    print("the word did not start with an a or a z")
```

## and
this is a key word used to ask if the answer works on both statenment it repersents. for example if you want to ask if the number is divisible by 2 and by 4.

### example:
```python
num = 8
if num % 2 == 0 and num % 4 == 0:
    print("the number is divisible by 2 and 4")
else:
    print("the number is not divisible by 2 and 4")
```

there is also a spectial way to write some codes like:
```python
num = 13
if 4 <= num < 30:
    print("the number is bigger than 3 and less than 30")
```

python alows you to do this insted of using and key word.

## modulo(%)
modulo is a way to caculate reminders.

### example:
```python
num = 15%2
print(num)
```
output: `1`

this shows the reminder for 15 divived by 2 which is 1.

## bool(boolean value)
this is a data type that only contains 2 kind of posibilitys which is a True or False. which have to be caped.

## match
this is a new way for printing out value based on whats the input.

### example:
```python
name = "jinghong"

match name:
    case "jinghong":
        print("hello friend!")
    case "john":
        print("hello friend!")
```
output: `hello friend!`

but if you need an else statnment just like the if else functions you would need to replace the condition with a single underscore "_".

### example:

```python
name = "random"

match name:
    case "jinghong":
        print("hello friend!")
    case "john":
        print("hello friend!")
    case _:
        print("hello")
```
output: `hello`

there is also a way showing or in this new function useing a single vertical bar "|"

### example:
```python
name = "john"

match name:
    case "jinghong" | "john":
        print("hello friend!")
    case _:
        print("hello")
```

output: `hello friend!`
