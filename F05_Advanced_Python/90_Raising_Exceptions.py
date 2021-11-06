def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harry")

a = increment('dsdsd')
print(a)
b = increment(23)
print(b)