# student.py
import sys

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg < 90:
        return "A"
    elif 65 <= avg < 80:
        return "B"
    elif 50 <= avg < 65:
        return "C"
    elif 40 <= avg < 50:
        return "D"
    else:
        return "F"

def main():
    if len(sys.argv) == 7:  # name dept sem m1 m2 m3
        name, department, semester = sys.argv[1:4]
        m1, m2, m3 = map(float, sys.argv[4:7])
    else:
        # fallback for local interactive use
        name = input("Enter student name: ")
        department = input("Enter department: ")
        semester = input("Enter semester: ")
        print("Enter marks for 3 subjects:")
        m1 = float(input("Subject 1: "))
        m2 = float(input("Subject 2: "))
        m3 = float(input("Subject 3: "))

    average = (m1 + m2 + m3) / 3
    grade = calculate_grade(average)

    print("\n---- Result ----")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Average    : {average:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()
