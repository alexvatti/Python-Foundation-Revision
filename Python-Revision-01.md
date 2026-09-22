
## Python Basics — Before OOPs

### 1. Variables & Data Types

A variable is a name that stores a value.

```python
name = "Alex"
age = 45
height = 170.5
is_working = True
```

Here:

| Variable | Value | Type |
|---|---|---|
| `name` | `"Alex"` | `str` |
| `age` | `45` | `int` |
| `height` | `170.5` | `float` |
| `is_working` | `True` | `bool` |

Check the type:

```python
print(type(age))
```

Output:

```text
<class 'int'>
```

**Simple idea:**  
Variable = **name**  
Value = **data stored in that name**

---

### 2. Mutable vs Immutable

This is an important Python concept.

**Mutable = can be changed**

```python
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
```

Output:

```text
[100, 20, 30]
```

A list can be changed → **mutable**.

**Immutable = cannot be changed**

```python
name = "Alex"

name[0] = "B"
```

This gives an error because a string cannot be changed character-by-character.

Common examples:

```text
Mutable:
list
set
dictionary

Immutable:
int
float
string
tuple
bool
```

**Simple idea:**

> Mutable → change the existing object  
> Immutable → cannot change the existing object

---

### 3. `==` vs `is`

These are often confused.

`==` → compares **values**

`is` → checks whether they are the **same object**

```python
a = [10, 20]
b = [10, 20]

print(a == b)
print(a is b)
```

Output:

```text
True
False
```

Why?

Both contain the same values:

```text
[10, 20]
```

So:

```python
a == b
```

is `True`.

But they are two different list objects.

```python
a is b
```

is `False`.

**Simple rule:**

```text
==  → same value?
is  → same object?
```

---

### 4. Reference vs Copy

Look at this:

```python
a = [10, 20, 30]

b = a

b[0] = 100

print(a)
print(b)
```

Output:

```text
[100, 20, 30]
[100, 20, 30]
```

Why did `a` also change?

Because:

```python
b = a
```

does **not create a new list**.

Both names refer to the same list.

Think:

```text
a ──┐
    └──> [10, 20, 30]
    ↑
b ──┘
```

**Simple idea:**

> `b = a` → both refer to the same object.

---

### 5. Shallow Copy vs Deep Copy

First, understand the basic copy:

```python
a = [10, 20, 30]

b = a.copy()

b[0] = 100

print(a)
print(b)
```

Output:

```text
[10, 20, 30]
[100, 20, 30]
```

Now they are separate lists.

But nested lists make things slightly different.

```python
a = [[10, 20], [30, 40]]

b = a.copy()

b[0][0] = 100

print(a)
print(b)
```

Output:

```text
[[100, 20], [30, 40]]
[[100, 20], [30, 40]]
```

The inner list is still shared.

For a **deep copy**:

```python
import copy

a = [[10, 20], [30, 40]]

b = copy.deepcopy(a)

b[0][0] = 100

print(a)
print(b)
```

Output:

```text
[[10, 20], [30, 40]]
[[100, 20], [30, 40]]
```

**Simple idea:**

```text
copy.copy()       → shallow copy
copy.deepcopy()   → completely separate nested objects
```

---

### 6. List vs Tuple vs Set vs Dictionary

#### List

Ordered and changeable.

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

```text
[10, 20, 30, 40]
```

#### Tuple

Ordered but cannot be changed.

```python
numbers = (10, 20, 30)

print(numbers[0])
```

```text
10
```

#### Set

Stores unique values.

```python
numbers = {10, 20, 20, 30}

print(numbers)
```

The duplicate `20` is removed.

```text
{10, 20, 30}
```

#### Dictionary

Stores **key → value**.

```python
student = {
    "name": "Alex",
    "age": 45
}

print(student["name"])
```

Output:

```text
Alex
```

**Easy memory:**

```text
List       → ordered collection
Tuple      → fixed collection
Set        → unique values
Dictionary → key-value data
```

---

### 7. Indexing & Slicing

Indexing means getting one item.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
```

Output:

```text
10
30
```

Python starts from **0**.

```text
10   20   30   40   50
↑    ↑    ↑
0    1    2
```

Slicing gets multiple values.

```python
print(numbers[1:4])
```

Output:

```text
[20, 30, 40]
```

Meaning:

```text
start = 1
stop  = 4
```

The `4` is **not included**.

**Simple rule:**

```python
numbers[start:stop]
```

---

### 8. Functions & Parameters

A function is a reusable block of code.

```python
def add(a, b):
    return a + b
```

Call it:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

Here:

```text
a, b → parameters
10,20 → arguments
```

**Simple idea:**

> Function = write code once, use it many times.

---

### 9. Positional vs Keyword Arguments

#### Positional

Position matters.

```python
def student(name, age):
    print(name, age)

student("Alex", 45)
```

Output:

```text
Alex 45
```

#### Keyword

Use the parameter name.

```python
student(age=45, name="Alex")
```

Output:

```text
Alex 45
```

Here the order doesn't matter.

**Simple:**

```text
student("Alex", 45)
→ positional

student(age=45, name="Alex")
→ keyword
```

---

### 10. Default Arguments

You can give a parameter a default value.

```python
def greet(name="Alex"):
    print("Hello", name)
```

Call without argument:

```python
greet()
```

Output:

```text
Hello Alex
```

Call with argument:

```python
greet("John")
```

Output:

```text
Hello John
```

**Simple idea:**

> If the caller doesn't provide a value, Python uses the default.

---

### 11. `*args` vs `**kwargs`

`*args` → many positional arguments.

```python
def add(*args):
    print(args)

add(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`**kwargs` → many keyword arguments.

```python
def student(**kwargs):
    print(kwargs)

student(name="Alex", age=45)
```

Output:

```text
{'name': 'Alex', 'age': 45}
```

**Easy memory:**

```text
*args    → many positional values
**kwargs → many named values
```

---

### 12. Local vs Global Variables

```python
name = "Alex"       # global

def test():
    age = 45        # local
    print(name)
    print(age)

test()
```

`name` is available outside and inside the function.

`age` belongs only to the function.

**Simple:**

```text
Global → outside function
Local  → inside function
```

---

### 13. LEGB Rule

Python searches for a variable in this order:

```text
L → Local
E → Enclosing
G → Global
B → Built-in
```

Example:

```python
name = "Global"

def test():
    name = "Local"
    print(name)

test()
```

Output:

```text
Local
```

Python finds the **local** variable first.

**Easy memory:**

> Python looks nearby first, then moves outward.

---

### 14. `return` vs `yield`

`return` gives back a result and finishes the function.

```python
def numbers():
    return [1, 2, 3]

print(numbers())
```

Output:

```text
[1, 2, 3]
```

`yield` produces values one at a time.

```python
def numbers():
    yield 1
    yield 2
    yield 3
```

Use:

```python
for n in numbers():
    print(n)
```

Output:

```text
1
2
3
```

**Simple:**

```text
return → give result and finish
yield  → give one value at a time
```

---

### 15. Iterable vs Iterator

A **list is iterable**.

```python
numbers = [10, 20, 30]

for n in numbers:
    print(n)
```

An **iterator** remembers where it is.

```python
numbers = [10, 20, 30]

it = iter(numbers)

print(next(it))
print(next(it))
```

Output:

```text
10
20
```

**Simple idea:**

```text
Iterable → can be looped over
Iterator → gives next item
```

---

### 16. Generator

A generator uses `yield`.

```python
def numbers():
    for i in range(3):
        yield i

for n in numbers():
    print(n)
```

Output:

```text
0
1
2
```

The important idea:

> Generator produces values when needed instead of creating everything at once.

---

### 17. `lambda`

A lambda is a small anonymous function.

Normal function:

```python
def square(x):
    return x * x
```

Lambda:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

**Simple:**

> `lambda` = small one-line function.

---

### 18. `map()` vs `filter()` vs `reduce()`

Suppose:

```python
numbers = [1, 2, 3, 4]
```

`map()` → change every item.

```python
result = map(lambda x: x * 2, numbers)

print(list(result))
```

```text
[2, 4, 6, 8]
```

`filter()` → select items.

```python
result = filter(lambda x: x > 2, numbers)

print(list(result))
```

```text
[3, 4]
```

`reduce()` → combine into one result.

```python
from functools import reduce

result = reduce(lambda a, b: a + b, numbers)

print(result)
```

```text
10
```

**Easy memory:**

```text
map    → change
filter → select
reduce → combine
```

---

### 19. Exception Handling

Used when something can cause an error.

```python
try:
    number = 10 / 0
except:
    print("Something went wrong")
```

Output:

```text
Something went wrong
```

Without `try/except`, the program stops with an error.

**Simple idea:**

> Exception handling lets your program handle expected errors gracefully.

---

### 20. `try` vs `except` vs `else` vs `finally`

```python
try:
    number = int("10")

except:
    print("Error")

else:
    print("Success")

finally:
    print("Done")
```

Output:

```text
Success
Done
```

Meaning:

```text
try     → try the code
except  → if error happens
else    → if no error
finally → always execute
```

---

### 21. `raise` vs `assert`

`raise` deliberately creates an exception.

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

`assert` checks whether something is true.

```python
age = 20

assert age >= 18
```

If the condition is false, an `AssertionError` occurs.

**Simple:**

```text
raise  → create an error yourself
assert → check that something is true
```

---

### 22. File Handling

Write to a file:

```python
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

Read:

```python
file = open("data.txt", "r")

data = file.read()

print(data)

file.close()
```

Output:

```text
Hello Python
```

**Simple:**

```text
"w" → write
"r" → read
"a" → append
```

---

### 23. `with` / Context Manager

Instead of manually closing:

```python
file = open("data.txt", "r")
data = file.read()
file.close()
```

Use:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Python handles closing the file.

**Simple idea:**

> `with` safely manages resources for you.

---

### 24. Module vs Package

A **module** is normally a Python file.

```text
math_utils.py
```

Example:

```python
# math_utils.py

def add(a, b):
    return a + b
```

Use it:

```python
import math_utils

print(math_utils.add(10, 20))
```

A **package** is a directory containing Python modules.

```text
my_package/
    __init__.py
    math_utils.py
    string_utils.py
```

**Simple:**

```text
Module  → .py file
Package → folder containing modules
```

---

### 25. `import` vs `from ... import`

```python
import math

print(math.sqrt(25))
```

You use:

```text
math.sqrt()
```

With:

```python
from math import sqrt

print(sqrt(25))
```

You can directly use:

```text
sqrt()
```

**Simple:**

```text
import math
→ use math.sqrt()

from math import sqrt
→ use sqrt()
```

---

### 26. Mutable Default Arguments

This is a **Python trap**.

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Because the same default list can be reused.

Better:

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

**Simple rule:**

> Don't use a mutable object like `[]` or `{}` as a default parameter.

---

### 27. Recursion

A function calling itself is recursion.

```python
def count(n):

    if n == 0:
        return

    print(n)

    count(n - 1)

count(3)
```

Output:

```text
3
2
1
```

There must be a **stopping condition**.

```python
if n == 0:
    return
```

**Simple:**

> Recursion = function calls itself until a stopping condition is reached.

---

### 28. `*` Unpacking vs `**` Unpacking

`*` unpacks a list/tuple.

```python
numbers = [10, 20, 30]

print(*numbers)
```

Output:

```text
10 20 30
```

`**` unpacks a dictionary into keyword arguments.

```python
data = {
    "name": "Alex",
    "age": 45
}

def student(name, age):
    print(name, age)

student(**data)
```

Output:

```text
Alex 45
```

**Simple:**

```text
*  → unpack sequence
** → unpack dictionary
```

---

### 29. List / Set / Dictionary Comprehensions

Normal list:

```python
numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
```

Comprehension:

```python
numbers = [i for i in range(5)]

print(numbers)
```

Output:

```text
[0, 1, 2, 3, 4]
```

With condition:

```python
even = [i for i in range(10) if i % 2 == 0]

print(even)
```

Output:

```text
[0, 2, 4, 6, 8]
```

**Simple:**

> Comprehension = short way to create a collection.

---

### 30. `pass` vs `continue` vs `break`

#### `pass`

Do nothing.

```python
for i in range(3):
    pass
```

#### `continue`

Skip current iteration.

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

#### `break`

Stop the loop completely.

```python
for i in range(5):

    if i == 2:
        break

    print(i)
```

Output:

```text
0
1
```

**Easy memory:**

```text
pass     → do nothing
continue → skip this round
break    → stop the loop
```

---

## The most important ones to really understand

For your **Python → OOP transition**, I would pay extra attention to these:

```text
1. Mutable vs Immutable
2. == vs is
3. Reference vs Copy
4. Shallow vs Deep Copy
5. Functions & Parameters
6. *args / **kwargs
7. Local / Global / LEGB
8. return / yield
9. Iterable / Iterator / Generator
10. Exception Handling
11. Mutable Default Arguments
12. Recursion
13. * / ** Unpacking
```

These are the concepts where **small differences cause big confusion later**.
