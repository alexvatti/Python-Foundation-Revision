# python-foundation-test.py
# Sample student data represented in FIVE different ways.
# Columns: name, marks, grade, class, section
# 15 unique records (no duplicates).

from functools import reduce  # reduce() folds a list down to a single value

# ----------------------------------------------------------------------
# 1) LIST OF LISTS
#    The first inner list is the header row (column names).
#    Every other inner list is one student's values in the same order.
# ----------------------------------------------------------------------
students_list_of_lists = [
    ["name", "marks", "grade", "class", "section"],
    ["Aarav Sharma",  88, "A",  10, "A"],
    ["Diya Patel",    92, "A+", 10, "B"],
    ["Vivaan Reddy",  75, "B",  9,  "A"],
    ["Ananya Iyer",   81, "A",  9,  "C"],
    ["Aditya Nair",   67, "C",  8,  "B"],
    ["Ishaan Gupta",  95, "A+", 10, "A"],
    ["Saanvi Rao",    58, "D",  8,  "A"],
    ["Kabir Menon",   73, "B",  9,  "B"],
    ["Myra Joshi",    84, "A",  10, "C"],
    ["Reyansh Verma", 62, "C",  8,  "C"],
    ["Aadhya Singh",  90, "A+", 9,  "A"],
    ["Arjun Kumar",   78, "B",  10, "B"],
    ["Kiara Das",     55, "D",  8,  "B"],
    ["Vihaan Bose",   69, "C",  9,  "C"],
    ["Anika Kapoor",  87, "A",  10, "A"],
]

# ----------------------------------------------------------------------
# 2) DICT (dictionary of dictionaries)
#    The outer key is a unique student id (roll number).
#    The value is a dictionary of that student's details.
# ----------------------------------------------------------------------
students_dict = {
    "S01": {"name": "Aarav Sharma",  "marks": 88, "grade": "A",  "class": 10, "section": "A"},
    "S02": {"name": "Diya Patel",    "marks": 92, "grade": "A+", "class": 10, "section": "B"},
    "S03": {"name": "Vivaan Reddy",  "marks": 75, "grade": "B",  "class": 9,  "section": "A"},
    "S04": {"name": "Ananya Iyer",   "marks": 81, "grade": "A",  "class": 9,  "section": "C"},
    "S05": {"name": "Aditya Nair",   "marks": 67, "grade": "C",  "class": 8,  "section": "B"},
    "S06": {"name": "Ishaan Gupta",  "marks": 95, "grade": "A+", "class": 10, "section": "A"},
    "S07": {"name": "Saanvi Rao",    "marks": 58, "grade": "D",  "class": 8,  "section": "A"},
    "S08": {"name": "Kabir Menon",   "marks": 73, "grade": "B",  "class": 9,  "section": "B"},
    "S09": {"name": "Myra Joshi",    "marks": 84, "grade": "A",  "class": 10, "section": "C"},
    "S10": {"name": "Reyansh Verma", "marks": 62, "grade": "C",  "class": 8,  "section": "C"},
    "S11": {"name": "Aadhya Singh",  "marks": 90, "grade": "A+", "class": 9,  "section": "A"},
    "S12": {"name": "Arjun Kumar",   "marks": 78, "grade": "B",  "class": 10, "section": "B"},
    "S13": {"name": "Kiara Das",     "marks": 55, "grade": "D",  "class": 8,  "section": "B"},
    "S14": {"name": "Vihaan Bose",   "marks": 69, "grade": "C",  "class": 9,  "section": "C"},
    "S15": {"name": "Anika Kapoor",  "marks": 87, "grade": "A",  "class": 10, "section": "A"},
}

# ----------------------------------------------------------------------
# 3) LIST OF DICTS
#    A list where each element is a dictionary (one student record).
# ----------------------------------------------------------------------
students_list_of_dicts = [
    {"name": "Aarav Sharma",  "marks": 88, "grade": "A",  "class": 10, "section": "A"},
    {"name": "Diya Patel",    "marks": 92, "grade": "A+", "class": 10, "section": "B"},
    {"name": "Vivaan Reddy",  "marks": 75, "grade": "B",  "class": 9,  "section": "A"},
    {"name": "Ananya Iyer",   "marks": 81, "grade": "A",  "class": 9,  "section": "C"},
    {"name": "Aditya Nair",   "marks": 67, "grade": "C",  "class": 8,  "section": "B"},
    {"name": "Ishaan Gupta",  "marks": 95, "grade": "A+", "class": 10, "section": "A"},
    {"name": "Saanvi Rao",    "marks": 58, "grade": "D",  "class": 8,  "section": "A"},
    {"name": "Kabir Menon",   "marks": 73, "grade": "B",  "class": 9,  "section": "B"},
    {"name": "Myra Joshi",    "marks": 84, "grade": "A",  "class": 10, "section": "C"},
    {"name": "Reyansh Verma", "marks": 62, "grade": "C",  "class": 8,  "section": "C"},
    {"name": "Aadhya Singh",  "marks": 90, "grade": "A+", "class": 9,  "section": "A"},
    {"name": "Arjun Kumar",   "marks": 78, "grade": "B",  "class": 10, "section": "B"},
    {"name": "Kiara Das",     "marks": 55, "grade": "D",  "class": 8,  "section": "B"},
    {"name": "Vihaan Bose",   "marks": 69, "grade": "C",  "class": 9,  "section": "C"},
    {"name": "Anika Kapoor",  "marks": 87, "grade": "A",  "class": 10, "section": "A"},
]


# ----------------------------------------------------------------------
# 4) DICT OF LISTS (column oriented)
#    Each key is a column name and its value is a list of that column's
#    values. Position i across all lists belongs to the same student.
# ----------------------------------------------------------------------
students_dict_of_lists = {
    "name": [
        "Aarav Sharma", "Diya Patel", "Vivaan Reddy", "Ananya Iyer", "Aditya Nair",
        "Ishaan Gupta", "Saanvi Rao", "Kabir Menon", "Myra Joshi", "Reyansh Verma",
        "Aadhya Singh", "Arjun Kumar", "Kiara Das", "Vihaan Bose", "Anika Kapoor",
    ],
    "marks": [88, 92, 75, 81, 67, 95, 58, 73, 84, 62, 90, 78, 55, 69, 87],
    "grade": ["A", "A+", "B", "A", "C", "A+", "D", "B", "A", "C", "A+", "B", "D", "C", "A"],
    "class": [10, 10, 9, 9, 8, 10, 8, 9, 10, 8, 9, 10, 8, 9, 10],
    "section": ["A", "B", "A", "C", "B", "A", "A", "B", "C", "C", "A", "B", "B", "C", "A"],
}


# ----------------------------------------------------------------------
# 5) LIST OF TUPLES
#    Like a list of lists, but each row is a TUPLE, so the row is
#    immutable (its values cannot be changed after creation).
# ----------------------------------------------------------------------
students_list_of_tuples = [
    ("Aarav Sharma",  88, "A",  10, "A"),
    ("Diya Patel",    92, "A+", 10, "B"),
    ("Vivaan Reddy",  75, "B",  9,  "A"),
    ("Ananya Iyer",   81, "A",  9,  "C"),
    ("Aditya Nair",   67, "C",  8,  "B"),
    ("Ishaan Gupta",  95, "A+", 10, "A"),
    ("Saanvi Rao",    58, "D",  8,  "A"),
    ("Kabir Menon",   73, "B",  9,  "B"),
    ("Myra Joshi",    84, "A",  10, "C"),
    ("Reyansh Verma", 62, "C",  8,  "C"),
    ("Aadhya Singh",  90, "A+", 9,  "A"),
    ("Arjun Kumar",   78, "B",  10, "B"),
    ("Kiara Das",     55, "D",  8,  "B"),
    ("Vihaan Bose",   69, "C",  9,  "C"),
    ("Anika Kapoor",  87, "A",  10, "A"),
]


# ----------------------------------------------------------------------
# Helper printing functions
# ----------------------------------------------------------------------
def print_row(values):
    """Print one row of five values in aligned columns."""
    name, marks, grade, cls, section = values
    print(f"{str(name):<15} {str(marks):>6} {str(grade):>6} {str(cls):>6} {str(section):>8}")


def print_header_line():
    header = ["name", "marks", "grade", "class", "section"]
    print_row(header)
    print("-" * 45)


def print_list_of_lists(data):
    print("\n===== 1) LIST OF LISTS =====")
    # data[0] is the header row, data[1:] are the students
    print_row(data[0])
    print("-" * 45)
    for row in data[1:]:
        print_row(row)


def print_dict(data):
    print("\n===== 2) DICT (id -> details) =====")
    print(f"{'ID':<5} {'Name':<15} {'Marks':>6} {'Grade':>6} {'Class':>6} {'Section':>8}")
    print("-" * 51)
    for student_id, info in data.items():
        print(
            f"{student_id:<5} "
            f"{info['name']:<15} "
            f"{info['marks']:>6} "
            f"{info['grade']:>6} "
            f"{info['class']:>6} "
            f"{info['section']:>8}"
        )


def print_list_of_dicts(data):
    print("\n===== 3) LIST OF DICTS =====")
    print_header_line()
    for info in data:
        print_row([info["name"], info["marks"], info["grade"], info["class"], info["section"]])


def print_list_of_tuples(data):
    print("\n===== 5) LIST OF TUPLES =====")
    print_header_line()
    for row in data:
        # a tuple can be passed straight to print_row (it unpacks fine)
        print_row(row)


def print_dict_of_lists(data):
    print("\n===== 4) DICT OF LISTS (column oriented) =====")
    print_header_line()
    # All columns have the same length; loop by index.
    total = len(data["name"])
    for i in range(total):
        print_row([
            data["name"][i],
            data["marks"][i],
            data["grade"][i],
            data["class"][i],
            data["section"][i],
        ])


# ----------------------------------------------------------------------
# FILTER: select only students whose grade is "A" or "A+"
# A comprehension is used for EACH of the four representations.
# ----------------------------------------------------------------------
TOP_GRADES = ("A", "A+")


def filter_list_of_lists(data):
    print("\n----- FILTER (A / A+) on LIST OF LISTS -----")
    header = data[0]
    # grade is at index 2 in each row.
    # filter() + lambda keeps only rows whose grade is a top grade.
    filtered = list(filter(lambda row: row[2] in TOP_GRADES, data[1:]))
    print_row(header)
    print("-" * 45)
    for row in filtered:
        print_row(row)
    print(f"Matched: {len(filtered)}")


def filter_dict(data):
    print("\n----- FILTER (A / A+) on DICT -----")
    # filter() runs over (sid, info) items; lambda checks the grade.
    filtered = dict(filter(lambda item: item[1]["grade"] in TOP_GRADES, data.items()))
    print_header_line()
    for sid, info in filtered.items():
        print_row([info["name"], info["marks"], info["grade"], info["class"], info["section"]])
    print(f"Matched: {len(filtered)}")


def filter_list_of_dicts(data):
    print("\n----- FILTER (A / A+) on LIST OF DICTS -----")
    # filter() + lambda over the records
    filtered = list(filter(lambda info: info["grade"] in TOP_GRADES, data))
    print_header_line()
    for info in filtered:
        print_row([info["name"], info["marks"], info["grade"], info["class"], info["section"]])
    print(f"Matched: {len(filtered)}")


def filter_dict_of_lists(data):
    print("\n----- FILTER (A / A+) on DICT OF LISTS -----")
    # filter() + lambda to find the indexes whose grade is a top grade,
    # then rebuild each column using those indexes.
    keep = list(filter(lambda i: data["grade"][i] in TOP_GRADES, range(len(data["grade"]))))
    filtered = {col: [values[i] for i in keep] for col, values in data.items()}
    print_header_line()
    for i in range(len(filtered["name"])):
        print_row([
            filtered["name"][i],
            filtered["marks"][i],
            filtered["grade"][i],
            filtered["class"][i],
            filtered["section"][i],
        ])
    print(f"Matched: {len(filtered['name'])}")


def filter_list_of_tuples(data):
    print("\n----- FILTER (A / A+) on LIST OF TUPLES -----")
    # grade is at index 2 in each tuple.
    # filter() + lambda keeps only tuples whose grade is a top grade.
    filtered = list(filter(lambda row: row[2] in TOP_GRADES, data))
    print_header_line()
    for row in filtered:
        print_row(row)
    print(f"Matched: {len(filtered)}")


# ----------------------------------------------------------------------
# REDUCE: total marks and average marks using functools.reduce + lambda
# The reduce() call is the SAME everywhere; only the way we pull out the
# marks list changes for each of the five representations.
# ----------------------------------------------------------------------
def _sum_average(label, marks):
    """Shared helper: fold marks to a total with reduce+lambda, then average."""
    # reduce() folds the marks list into one running total.
    # lambda takes the accumulator 'acc' and the next value 'm'.
    total = reduce(lambda acc, m: acc + m, marks, 0)
    average = total / len(marks)
    print(f"\n----- REDUCE on {label} -----")
    print(f"Number of students : {len(marks)}")
    print(f"Sum of marks       : {total}")
    print(f"Average of marks   : {average:.2f}")
    return total, average


def reduce_list_of_lists(data):
    # skip header row (data[0]); marks are at index 1
    marks = [row[1] for row in data[1:]]
    return _sum_average("LIST OF LISTS", marks)


def reduce_dict(data):
    # values are detail dicts; grab each "marks"
    marks = [info["marks"] for info in data.values()]
    return _sum_average("DICT", marks)


def reduce_list_of_dicts(data):
    marks = [info["marks"] for info in data]
    return _sum_average("LIST OF DICTS", marks)


def reduce_dict_of_lists(data):
    # marks column is already a ready-made list
    marks = data["marks"]
    return _sum_average("DICT OF LISTS", marks)


def reduce_list_of_tuples(data):
    # marks are at index 1 in each tuple
    marks = [row[1] for row in data]
    return _sum_average("LIST OF TUPLES", marks)


# ----------------------------------------------------------------------
# MAP: add a 1% correction to each mark using map() + lambda.
# Rule: if a mark is already >= 100, leave it unchanged; otherwise
# multiply by 1.01 (add 1%) and round to a whole number.
#
# MARKS IS A SINGLE COLUMN, so for every representation we:
#   1) pull out just the marks (one list),
#   2) apply map() + lambda on that single column,
#   3) show old mark -> new mark next to each name.
# ----------------------------------------------------------------------
# One shared correction rule reused by every representation:
correct_mark = lambda m: m if m >= 100 else round(m * 1.01)


def _show_correction(label, names, marks):
    """Apply map()+lambda to the single marks column and print old -> new."""
    corrected = list(map(correct_mark, marks))  # map over ONE column
    print(f"\n----- MAP (+1% marks) on {label} -----")
    print(f"{'Name':<15} {'Old':>5} {'New':>5}")
    print("-" * 27)
    for name, old, new in zip(names, marks, corrected):
        print(f"{name:<15} {old:>5} {new:>5}")
    return corrected


def map_list_of_lists(data):
    # skip header; name at index 0, marks at index 1
    names = [row[0] for row in data[1:]]
    marks = [row[1] for row in data[1:]]
    return _show_correction("LIST OF LISTS", names, marks)


def map_dict(data):
    names = [info["name"] for info in data.values()]
    marks = [info["marks"] for info in data.values()]
    return _show_correction("DICT", names, marks)


def map_list_of_dicts(data):
    names = [info["name"] for info in data]
    marks = [info["marks"] for info in data]
    return _show_correction("LIST OF DICTS", names, marks)


def map_dict_of_lists(data):
    # marks is already a single ready-made column
    return _show_correction("DICT OF LISTS", data["name"], data["marks"])


def map_list_of_tuples(data):
    names = [row[0] for row in data]
    marks = [row[1] for row in data]
    return _show_correction("LIST OF TUPLES", names, marks)


if __name__ == "__main__":
    print_list_of_lists(students_list_of_lists)
    print_dict(students_dict)
    print_list_of_dicts(students_list_of_dicts)
    print_dict_of_lists(students_dict_of_lists)
    print_list_of_tuples(students_list_of_tuples)

    print("\nTotal students in each representation:")
    print(f"  list of lists  : {len(students_list_of_lists) - 1}")  # minus header
    print(f"  dict           : {len(students_dict)}")
    print(f"  list of dicts  : {len(students_list_of_dicts)}")
    print(f"  dict of lists  : {len(students_dict_of_lists['name'])}")
    print(f"  list of tuples : {len(students_list_of_tuples)}")

    print("\n\n########## FILTERED VIEWS (grade A or A+) ##########")
    filter_list_of_lists(students_list_of_lists)
    filter_dict(students_dict)
    filter_list_of_dicts(students_list_of_dicts)
    filter_dict_of_lists(students_dict_of_lists)
    filter_list_of_tuples(students_list_of_tuples)

    print("\n\n########## AGGREGATE: SUM & AVERAGE of MARKS (reduce + lambda) ##########")
    reduce_list_of_lists(students_list_of_lists)
    reduce_dict(students_dict)
    reduce_list_of_dicts(students_list_of_dicts)
    reduce_dict_of_lists(students_dict_of_lists)
    reduce_list_of_tuples(students_list_of_tuples)

    print("\n\n########## CORRECTION: +1% MARKS, capped at 100 (map + lambda) ##########")
    map_list_of_lists(students_list_of_lists)
    map_dict(students_dict)
    map_list_of_dicts(students_list_of_dicts)
    map_dict_of_lists(students_dict_of_lists)
    map_list_of_tuples(students_list_of_tuples)

    print("\n\n########## AGGREGATE: SUM & AVERAGE of MARKS (reduce + lambda) ##########")
    reduce_list_of_lists(students_list_of_lists)
    reduce_dict(students_dict)
    reduce_list_of_dicts(students_list_of_dicts)
    reduce_dict_of_lists(students_dict_of_lists)
    reduce_list_of_tuples(students_list_of_tuples)
