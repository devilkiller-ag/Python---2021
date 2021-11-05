with open('another.txt', 'r') as f:
    a = f.read()
    print(a)
    # DON'T NEED TO CLOSE THE FILE WHEN USING WITH STATEMENT