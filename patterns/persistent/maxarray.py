a = [10, 89, 9, 56, 4, 80, 8]
max_element = a[0]
for i in range(len(a)):
        
        if a[i] > max_element:
            max_element = a[i]

print (max_element)

#method 2
a = [10, 89, 9, 56, 4, 80, 8]
a.sort()

print (a[-1])


#method 3
arr = [10, 89, 9, 56, 4, 80, 8]
print (max(arr))





