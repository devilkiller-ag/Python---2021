n = 6


def fact_itter(n):
    pro = 1
    for i in range(n):
        pro = pro * (i+1)
    return pro

print(fact_itter(n))

def fact_recur(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact_itter(n-1)

print(fact_recur(n))