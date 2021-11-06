try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(f'1 / a = {c}')
except ValueError as e:
    print(f'Please Enter a valid value.')
except ZeroDivisionError as e:
    print(f'Please Make sure you are not dividing by zero.')
except Exception as e:
    print(f'Your input resulted in an error {e}')
else:
    print(f'We were Successful')

print(f'Thanks for using this code!')