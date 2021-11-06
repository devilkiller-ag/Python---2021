num = int(input('Enter a number: '))
table= [num*i for i in range(1, 11)]
print(str(table))

with open('F05_Advanced_Python\\tables.txt', 'a') as f:
    f.write(str(table))
    f.write('\n')