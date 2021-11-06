class Employee:
    company = "Google"
    salary = 100

harry = Employee()
harry.salary = 300

rajni = Employee()
rajni.salary = 400

print(harry.company)
print(rajni.company)

Employee.company = "Youtube"

print(harry.company)
print(rajni.company)

print(harry.salary)
print(rajni.salary)