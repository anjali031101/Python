mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=len(mat)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j],end= "   ")
    print()
    
print("\nnext : (\ Diagonal)")
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i==j:
            print(mat[i][j],end= " ")
        else:
            print(end=" ")
    print()

print("\nnext : (/ Diagonal)")    
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if i+j==len(mat)-1:
            print(mat[i][j],end= " ")
        else:
            print(end=" ")
    print()

print("\nnext : (\/ both Diagonal)")
for i in range(n):
    for j in range(n):
        if j==i or i+j == n-1:
                print(mat[i][j],end="  ")

        else:
            print(end="   ")
    print()
    
print("\nnext : (below \ Diagonal)")
for i in range(len(mat)):
    for j in range(len(mat)):
        if j<i:
            print( mat[i][j],end = " ")
    print()      

print("\nnext: (above \ Diagonal)")
for i in range(len(mat)):
    for j in range(len(mat)):
        if j>i:
            print( mat[i][j],end = " ")
        else:
            print(end = "  ")
    print()   
    
print("\nnext : (above /  Diagonal)")
for i in range(len(mat)):
    for j in range(len(mat)):
        if i+j < len(mat)-1:
            print( mat[i][j],end = " ")
    print()   

print("\nnext : (below / Diagonal)")  
for i in range(len(mat)):
    for j in range(len(mat)):
        if i+j > len(mat)-1:
            print( mat[i][j],end = " ")
        else:
            print(end="   ")
    print()  

print("\nnext : (below \/ Diagonal)")
for i in range(n):
    for j in range(n):
        if j<i:
            if i+j > n-1:
                print(mat[i][j],end=" ")
            else:
                print(end="  ")
        else:
            print(end=" ")
    print()

print("\nnext : (below \ Diagonal and above /)")
for i in range(n):
    for j in range(n):
        if j<i:
            if i+j < n-1:
                print(mat[i][j],end=" ")
            else:
                print(end="  ")
        else:
            print(end=" ")
    print()

print("\nnext: (above \/ Diagonal)")
for i in range(n):
    for j in range(n):
        if j>i:
            if i+j < n-1:
                print(mat[i][j],end=" ")
            else:
                print(end="  ")
        else:
            print(end=" ")
    print()

print("\nnext : (above \ Diagonal below / )")
for i in range(n):
    for j in range(n):
        if j>i:
            if i+j > n-1:
                print(mat[i][j],end=" ")
            else:
                print(end="  ")
        else:
            print(end=" ")
    print()
    
print("\nnext : (all / Diagonal)")
dic= {}
for i in range(n):
    for j in range(n):
        if i+j not in dic:
            dic[i+j] = []
            dic[i+j].append(mat[i][j])
        else:
            dic[i+j].append(mat[i][j])
res = []

key = list(dic.keys())
key.sort()
for i in key:
    res.extend(reversed(dic[i]))

print(res)

matrix = mat
print("\nnext : transpose")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if j>i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end= "   ")
    print()
    
print()