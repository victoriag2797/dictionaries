def main():
    grades = {"Maya": 100, "JP": 99, "Erica": 98, "Vincent": 80} #defining a list
    fetch_grade(grades)

def fetch_grade(student_grade):
    for grade in student_grade:
        print(f"{grade} has a grade of {student_grade[grade]}")

main()