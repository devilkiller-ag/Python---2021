class Vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__(self):
        str = ''
        index = 0

        # Method 1
        # for i in range(len(self.vec)):
        #     if (i != len(self.vec) - 1):
        #         str += f'{self.vec[i]} a{index + 1} + '
        #     else:
        #         str += f'{self.vec[i]} a{index + 1}'
        #     index += 1
        # return str

        # Method 2
        for i in self.vec:
            str += f'{i} a{index + 1} + '
            index += 1
        return str[:-2]
    
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] * vec2.vec[i])
        return sum(newList)

    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6])
print('v1 = ', v1)      
v2 = Vector([1, 6, 9])
print('v2 = ', v2)
print('v1 + v2 = ', v1 + v2)
print('v1 . v2 = ', v1 * v2)
print(len(v1))
print(len(v2))