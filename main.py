"""
Student Marks Calculator
Beginner-friendly Python project for first-year CSE students.
"""

def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("=" * 36)
    print("       STUDENT MARKS CALCULATOR")
    print("=" * 36)

    name = input("Enter student name: ").strip()
    if not name:
        name = "Student"

    subjects = ["Mathematics", "Physics", "Chemistry", "Programming", "English"]
    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    total = sum(marks.values())
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)
    result = "PASS" if all(mark >= 35 for mark in marks.values()) else "FAIL"

    print("\n" + "=" * 36)
    print("             MARKS REPORT")
    print("=" * 36)
    print(f"Student name: {name}")
    for subject, mark in marks.items():
        print(f"{subject:<18}: {mark:g}")
    print("-" * 36)
    print(f"Total marks: {total:g} / {len(subjects) * 100}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")
    print(f"Result     : {result}")
    print("=" * 36)


if __name__ == "__main__":
    main()
