num1 = int("Enter Number 1: ")
num2 = int("Enter Number 2: ")
num3 = int("Enter Number 3: ")
num4 = int("Enter Number 4: ")

if(num1 > num2):
    f1 = num1
else:
    f1 = num2

if(num3 > num4):
    f2 = num3
else:
    f2 = num4

if(f1 > f2):
    print(str(f1) + " is greatest.")
else:
    print(str(f2) + " is greatest.")