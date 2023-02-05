# test
This is used to test a function to see if it works so you dont have to manuly test it.

you can acomplish this by writing some test cases.

example
```python
import square from caculator
def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("square root of 2 is not equal to 4")
    if square(3) != 9:
        print("square root of 3 is not equal to 9")

if __name__ == "__main__":
    main()
```

in this example you can see that we have tested the square function in caculator.py which should give back a 4 if you enter 2 and give back a 9 if you enter 3.

## assert
this function is used to make sure that some thing is true or boldly claim that some thing is true, and if it is not true its going to raise a AssertionError

## AssertionError
this is a error that happens when assert is false.

## pytest