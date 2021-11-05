'''
Procedural Oriented Programming: 
a = 12
b = 34
print("The sum of a and b is ", a + b)
'''

class NumberOP:
    def sum(self):
        return self.a + self.b

num = NumberOP()
num.a = 12
num.b = 34
s = num.sum()
print(s)

'''
PascalCase ----> EmployeName
camelCase ----> isFloatOrInt
'''