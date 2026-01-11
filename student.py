# student.py
import sys

def main():
    if len(sys.argv) == 7:  # args: name dept sem m1 m2 m3
        name, department, semester = sys.argv[1:4]
        m1, m2, m3 = map(float, sys.argv[4:7])
    else:
        # fallback to interactive input
        name = input("Enter student name: ")
        department = input("Enter department: ")
        semester = input("Enter semester: ")
        print("Enter marks for 3 subjects:")
        m1 = float(input("Subject 1: "))
        m2 = float(input("Subject 2: "))
        m3 = float(input("Subject 3: "))
    
    average = (m1 + m2 + m3) / 3
    grade = calculate_grade(average)
    print(f"Name: {name}, Dept: {department}, Semester: {semester}, Average: {average}, Grade: {grade}")

if __name__ == "__main__":
    main()
