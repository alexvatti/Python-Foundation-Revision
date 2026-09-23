# Python Foundation – 40 Skill Test Questions (Set 2)

A mix of **True/False**, **Predict the Output**, and **Write the Code** questions.
Write your answer right after each question. No answer key here — attempt everything.

---

## Section A – True / False (Q1–Q10)

**Q1.** A Python dictionary preserves the insertion order of its keys (Python 3.7+).
`True / False` - oder of insertion keys Matters - True

**Q2.** You can concatenate a list and a tuple directly using the `+` operator.
`True / False` - False

**Q3.** `len()` works on strings, lists, tuples, dictionaries, and sets.
`True / False` - True it works strings,lists,tupes,sets , dict on keys

**Q4.** The expression `not not True` evaluates to `False`.
`True / False` - False -let me check once

**Q5.** A function without a `return` statement returns `None`.
`True / False` - True -return None -Confident

**Q6.** Slicing a list with `[::-1]` modifies the original list in place.
`True / False` - No it will not change the original in Place -

**Q7.** `"5" + 5` is a valid expression in Python.
`True / False` - No - False -

**Q8.** Sets in Python are ordered collections.
`True / False` - no , it unordered collection

**Q9.** The `and` operator returns a boolean value only (never an operand).
`True / False` - I need clarity on this question with example -so that i can answer better

**Q10.** `global` keyword lets a function modify a variable defined outside it.
`True / False` -  yes True, to modify the global - outside 

---

## Section B – Predict the Output (Q11–Q28)

**Q11.**
```python
print(7 % 4, -7 % 4) #ans  3 , 3
```

**Q12.**
```python
print("abc"[1:]) # ans "bc"
```

**Q13.**
```python
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a, b) #ans [1,2,3] [1,2,3,4]
```

**Q14.**
```python
print(list("hi") + [1, 2]) #ans  ["h","i",1,2] , i can not say the order , but values are these 
```

**Q15.**
```python
print(1 == True, 0 == False, 2 == True) #ans  True, True, False
```

**Q16.**
```python
d = {"x": 1}
d["y"] = d.get("y", 0) + 5
print(d) # ans {"x":1, "y":5}
```

**Q17.**
```python
print("a,b,c".split(",")) # ans ["a","b","c"]
print("-".join(["a", "b", "c"])) # ans "a-b-c"
```

**Q18.**
```python
nums = [1, 2, 3, 4]
nums[1:3] = [9]
print(nums) #ans [1,9,4]
```

**Q19.**
```python
print(sorted([3, 1, 2], reverse=True)) #ans [3,2,1]
```

**Q20.**
```python
x = 5
print("even" if x % 2 == 0 else "odd") #ans "odd"
```

**Q21.**
```python
def g(a, b=2, c=3):
    return a + b + c
print(g(1, c=10)) #ans 13
```

**Q22.**
```python
print([x for x in range(10) if x % 3 == 0])#ans [0,3,6,9]
```

**Q23.**
```python
t = (1,)
print(type(t), len(t)) #ans tuple, 1
```

**Q24.**
```python
s = "Hello"
print(s.upper(), s.lower(), s) #ans "HELLO", "hello", "Hello"
```

**Q25.**
```python
print(list(enumerate(["a", "b", "c"]))) # [(0,"a),(1,"b),(2,"c")]
```

**Q26.**
```python
print(max("apple", "banana", key=len)) # ans banana
```

**Q27.**
```python
nums = [1, 2, 3]
print(sum(nums), min(nums), max(nums)) #ans 6, 1,3
```

**Q28.**
```python
print(list(zip([1, 2, 3], ["a", "b"]))) #ans [(1,"a),(2,"b")]# bot need  list need to equal -that is my understanding 
```

---

## Section C – Write the Code / Short Answer (Q29–Q40)

**Q29.** Write a list comprehension that produces the cubes of odd numbers from 1 to 10 (inclusive).
l = [i*i*i for i in rnage(1,11) if i%2!=0 ]

**Q30.** Write a function `count_vowels(s)` that returns how many vowels are in a string.

def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeoiu":
            count = count + 1
    return count

**Q31.** Given `nums = [5, 3, 8, 1, 9, 2]`, write code to find the smallest number without using `min()`.

min_val = nums[0]
for val in nums:
    if min_val > val:
        min_val = val
print(min_val)

**Q32.** Write a dictionary comprehension that maps each word in `["hi", "bye", "ok"]` to its length.

case 1:
dict_result = {}
for word in list_names: # i have takent eh list_names as ["hi", "bye", "ok"]
    dict[word]=len(word)
print(dict_result)

case 2: dictionary comprehension 
dict_result = {word:len(word) for word in list_names }

**Q33.** Write code that merges two dictionaries `d1 = {"a": 1}` and `d2 = {"b": 2}` into one.

d1.update(d2) # it will merge - as per my understanding
d_final = d1

**Q34.** Write a function `sum_to_n(n)` using recursion that returns 1 + 2 + ... + n.
def sum_to_n(n):
    if n==1:
        return 1
    return n+sum_to_n(n-1)

**Q35.** Given `pairs = [(1, "a"), (2, "b"), (3, "c")]`, use a loop to build a dict `{1: "a", 2: "b", 3: "c"}`.
dict_result = {}
for pair in pairs:
    dict_result[pair[0]]=pair[1]
print(dict_result)

**Q36.** Write code to find all numbers common to both lists `a = [1, 2, 3, 4]` and `b = [3, 4, 5, 6]`.

result = set(a).intersection(set(b))
print(result)

**Q37.** Write a lambda that takes a string and returns it reversed.

reverse = lambda x: x[::-1]

**Q38.** Write code to sort the list of tuples `[("Alex", 85), ("Bob", 72), ("Cara", 90)]` by the score (second element), highest first.


sorted(list_tuple, key = lambda x: x[1],reverse=True) # attempted 


**Q39.** Write a function `is_prime(n)` that returns `True` if `n` is a prime number.

def is_prime(n):
    prime_flag = True
    if n < 2:
        return False

    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

**Q40.** Write code that uses a `try/except` to safely convert the string `"abc"` to an int, printing `"not a number"` if it fails.

try:
    num = int("abc")
except:
    print("Can not convert text to number, not a number")

---

## 🧑‍🏫 Evaluation by Zoo (Set 2 — RE-GRADED after your revisions)

Legend: ✅ correct · ⚠️ partially correct · ❌ incorrect. Spelling ignored, logic judged.
🔼 = you fixed this since the first grading.

### Section A – True / False
- **Q1** ✅ 🔼 Now **True** — dicts preserve insertion order (3.7+).
- **Q2** ✅ 🔼 Now **False** — `list + tuple` raises `TypeError`.
- **Q3** ✅ Correct. `len()` works on all — dict counts keys.
- **Q4** ✅ 🔼 Now **False** — `not not True` = True, so "evaluates to False" is False.
- **Q5** ✅ Correct. No `return` → `None`.
- **Q6** ✅ Correct. `[::-1]` returns a new list.
- **Q7** ✅ Correct. `"5" + 5` → `TypeError`.
- **Q8** ✅ Correct. Sets are unordered.
- **Q9** ❓ Still unanswered — statement is **False**. `and`/`or` return an **operand**, not a strict bool. Examples: `"" and 5` → `""`; `3 and 5` → `5`; `0 or "hi"` → `"hi"`.
- **Q10** ✅ Correct. `global` rebinds a module-level variable.

**Section A score: 9/10** 🔼 (only Q9 left blank)

### Section B – Predict the Output
- **Q11** ❌ Now `3, 3` — closer, but still wrong. Correct = **`3 1`**. `-7 % 4 = 1` (result takes the **divisor's** sign; `-7 = -2*4 + 1`).
- **Q12** ✅ `bc`.
- **Q13** ✅ `[1, 2, 3] [1, 2, 3, 4]`.
- **Q14** ✅ 🔼 Now `['h', 'i', 1, 2]` — correct.
- **Q15** ✅ 🔼 Now `True, True, False` — correct.
- **Q16** ✅ `{'x': 1, 'y': 5}`.
- **Q17** ✅ `['a', 'b', 'c']` and `a-b-c`.
- **Q18** ✅ 🔼 Now `[1, 9, 4]` — correct slice-assignment result.
- **Q19** ✅ `[3, 2, 1]`.
- **Q20** ✅ `odd`.
- **Q21** ✅ `13`.
- **Q22** ✅ `[0, 3, 6, 9]`.
- **Q23** ✅ `<class 'tuple'> 1`.
- **Q24** ✅ `HELLO hello Hello`.
- **Q25** ✅ `[(0, 'a'), (1, 'b'), (2, 'c')]`.
- **Q26** ✅ `banana`.
- **Q27** ✅ `6 1 3`.
- **Q28** ✅ 🔼 Now `[(1, 'a'), (2, 'b')]` — correct (zip stops at shortest).

**Section B score: 17/18** 🔼 (only Q11 left)

### Section C – Write the Code
- **Q29** ✅ Correct logic (odd cubes 1–10). Typo `rnage` ignored.
- **Q30** ✅ Correct vowel counter.
- **Q31** ✅ 🔼 Now `if min_val > val: min_val = val` — correct smallest-finder.
- **Q32** ✅ Comprehension correct.
- **Q33** ✅ 🔼 Now two steps (`d1.update(d2)` then `d_final = d1`) — correct.
- **Q34** ✅ Correct recursion.
- **Q35** ✅ Correct dict-building loop.
- **Q36** ✅ 🔼 `set(a).intersection(set(b))` → `{3, 4}` (typo fixed too).
- **Q37** ✅ Correct reverse lambda.
- **Q38** ✅ 🔼 Now correct: `sorted(list_tuple, key=lambda x: x[1], reverse=True)`.
- **Q39** ⚠️ 🔼 Base case fixed (`if n < 2: return False`) and `range(2, n//2+1)` is fine. Only remaining issue: the body isn't **indented** under `def is_prime(n):` — as written it's a syntax error. Indent everything:
  ```python
  def is_prime(n):
      if n < 2:
          return False
      for i in range(2, n // 2 + 1):
          if n % i == 0:
              return False
      return True
  ```
- **Q40** ✅ Correct `try/except`.

**Section C score: ~11.5/12** 🔼 (only Q39 half for the indentation.)

---

### 🏁 Set 2 Result (after latest revisions)

| Section | First | Second | **Now** |
|---|---|---|---|
| A – True/False | 6 / 10 | 9 / 10 | **9 / 10** |
| B – Predict Output | 14 / 18 | 17 / 18 | **17 / 18** |
| C – Write Code | 9 / 12 | 10.5 / 12 | **11.5 / 12** 🔼 |
| **Total** | 29 (72.5%) | 36.5 (91%) | **37.5 / 40 ≈ 94%** 🎉 |

**Verdict: Excellent — 72.5% → 91% → 94%!** 👏

**Only 3 tiny things left for a perfect 40:**
1. **Q9** (still blank) — statement is **False**: `and`/`or` return an **operand**, e.g. `3 and 5` → `5`, `0 or "hi"` → `"hi"`.
2. **Q11** — `-7 % 4 = 1`, not 3. Python modulo takes the **divisor's sign**.
3. **Q39** — logic is perfect; just **indent** the body under `def`.
