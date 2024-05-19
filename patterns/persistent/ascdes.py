import random

array = [random.randint(1,100) for i in range(15)]
print(array)
ar= sorted(array)
print(ar)
for i in range(len(array)//2):
    print(array[i],end =" ")
for j in range(len(array)-1,len(array)//2-1,-1):
    print(array[j],end=" ")
    
print()
print()

 
    
#method2

    
    
import random

array = [random.randint(1, 100) for i in range(15)]
print("Original array:", array)

# Split the array into two halves
mid_point = len(array) // 2

# Sort the first half in ascending order
first_half = sorted(array[:mid_point])

# Sort the second half in descending order
second_half = sorted(array[mid_point:], reverse=True)

# Concatenate the two halves
sorted_array = first_half + second_half

print("Sorted array:", sorted_array)

