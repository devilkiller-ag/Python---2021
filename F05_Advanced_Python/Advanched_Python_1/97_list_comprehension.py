a = [3, 6, 7, 8, 9, 2, 34, 455 , 76756 ,23,4 ,46, 43, 4, 25, 36, 4498]

# Majdoori for even number extraction
# b = []
# for item in a:
#     if(item % 2 == 0):
#         b.append(item)
# print(b)

# Chalaki
b = [i for i in a if i%2 == 0]
print(b)

# list - set - dictionary comprehension

t = [1, 4, 2, 4, 1, 2, 3]
s = {i for i in t}
print(s)