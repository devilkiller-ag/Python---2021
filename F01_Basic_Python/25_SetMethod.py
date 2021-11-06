b = numSet()
print(type(b))
print(b)

# Adding elements to numSet b
b.add(4)
b.add(56)
b.add(56)
b.add(56)
b.add(6)
b.add(5)
print(b)

# b.add([3, 4, 3, 5]) # Error as list is an mutable data structure
# b.add({4:5, 'ashmit':'gupta'}) # Cannot add dicitionary to numSets
b.add((1, 3, 2, 4, 2, 4, 5, 24))  # tuple is an immutable data structure
print(b)
print(len(b))

b.remove(6)  # Remove 5 from numSets
# throws an error while trying to remove 15(which is not present in the numSet)
# b.remove(15)
print(b)

print(b.pop())
print(b)
