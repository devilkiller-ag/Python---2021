try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(f'1 / a = {c}')
except Exception as e:
    print(f'Your input resulted in an error {e}')
    exit()
finally:
    print(f'We were done!')

print(f'Thanks for using this code!')