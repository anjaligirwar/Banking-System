class Employee:
    def employee_details(self):
        self.name = "Anjali"
        self.age = 22

    def print_employee_details(self):
        print("printing in another method")
        print(self.name)
        print(self.age)

    @staticmethod
    def welcome_message():
        print("welcome to explore oops deeply")


employee = Employee()
employee.employee_details()
print(employee.name)
employee.print_employee_details()
employee.welcome_message()
