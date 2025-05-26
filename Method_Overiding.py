class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self): # This method overrides the one in Parent
        print("Hello from Child!")

# Create objects
parent_obj = Parent()
child_obj = Child()

parent_obj.greet()
child_obj.greet()  