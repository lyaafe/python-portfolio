
import csv


class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority


class To_do_list:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No task found!")
        else:
            for index, task in enumerate(self.tasks):
                print(index, "-", task.title, task.description, task.priority)

    def remove_task(self, index):
        try:
            self.tasks.pop(index)
            print("Task removed successfully!")

        except IndexError:
            print("Invalid task number!")

    def save_tasks(self):
        try:
            with open("tasks.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)

                for task in self.tasks:
                    writer.writerow([
                        task.title,
                        task.description,
                        task.priority
                    ])

        except OSError:
            print("Error: Could not save tasks!")

    def load_tasks(self):
        try:
            with open("tasks.csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                for row in reader:
                    try:
                        title, description, priority = row
                        task = Task(title, description, priority)
                        self.tasks.append(task)

                    except ValueError:
                        print("Warning: Invalid row found in CSV file!")

        except FileNotFoundError:
            pass

        except OSError:
            print("Error: Could not read tasks file!")


todo = To_do_list()
todo.load_tasks()

while True:
    choice = input(
        "\n1: Add Task\n"
        "2: Show Tasks\n"
        "3: Remove Task\n"
        "4: Exit\n"
        "Choose: "
    )

    if choice == "4":
        todo.save_tasks()
        break

    elif choice == "1":
        title = input("Title: ")
        description = input("Description: ")
        priority = input("Priority: ")

        task = Task(title, description, priority)
        todo.add_task(task)

    elif choice == "2":
        todo.show_tasks()

    elif choice == "3":
        try:
            index = int(input("Task number: "))
            todo.remove_task(index)

        except ValueError:
            print("Please enter a valid number!")

    else:
        print("Invalid choice!")

