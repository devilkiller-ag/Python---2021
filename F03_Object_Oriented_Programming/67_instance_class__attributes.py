class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# creating intance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400

print(harry.company)
print(rajni.company)

Employee.company = "Youtube"

print(harry.company)
print(rajni.company)

harry.salary = 35
print(harry.salary) 
print(rajni.salary)
# print(rajni.address) # Throws an error as addressis not present in instance/class