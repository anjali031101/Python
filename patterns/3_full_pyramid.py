n=7
for i in range(1,n):
    for j in  range(1,n):
        if j>=n-i:
            print("*",end = " ")
        else:
            print(end=" ")
    print()
