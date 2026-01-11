# student.py
import sys

def main():
    if len(sys.argv) == 7:  # name dept sem m1 m2 m3
        name, department, semester = sys.argv[1:4]
        m1, m2, m3 = map(float, sys.argv[4:7])
    else:
        # fallback for local use
        name = "Default Name"
        department = "CSE"
        semester = "5"
        m1, m2, m3 = 70, 80, 90

    average = (m1 + m2 + m3) / 3
    grade = calculate_grade(average)
    print(f"Average: {average}, Grade: {grade}")

if __name__ == "__main__":
    main()


