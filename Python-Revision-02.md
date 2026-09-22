# Python Standard Library — `math`, `datetime`, `random`, `re`

## 1. `math` Module

### Import

```python
import math
```

### Common Functions

| Function | Purpose | Example |
|---|---|---|
| `math.sqrt()` | Square root | `math.sqrt(25)` → `5.0` |
| `math.pow()` | Power | `math.pow(2, 3)` → `8.0` |
| `math.ceil()` | Round up | `math.ceil(4.2)` → `5` |
| `math.floor()` | Round down | `math.floor(4.8)` → `4` |
| `math.factorial()` | Factorial | `math.factorial(5)` → `120` |
| `math.gcd()` | Greatest common divisor | `math.gcd(12, 8)` → `4` |
| `math.fabs()` | Absolute value as float | `math.fabs(-5)` → `5.0` |
| `math.pi` | π | `3.14159...` |

### Import specific function

```python
from math import sqrt

print(sqrt(25))
```

### Confusing Questions

**Q1. What is the difference?**

```python
math.sqrt(25)
```

vs

```python
math.pow(25, 0.5)
```

**Q2. What is the output?**

```python
import math

print(math.ceil(4.1))
print(math.floor(4.9))
```

**Q3. What is the difference?**

```python
abs(-10)
```

vs

```python
math.fabs(-10)
```

**Q4. What is the output?**

```python
from math import sqrt

print(sqrt(16))
print(math.sqrt(16))
```

**Q5. What is wrong here?**

```python
from math import sqrt

print(math.sqrt(25))
```

---

# 2. `datetime` Module

## Import

```python
import datetime
```

### Current date and time

```python
now = datetime.datetime.now()

print(now)
```

### Current date

```python
today = datetime.date.today()

print(today)
```

### Create a date

```python
date = datetime.date(2026, 8, 7)

print(date)
```

### Create a time

```python
time = datetime.time(10, 30, 0)

print(time)
```

### Date difference

```python
from datetime import date

d1 = date(2026, 8, 1)
d2 = date(2026, 8, 7)

print(d2 - d1)
```

Output:

```text
6 days, 0:00:00
```

### `timedelta`

Used to add/subtract time.

```python
from datetime import date, timedelta

today = date.today()

tomorrow = today + timedelta(days=1)

print(tomorrow)
```

### Confusing Questions

**Q1. What is the difference?**

```python
datetime.date.today()
```

vs

```python
datetime.datetime.now()
```

**Q2. What is the output?**

```python
from datetime import date

d1 = date(2026, 8, 10)
d2 = date(2026, 8, 20)

print(d2 - d1)
```

**Q3. What is the output?**

```python
from datetime import date, timedelta

d = date(2026, 8, 7)

print(d + timedelta(days=10))
```

**Q4. What is wrong?**

```python
import datetime

print(datetime.date.today())
print(datetime.today())
```

**Q5. What is the difference?**

```python
import datetime

datetime.datetime.now()
```

vs

```python
from datetime import datetime

datetime.now()
```

---

# 3. `random` Module

## Import

```python
import random
```

### Random integer

```python
print(random.randint(1, 10))
```

Possible values:

```text
1 2 3 4 5 6 7 8 9 10
```

**Important:** `randint()` includes both ends.

### Random choice

```python
names = ["Alex", "John", "Sam"]

print(random.choice(names))
```

### Random float

```python
print(random.random())
```

Returns a value between:

```text
0.0 <= value < 1.0
```

### Random number in range

```python
print(random.randrange(1, 10))
```

Possible values:

```text
1 to 9
```

`10` is excluded.

### Shuffle

```python
numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)
```

The list is changed randomly.

### Sample

```python
numbers = [1, 2, 3, 4, 5]

print(random.sample(numbers, 2))
```

Returns 2 different elements.

### Confusing Questions

**Q1. Difference?**

```python
random.randint(1, 10)
```

vs

```python
random.randrange(1, 10)
```

**Q2. What values are possible?**

```python
random.randrange(5)
```

**Q3. What values are possible?**

```python
random.randint(5, 10)
```

**Q4. Difference?**

```python
random.choice(numbers)
```

vs

```python
random.sample(numbers, 2)
```

**Q5. What happens to `numbers`?**

```python
numbers = [1, 2, 3, 4]

result = random.shuffle(numbers)

print(result)
print(numbers)
```

**Q6. What is the difference?**

```python
random.random()
```

vs

```python
random.randint(1, 10)
```

---

# 4. `re` — Regular Expressions

`re` is used for **searching and matching patterns in strings**.

## Import

```python
import re
```

### `re.search()`

Search anywhere in the string.

```python
text = "I am learning Python"

result = re.search("Python", text)

print(result)
```

If found, it returns a match object.

### `re.match()`

Checks only from the **beginning**.

```python
text = "Python is easy"

result = re.match("Python", text)

print(result)
```

### `re.findall()`

Find all matches.

```python
text = "cat bat rat"

result = re.findall("at", text)

print(result)
```

Output:

```text
['at', 'at', 'at']
```

### `re.sub()`

Replace matching text.

```python
text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)
```

Output:

```text
I like Python
```

---

## Common Regex Patterns

| Pattern | Meaning |
|---|---|
| `\d` | Digit |
| `\D` | Not a digit |
| `\w` | Word character |
| `\W` | Not a word character |
| `\s` | Whitespace |
| `.` | Any character |
| `^` | Start |
| `$` | End |
| `+` | One or more |
| `*` | Zero or more |
| `?` | Zero or one |

### Example — Find numbers

```python
text = "My age is 45"

result = re.findall(r"\d+", text)

print(result)
```

Output:

```text
['45']
```

### Example — Find words

```python
text = "Python is very easy"

result = re.findall(r"\w+", text)

print(result)
```

Output:

```text
['Python', 'is', 'very', 'easy']
```

### Confusing Questions

**Q1. Difference?**

```python
re.match()
```

vs

```python
re.search()
```

**Q2. What is the output?**

```python
import re

text = "abc123xyz456"

print(re.findall(r"\d+", text))
```

**Q3. What is the difference?**

```python
r"\d"
```

vs

```python
r"\d+"
```

**Q4. What does this mean?**

```python
r"^Python"
```

**Q5. What does this mean?**

```python
r"Python$"
```

**Q6. What is the output?**

```python
text = "cat bat car"

print(re.findall(r"ca.", text))
```

**Q7. What is the difference?**

```python
re.findall()
```

vs

```python
re.search()
```

**Q8. What does `+` mean?**

```python
r"\d+"
```

**Q9. What does `*` mean?**

```python
r"\d*"
```

**Q10. What does `?` mean?**

```python
r"\d?"
```

---

# Quick Revision — Important Confusions

```text
MATH
sqrt()       → square root
pow()        → power
ceil()       → round up
floor()      → round down

DATETIME
date         → date only
datetime     → date + time
timedelta    → duration/difference

RANDOM
randint(a,b)     → b included
randrange(a,b)   → b excluded
choice()         → one item
sample()         → multiple items
shuffle()        → changes the list

RE
match()      → beginning
search()     → anywhere
findall()    → all matches
sub()        → replace

REGEX
\d     → digit
\d+    → one or more digits
\d*    → zero or more digits
\d?    → zero or one digit
^      → start
$      → end
```

### Core revision questions

1. `import math` vs `from math import sqrt`?
2. `sqrt()` vs `pow()`?
3. `ceil()` vs `floor()`?
4. `date` vs `datetime`?
5. `datetime.now()` vs `date.today()`?
6. `timedelta` — why is it used?
7. `randint()` vs `randrange()`?
8. `choice()` vs `sample()`?
9. Why does `shuffle()` return `None`?
10. `re.match()` vs `re.search()`?
11. `re.search()` vs `re.findall()`?
12. `\d` vs `\d+`?
13. `+` vs `*` vs `?`?
14. `^` vs `$`?
15. What does `r` before a regex string mean?
