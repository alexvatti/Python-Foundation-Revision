### Python Foundation — Tricky & Difficult — 10 Questions

**Up to OOP concepts, but OOP is NOT included**

1. **List/Tuple**
   Given: `[("Ravi",25),("Anil",22),("Suresh",25),("Arun",22),("Kiran",30)]`
   **Question:** Sort the list by age in ascending order; if age is the same, sort by name. **Expected:** `[("Anil",22),("Arun",22),("Ravi",25),("Suresh",25),("Kiran",30)]`

2. **Dictionary**
   Given: `[{"name":"Ravi","age":25,"marks":85},{"name":"Anil","age":25,"marks":92},{"name":"Arun","age":30,"marks":88},{"name":"Kiran","age":30,"marks":95}]`
   **Question:** Find the highest-scoring student for each age. **Expected:** `{25:"Anil",30:"Kiran"}`

3. **Set**
   Given: `[1,2,3,4,5,6]` and `[4,5,6,7,8]`
   **Question:** Find elements present in exactly one list while preserving original order. **Expected:** `[1,2,3,7,8]`

4. **String**
   Given: `"Swiss"`
   **Question:** Find the first character that occurs exactly once, ignoring case. **Expected:** `"w"`

5. **Recursion**
   Given: `[2,4,6,7,8,10]`
   **Question:** Recursively check whether the list is sorted and return the first breaking index. **Expected:** `False, index 3`

6. **Lambda + Map/Filter/Reduce**
   Given: `[5,12,15,20,7,30]`
   **Question:** Using `filter()` and `reduce()`, calculate the product of all even numbers greater than 10. **Expected:** `7200`

7. **Regular Expression**
   Given: `"Call 9876543210 or 12345 98765432109 and 9123456789"`
   **Question:** Extract only valid 10-digit Indian mobile numbers. **Expected:** `["9876543210","9123456789"]`

8. **Datetime**
   Given joining dates `["2019-05-10","2021-08-15","2020-03-20"]`, as-of date `"2026-09-30"`
   **Question:** Find employees who have completed at least 5 years. **Expected:** `["2019-05-10","2020-03-20"]`

9. **Iterator/Generator**
   Given: `range(1,21)`
   **Question:** Generate numbers divisible by 2 but not by 3, without creating the complete result list. **Expected:** `2,4,8,10,14,16,20`

10. **File Handling**
    Given file content: `"Python is easy. Python is powerful. Python is popular."`
    **Question:** Find the frequency of each word, ignoring case and punctuation. **Expected:** `python:3, is:3, easy:1, powerful:1, popular:1`
