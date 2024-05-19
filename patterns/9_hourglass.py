n=7

for i in range(n-1):
    for j in range(n):
        if j>i:
            print("*",end=" ")
        else:
            print(end=" ")
    print()

for i in range(2,n):
    for j in  range(n):
        if j>=n-i:
            print("*",end = " ")
        else:
            print(end=" ")
    print()
