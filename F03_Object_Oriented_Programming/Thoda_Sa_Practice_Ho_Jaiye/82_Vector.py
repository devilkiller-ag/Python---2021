class C2dVector:
    icap = 0
    jcap = 0

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
    

class C3dVector(C2dVector):
    kcap = 0

    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVector(10, 5)
v3d = C3dVector(12, 34, 56)
print(v2d)
print(v3d)