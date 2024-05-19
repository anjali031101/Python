rows = 7
  
# // outer loop for rows 
for i in range(rows+1):

    # // inner loop 1 for leading white spaces 
    for j in range(rows-i):
        print(end=" ") 
        
    #coefficient
    C = 1 

    # // inner loop 2 for printing numbers 
    for k in range(1,i+1):
        print(C,end=" "); 
        C = C * (i - k) // k 
    
    print()
