class Person:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # marks is a list of 3 subject marks

    def greet(self):
        print(f"Hi {self.name}!")

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average()}")
        print("-" * 30)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


if __name__ == "__main__":
    # Create list of students with (name, roll number, [marks])
    students = [
        Person("Kumar", 101, [85, 90, 88]),
        Person("Jaya", 102, [78, 82, 80]),
        Person("Kala", 103, [92, 89, 95])
    ]

    # Display details of all students
    for student in students:
        student.display_details()