# student.py
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

def main():
    # example, no input in CI/CD
    name = "Test Student"
    marks = [80, 85, 90]
    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    print(f"{name} Average: {average}, Grade: {grade}")

if __name__ == "__main__":
    main()
