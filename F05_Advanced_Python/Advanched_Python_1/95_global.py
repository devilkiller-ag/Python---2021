a = 54 # Global variable

def func():
    a = 8 # Local Variable (if global keyword is not used)
    print(f'Print Statement 1: {a}')

def func1():
    global a
    print(f'Print Statement 2: {a}')
    a = 18 # global variable is changed (Local Variable if global keyword is not used)
    print(f'Print Statement 3: {a}')



func()
func1()

print(f'Print Statement 4: {a}')