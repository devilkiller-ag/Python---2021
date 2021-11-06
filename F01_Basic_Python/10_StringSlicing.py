# greeting = 'Good Morning '
# name = "Harry"

# print(type(name))

# print(greeting + name)  # Concatenation
# text = greeting + name
# print(text)

name = "Harry"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5]) # Error - Index Out Of Range

# name[2] = "d" # Error - Invalid

# string[including:excluding]
# print(name[0:3])  # 0, 1, 2
# print(name[1:4])  # 1, 2, 3
# print(name[0:5])  # 0, 1, 2, 3, 4
# print(name[:4])  # 0, 1, 2, 3 = name[0:3]
# print(name[1:])  # 1, 2, 3, 4 = name[1:5]

# Negative Indexing
# print(name[-4:-1])  # 1, 2, 3 = name[1:4]

# slicing with skip value
str = "ashit is a goood buy. [;)]"
print(str[1:4:1])  # 1, 2, 3
print(str[1:8:2])  # 1, 3, 5, 7
print(str[1::2])  # 1, 3, 5, 7, 9, 11, 12, 13, 15, 17, 19, 21, 23, 25
