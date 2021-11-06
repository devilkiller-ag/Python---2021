n = row = 5

for i in range (row):
    for j in range (row):
        if(i==0 or j==0 or i == n-1 or j == n-1):
            print(' # ', end='')
        else:
            print("   ",  end='')
        if(j==n-1):
            print('\n')