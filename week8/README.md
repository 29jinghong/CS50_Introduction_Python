# Regular Expressions

Regular expressions or “regexes” will enable us to examine patterns within our code. For example, we might want to validate that an email address is formatted correctly. Regular expressions will enable us to examine expressions in this fashion.

```python
import re

email = input("What's your email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")
```
this code ask the use to input a email and check is the email end with `'@'` and `'email'`

here is the rule for regular expression:

```
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
```

so we can use this code

```python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
```
to check if the email have `'1 or more letters'` and have a `'@'` and then have `'1 or more letters'` then end with `'email'`

```
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string
```

then we can modify our code using our added vocabulary as follows:

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

We propose we can do even better! Even though we are now looking for the username at the start of the string, the @ symbol, and the domain name at the end, we could type in as many @ symbols as we wish! malan@@@harvard.edu is considered valid!

```
[]    set of characters
[^]   complementing the set
```

```
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character
```

```
A|B     either A or B
(...)   a group
(?:...) non-capturing version
```

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
```
this takes email that are not simply .edu email addresses.

## Case Sensitivity

To illustrate how you might address issues around case sensitivity, where there is a difference between EDU and edu and the like, let’s rewind our code to the following:

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

Notice how we have removed the | statements provided previously.

Recall that within the re.search function, there is a parameter for flags.

## Cleaning Up User Input

You should never expect your users to always follow your hopes for clean input. Indeed, users will often violate your intentions as a programmer.
There are ways to clean up your data.

```python 
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"

print(f"hello, {name}")
```

## Extracting User Input

Now, let’s extract some specific information from user input. In the terminal window, type code twitter.py and code as follows in the text editor window:

```python
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
```

Notice that the [a-z0-9_]+ tells the compiler to only expect a-z, 0-9, and _ as part of the regular expression. The + indicates that we are expecting one or more characters.
