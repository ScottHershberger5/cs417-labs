

def greet(name: str) -> str:
    return (f"Hello, {name}!")

def square(n: int) -> int:
    return n * n

def is_adult(age: int) -> bool:
    return age >= 18

def log_message(msg: str) -> None:
    print(f"[log] {msg}")

# part 2

def total_grades(grades: list[int]) -> int:
    return sum(grades)

def grade_lookup(roster: dict[str, int], name: str) -> int:
    return roster[name]

def first_and_last(items: list[str]) -> tuple[str, str]:
    return items[0], items[-1]

# part 3

def find_grade(roster: dict[str, int], name: str) -> int | None:
    if name in roster:
        return roster[name]
    return None

roster1 = {"alice": 92, "bob": 85}
grade = find_grade(roster1, "charlie")
if grade is not None:
    print(grade + 10)
else:
    print("no grade on record")

def format_id(value: int | str) -> str:
    return f"id-{value}"

# part 4

from typing import TypedDict

class StudentRow(TypedDict):
    name: str
    email: str
    grade: str

def read_roster(path: str) -> list[StudentRow]:
    # pretend this reads a CSV
    return [{"name": "Alice", "email": "alice@uni.edu", "grade": "92"}]

roster = read_roster("roster.csv")
print(roster[0]["name"])   # typo!