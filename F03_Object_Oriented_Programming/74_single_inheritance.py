# Single Inheritance
class Employee:
    company = 'Google'

    def showDetail(self):
        print("This is an employee")

class Programmer(Employee):
    lang = 'python'
    # company = 'youtube'
    def getlang(self):
        print(f'The language is {self.lang}')

    def showDetail(self):
        print("This is a programmer")

e = Employee()
e.showDetail()
p = Programmer()
p.showDetail()
print(p.company)