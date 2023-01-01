# Loops 
is a block of code thats going to do someting again and again as many times as you want.

example:
```python
for i in range(3):
    print("woof")
```

## while
This is a way to loop a serten code multiple times useing a form of asking a question.


example:
``` python
x = 0
while x > 2:
    print("woof")
    x = x+
```
output: `woof woof woof`

### accidental infinite loop
this is a mistake that could happen if you forgot to make your loop stop which it will keep on going for ever, but you can stop it by forcefuly stoping the loop by pressing `Control c` for cancel.

### tips
in the coding convention counting up numbers usally starts at 0 insted of 1 since for list they start at 0 too. 

you can use the `*` to print mutiple at the same time.

example:
```python
print("woof" * 3)
```
### range
this is a function to use to get a list of any number you want for example if you want to get from 0 to 10 then you would type `range(10)` 

### break
break is a function to forcefully break out the loop.

example:
```python
nums = [6, 0, 9, 8]
for i in range(nums):
    print(i)
```
output:`1 2 3 4`

### len
this is a function that you can perform to a list and will tell you the length of that list.
```python
nums = [2, 4, 5, 6]
print(len(4))
```
output:`4`

## for loop
its a simular function as the while loop but in this loop you can perform looping a list.


## list
is a list of data type for example 
its a way to contain multiple value all in the same place.

example:
```python
[0,1,2]
```
this is a int list that have the number 1,2 ,and 3.
you can also loop the list.

example:
```python
for i in [0,1,2]:
    print(i)
```
output: `0 1 2`

## dict
this is a way to let you associate something with something else, with a key and a value.

example:
```python
students = {
    "jinghong":"19",
    "jingyang":"12",
    "lei":"53"
    "quan":"50"
}
print(students[jinghong])
```
output:`19`

### list and dict
this is a way that you can repersent multiple values in dictonary.
example:
```python
students = [
    {"name":"jinghong","age":"19", "sex":"male"}
    {"name":"jingyang","age":"12", "sex":"male"}
    {"name":"lei","age":"53", "sex":"male"}
    {"name":"quan","age":"50", "sex":"female"}
]
for student in students:
    print(student{name})
```
output:`jinghong jingyang lei quan`

## None
this is a data type repersent literly nothing which is called none.

## nested loop
this is porforming a loop inside a loop.

example:

```python
for i in range(2):
    for x in range(2):
        print(x)
```
output:`0 1 2 0 1 2 0 1 2`