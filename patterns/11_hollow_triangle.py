# n=7
# for i in range(n):
#     for j in  range(n):
#         if j>=n-i:
#             print("*",end = " ")
#         else:
#             print(end="")
#     print()
    
rows = 5

# // first outer loop to iterate through each loop 
for i in range(rows): 

    # // first inner loop to print leading whitespaces 
    for j in range(2 * (rows - i) - 1):
        print(end=" ")

    # // second inner loop to print stars * and inner whitespaces 
    for k in range(2 * i + 1): 
        if (k == 0 or k == 2 * i or i == rows - 1):
            print("* ",end="")
        else :
            print(end="  ")
    print() 
