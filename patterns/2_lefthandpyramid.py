n=7
for i in range(1,n):
    for j in  range(1,n):
        if j>=n-i:
            print("*",end = " ")
        else:
            print(end="  ")
    print()


"""
# // first loop is for printing the rows 
for i in range(rows):

    # // loop for printing leading whitespaces 
    for j in range(2 * (rows - i) - 1): 
        print(end=" ")

    # // loop for printing * character 
    for k in range(i) :
        print("* ",end="")
    print()
"""