list = [32, 45, 12, 54, 23, 56, 21, 65 ,32, 12, 39, 41, 24, 23, 57]

for index, item in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        print(f'The value at {index + 1} is {item}')