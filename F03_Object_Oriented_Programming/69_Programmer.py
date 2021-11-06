class Programmer:
    company = 'Microsoft'
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def getDetails(self):
        print(f'Programmer Name: {self.name}')
        print(f'Programmer Salary: {self.salary}')
        print(f'Programmer Department: {self.department}')

harry = Programmer('Harry', 12000, 'IT')
harry.getDetails()
alka = Programmer('Alka', 12000, 'Marketing')
alka.getDetails()