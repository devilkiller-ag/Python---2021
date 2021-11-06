class Employee:
    company = 'Google'

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is Created!")

    def getDetails(self):
        print(f"The name of the employee working in {self.name}")
        print(f"The salary of the employee working in {self.salary}")
        print(f"The subunit of the employee working in {self.subunit}")

    def getSalary(self, signature):
        print(f"Salary of {self.name} working in {self.company} is {self.salary}.\n{signature}")
     
    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee("Harry", 6000, 'Printers')
# harry.salary = 10101010
# harry.getSalary('Thanks') # Employee.getSalary(harry)

harry.getDetails()

harry.greet() # Employee,greet()