# Python Foundation — Practice Questions (No OOP)

> LeetCode-style but keep it simple. Topics: comprehensions (list/dict/set/tuple),
> file open & read, try/except, math, random, datetime, regular expressions,
> and a few "confusing" tricky questions.
>
> **Rules:** No classes / no OOP. Only functions, built-ins, and the standard
> modules mentioned. Write your own solutions — answers are intentionally omitted.

---

## Section A — Comprehensions (List / Dict / Set / Tuple)

**Q1.** Given a list of numbers, use a **list comprehension** to return a new list
containing only the squares of the **even** numbers.
Example: `[1, 2, 3, 4, 5, 6]` → `[4, 16, 36]`

**Q2.** Using a **dict comprehension**, build a dictionary that maps each word in a
sentence to its length. Ignore case and split on spaces.
Example: `"the quick brown fox"` → `{'the': 3, 'quick': 5, 'brown': 5, 'fox': 3}`

**Q3.** Given two lists (`keys` and `values`) of equal length, use a **dict
comprehension** with `zip()` to combine them into a single dictionary.

**Q4.** Use a **set comprehension** to return the set of all unique first letters
(lowercased) from a list of names.
Example: `["Alex", "amy", "Bob", "brian"]` → `{'a', 'b'}`

**Q5.** Use a **nested list comprehension** to flatten a 2D matrix into a single
list. Example: `[[1, 2], [3, 4], [5, 6]]` → `[1, 2, 3, 4, 5, 6]`

**Q6.** Given a list of integers, use a comprehension to build a list of **tuples**
`(number, "even")` or `(number, "odd")` depending on parity.
Example: `[1, 2, 3]` → `[(1, 'odd'), (2, 'even'), (3, 'odd')]`

---

## Section B — File Opening & Reading

**Q7.** Write a function that opens a text file (using `with open(...)`) and returns
the **total number of lines** in it.

**Q8.** Read a text file and return a dictionary counting how many times each
**word** appears (case-insensitive). Use file reading + a dict.

**Q9.** Write a function that reads a file and prints only the lines that contain
the word `"error"` (case-insensitive). Strip trailing newline characters.

**Q10.** Read a file of numbers (one number per line) and return their **sum** as a
float. (Hint: you'll need to convert strings to numbers.)

---

## Section C — Try / Except (Error Handling)

**Q11.** Write a function `safe_divide(a, b)` that returns `a / b`, but returns the
string `"Cannot divide by zero"` if `b` is `0`. Use `try/except`.

**Q12.** Write a function that takes a list of strings and tries to convert each to
an `int`. Collect the successful conversions in one list and the failures in
another. Use `try/except` inside a loop.

**Q13.** Write a function that opens a file by name and returns its contents, but
returns `"File not found"` if the file does not exist (catch
`FileNotFoundError`).

---

## Section D — math Module

**Q14.** Write a function that takes the radius of a circle and returns its area
using `math.pi`. Round the result to 2 decimal places.

**Q15.** Given the two shorter sides of a right triangle, use `math.sqrt()` to
return the length of the hypotenuse.

**Q16.** Write a function that returns `True` if a given number is a **perfect
square**, using `math.sqrt()` and `math.isqrt()`.

---

## Section E — random Module

**Q17.** Write a function that simulates rolling two dice `n` times and returns a
dictionary counting how often each **total** (2–12) appeared. Use
`random.randint()`.

**Q18.** Given a list, use the `random` module to (a) shuffle it and (b) pick 3
unique random items from it (`random.sample`).

---

## Section F — datetime Module

**Q19.** Write a function that takes a birth year and returns the person's age using
`datetime` (based on the current year).

**Q20.** Write a function that takes two date strings in the format `"YYYY-MM-DD"`
and returns the **number of days** between them. Use
`datetime.strptime()`.

---

## Section G — Regular Expressions (re Module)

**Q21.** Write a function that uses `re` to extract all **email addresses** from a
block of text and returns them as a list.

**Q22.** Use `re` to check whether a string is a **valid 10-digit phone number**
(digits only, exactly 10). Return `True` or `False`.

**Q23.** Given a sentence, use `re.findall()` to return all words that start with a
**capital letter**.

---

## Section H — "Confusing" / Tricky Questions

**Q24.** What is the difference between the following, and what does each print?
```python
a = [1, 2, 3]
b = a
c = a[:]
b.append(4)
print(a)   # ?
print(c)   # ?
```

**Q25.** Predict the output and explain why:
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))
```

**Q26.** Explain the difference between these two and predict each output:
```python
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
```

**Q27.** What is printed and why? (Integer caching / identity vs equality)
```python
x = 256
y = 256
print(x is y)   # ?

a = 257
b = 257
print(a is b)   # ?
```

**Q28.** Predict the output of this comprehension scoping puzzle:
```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])
```

**Q29.** Explain the difference in output:
```python
print("5" * 3)
print(5 * 3)
print("5" + "3")
```

**Q30.** What does each line return, and why can slicing be confusing here?
```python
s = "python"
print(s[::-1])   # ?
print(s[1:4])    # ?
print(s[-2:])    # ?
```
