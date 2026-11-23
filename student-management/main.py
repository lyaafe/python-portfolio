import json
from pathlib import Path


class Student:
    def __init__(self, name, math, python):
        self.name = name
        self.math = math
        self.python = python

    def average(self):
        return (self.math + self.python) / 2

    def show_info(self):
        print(f"\nName: {self.name}")
        print(f"Math: {self.math}")
        print(f"Python: {self.python}")
        print(f"Average: {self.average():.2f}")

    def to_dict(self):
        return {
            "name": self.name,
            "math": self.math,
            "python": self.python
        }


class StudentManager:
    FILE_PATH = Path("students.json")

    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if not self.FILE_PATH.exists():
            return

        try:
            with self.FILE_PATH.open("r", encoding="utf-8") as file:
                data = json.load(file)

            self.students = [
                Student(item["name"], item["math"], item["python"])
                for item in data
            ]

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Could not load saved data.")

    def save_data(self):
        data = [student.to_dict() for student in self.students]

        with self.FILE_PATH.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def get_score(subject):
        while True:
            try:
                score = float(input(f"Enter {subject} score (0-20): "))

                if 0 <= score <= 20:
                    return score

                print("Score must be between 0 and 20.")

            except ValueError:
                print("Please enter a valid number.")

    def add_student(self):
        name = input("Enter student name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        if self.find_student(name):
            print("Student already exists.")
            return

        math = self.get_score("Math")
        python = self.get_score("Python")

        self.students.append(Student(name, math, python))
        self.save_data()

        print("Student added successfully!")

    def show_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.show_info()
            print("-" * 30)

    def find_student(self, name):
        for student in self.students:
            if student.name.casefold() == name.casefold():
                return student

        return None

    def search_student(self):
        name = input("Enter student name: ").strip()
        student = self.find_student(name)

        if student:
            student.show_info()
        else:
            print("Student not found.")

    def show_average(self):
        name = input("Enter student name: ").strip()
        student = self.find_student(name)

        if student:
            print(f"Average: {student.average():.2f}")
        else:
            print("Student not found.")

    def update_student(self):
        name = input("Enter student name: ").strip()
        student = self.find_student(name)

        if not student:
            print("Student not found.")
            return

        print("Enter new scores:")
        student.math = self.get_score("Math")
        student.python = self.get_score("Python")

        self.save_data()
        print("Student updated successfully!")

    def delete_student(self):
        name = input("Enter student name: ").strip()
        student = self.find_student(name)

        if not student:
            print("Student not found.")
            return

        self.students.remove(student)
        self.save_data()

        print("Student deleted successfully!")


def menu():
    manager = StudentManager()

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Show Student Average")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Exit")
        print("=" * 48)

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.show_average()

        elif choice == "5":
            manager.update_student()

        elif choice == "6":
            manager.delete_student()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
