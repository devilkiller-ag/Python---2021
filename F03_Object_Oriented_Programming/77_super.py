class Person:
    country = 'India'

    def __init__(self):
        print('Inititalizing Person....')

    def takeBreath(self):
        print('I am breathing...')

class Employee(Person):
    company = 'Honda'

    def __init__(self):
        super().__init__()
        print('Inititalizing Employee....')

    def getSalary(self):
        print(f'Salary is {self.salary}')

    def takeBreath(self):
        # super().takeBreath()
        print('I am an Employee so I am luckily breathing....')

class Programmer(Employee):
    company = 'Fiverr'

    def __init__(self):
        # super().__init__()
        print('Inititalizing Programmer....')

    @staticmethod
    def getSalary():
        print(f'No salary to programmer')
    
    def takeBreath(self):
        super().takeBreath()
        print('I am an Programmer so I am breathing++....')

p = Person()
p.takeBreath()
# print(p.company) # throws an error
e = Employee()
e.takeBreath()
print(e.company)
print(e.country)
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)