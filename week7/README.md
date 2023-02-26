# File I/O
File I/O is the ability of a program to take a file as input or create a file as output.

## basic 
here is some simple code that can simply append names into ordered paires

```python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
```

## open
open is a function in python that allows you to open a file and acess what is in the file and then even modifies it.

example:

```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
```

## close
close is a way to close opend files so it dont use any of the resorses on your currently running machine.

example:
```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

## with 
The keyword `with` allows you to automate the closing of a file.

example:
```python
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```

in this example in the for loop we are appeding all the lines in the file into a list called names and then we are looping through that list to sort all the names and then print it to the screen.

## CSV
CSV stands for “comma separated values”.

example:
```
name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```

code example:
```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```
in this example first you ask the user for the name and home then you open the file with the `with` function, next up you read the csv file with `csv.DictWriter` function which takes in two paramiter and set the comma seprated values equal to the same, lastly the code write into the file with `writer.writerow` fucntion.

## PLI
PLI is a python libery that that works with images, and here we use it to make a gif.


example:
```python
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
```
Notice that we import the Image functionality from PIL. Notice that the first for loop simply loops through the images provided as command-line arguments and stores theme into the list called images. The 1: starts slicing argv at its second element. The last lines of code saves the first image and also appends a second image to it as well, creating an animated gif. Typing python costumes.py costume1.gif costume2.gif into the terminal. Now, type code costumes.gif into the terminal window, and you can now see an animated GIF.