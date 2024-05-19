a = [10, 89, 9, 56, 4, 80, 8]
min_element = a[0]
for i in range(len(a)):
        
        if a[i] < min_element:
            min_element = a[i]

print (min_element)

#method 2
a = [10, 89, 9, 56, 4, 80, 8]
a.sort()

print (a[0])


#method 3
arr = [10, 89, 9, 56, 4, 80, 8]
print (min(arr))



