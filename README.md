# Student Marks Calculator

A simple Python project for first-year CSE students. It accepts marks for five subjects and displays the total, percentage, grade, and pass/fail result.

## Features
- Accepts a student's name
- Takes marks for five subjects
- Checks that each mark is between 0 and 100
- Calculates total and percentage
- Displays a grade and pass/fail result

## Requirements
- Python 3.8 or newer
- No external libraries required

## How to run
1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## Grade rules
| Percentage | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

The project marks a student as PASS only when every subject mark is at least 35.

## Example
```text
Enter student name: Ravi
Enter marks for Mathematics (0-100): 90
...
Total marks: 420 / 500
Percentage : 84.00%
Grade      : A
Result     : PASS
```

## GitHub upload
1. Sign in to GitHub and choose **New repository**.
2. Name it `student-marks-calculator`.
3. Create the repository.
4. Choose **Add file → Upload files**.
5. Extract this ZIP on your computer, then upload the files inside the project folder.
6. Commit the changes.

## Learning concepts
- Variables and data types
- `input()` and `print()`
- Loops and conditionals
- Functions
- Dictionaries
- Input validation
