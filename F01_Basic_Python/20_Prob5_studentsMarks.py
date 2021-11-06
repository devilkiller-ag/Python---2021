list = []
print("Life Before Loops!")
marks = int(input("Enter the marks: "))
list.append(marks)
marks = int(input("Enter the marks: "))
list.append(marks)
marks = int(input("Enter the marks: "))
list.append(marks)
marks = int(input("Enter the marks: "))
list.append(marks)
marks = int(input("Enter the marks: "))
list.append(marks)
marks = int(input("Enter the marks: "))
list.append(marks)

list.sort()
print(list)

# print(list[0]+list[1]+list[2]+list[3]+list[4]+list[5])
print("The Sum of Marks is: ",sum(list))

tup = (7, 0, 8, 0, 0, 9)
print(tup.count(0))
