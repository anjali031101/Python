for i in range(10):
    print(i)
    for j in range(10,i,-1):
        if j>=i:
            print(j,end=" ")
    print()