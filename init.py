class Employee:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(self.name)


employee = Employee("Annie")
employeeOne = Employee("Anjali")
employee.display_name()
employeeOne.display_name()
