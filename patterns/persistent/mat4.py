mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(mat)):
    for j in range(len(mat)):
        if i+j < len(mat)-1:
            print( mat[i][j],end = " ")
    print()   
    