printch = "*"

row = 3
n = 3
for i in range(row):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (2*i+1))
