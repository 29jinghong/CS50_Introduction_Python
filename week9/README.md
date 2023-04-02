# Object-Oriented Programming
Object-oriented programming (OOP) is a compelling solution to programming-related problems.

Notice that this program follows a procedural, step-by-step paradigm: Much like you have seen in prior parts of this course.

Drawing on our work from previous weeks, we can create functions to abstract away parts of this program.

```python
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main()
```

Notice how get_name and get_house abstract away some of the needs of our main function. Further, notice how the final lines of the code above tell the compiler to run the main function.

We can further simplify our program by storing the student as a tuple. A tuple is a sequences of values. Unlike a list, a tuple can’t be modified. In spirit, we are returning two values.

```python
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()

```
Packing that tuple, such that we are able to return both items to a variable called student, we can modify our code as follows.

```python
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
```

the finnal version:

```python
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
```
Notice how, similar in spirit to our previous iterations of this code, we can utilize the key names to index into our student dictionary.

## Classes

Classes are a way by which, in object-oriented programming, we can create our own type of data and give them names.
A class is like a mold for a type of data – where we can invent our own data type and give them a name.
We can modify our code as follows to implement our own class called Student:

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
```

We can simplify our code as follows:
```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

## raise

Object-oriented program encourages you to encapusulate all the functionality of a class within the class definition. What if something goes wrong? What if someone tries to type in something random? What if someone tries to create a student without a name? Modify your code as follows:
```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

Notice how we check now that a name is provided and a proper house is designated. It turns out we can create our own exceptions that alerts the programmer to a potential error created by the user called raise. In the case above, we raise ValueError with a specific error message.

It just so happens that Python allows you to create a specific function by which you can print the attributes of an object. Modify your code as follows:

```python
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
```

Notice how def __str__(self) provides a means by which a student is returned when called. Therefore, you can now, as the programmer, print an object, its attributes, or almost anything you desire related to that object.

__str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods for a class as well! Modify your code as follows:

```python
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
```

Notice how we define our own method charm. Unlike dictionaries, classes can have built-in functions called methods. In this case, we define our charm method where specific cases have specific results. Further, notice that Python has the ability to utilize emojis directly in our code.

Before moving forward, let us remove our patronus code. Modify your code as follows:

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```
Notice how we have only two methods: __init__ and __str__.

## Decorators

Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which begin with @. Modify your code as follows:

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```
Notice how we’ve written `@property` above a function called `house`. Doing so defines `house` as a property of our class. With `house` as a property, we gain the ability to define how some attribute of our class, `_house`, should be set and retrieved. Indeed, we can now define a function called a “setter”, via @house.setter, which will be called whenever the house property is set—for example, with student.house = "Gryffindor". Here, we’ve made our setter validate values of house for us. Notice how we raise a ValueError if the value of house is not any of the Harry Potter houses, otherwise, we’ll use house to update the value of _house. Why _house and not house? house is a property of our class, with functions via which a user attempts to set our class attribute. _house is that class attribute itself. The leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. _house should only be set through the house setter. Notice how the house property simply returns that value of _house, our class attribute that has presumably been validated using our house setter. When a user calls student.house, they’re getting the value of _house through our house “getter”.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```

Notice how, much like the previous code, we provide a getter and setter for the name.

Here is a link to the method page
`https://docs.python.org/3/tutorial/classes.html`

## Class Methods

Sometimes, we want to add functionality to a class itself, not to instances of that class.
@classmethod is a function that we can use to add functionality to a class as a whole.

```python
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
```

## Static Methods

It turns out that besides @classmethods, which are distinct from instance methods, there are other types of methods as well.
Using @staticmethod may be something you might wish to explore. While not covered explicitly in this course, you are welcome to go and learn more about static methods and their distinction from class methods.

## Inheritance

Inheritance is, perhaps, the most powerful feature of object-oriented programming.
It just so happens that you can create a class that “inherits” methods, variables, and attributes from another class.

```python
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...
```

Notice that there is a class above called Wizard and a class called Student. Further, notice that there is a class called Professor. Both students and professors have names. Also, both students and professors are wizards. Therefore, both Student and Professor inherit the characteristics of Wizard. Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line super().__init__(name) runs the init method of Wizard. Finally, notice that the last lines of this code create a wizard called Albus, a student called Harry, and so on.

## Inheritance and Exceptions

While we have just introduced inheritance, we have been using this all along during our use of exceptions.
It just so happens that exceptions come in a heirarchy, where there are children, parent, and grandparent classes. These are illustrated below:

```
BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...
 ```

## Operator Overloading
Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.
In your terminal window, type code vault.py. Then, code as follows:

 ```python
 class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)
 ```
 Notice how the __str__ method returns a formatted string. Further, notice how the __add__ method allows for the addition of the values of two vaults. self is what is on the left of the + operand. other is what is right of the +.
