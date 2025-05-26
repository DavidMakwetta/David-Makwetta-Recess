class Person:
    #Parent class for all people in the university
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    #Subclass for students.
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age) 
        self.student_id = student_id
        self.major = major

    def display_info(self):
        super().display_info() 
        print(f"  Type: Student, ID: {self.student_id}, Major: {self.major}")

class Lecturer(Person):
    #Subclass for lecturers.
    def __init__(self, name, age, staff_id, department):
        super().__init__(name, age) 
        self.staff_id = staff_id
        self.department = department

    def display_info(self):
        super().display_info() 
        print(f"  Type: Lecturer, ID: {self.staff_id}, Dept: {self.department}")

class Staff(Person):
    def __init__(self, name, age, staff_id, role):
        super().__init__(name, age) 
        self.staff_id = staff_id
        self.role = role

    def display_info(self):
        super().display_info() 
        print(f"  Type: Staff, ID: {self.staff_id}, Role: {self.role}")

print("--- University Members Info ---")

# Create one object of each type
p1 = Person("Generic Guy", 30)
s1 = Student("Alice", 20, "S001", "CS")
l1 = Lecturer("Dr. Smith", 45, "L001", "Physics")

p1.display_info()
s1.display_info()
l1.display_info()
