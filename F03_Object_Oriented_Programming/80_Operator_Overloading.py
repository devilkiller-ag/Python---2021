class Number:
    def __init__(self, num):
        self.num = num;
    
    def __add__(self, num2):
        print("Adding...")
        return self.num + num2.num
    
    def __mul__(self, num2):
        print("Multiplying...")
        return self.num * num2.num

n1 = Number(4)
n2 = Number(6)

sum = n1 + n2
print('Result: ',sum)

mul = n1 * n2
print('Result: ',mul)