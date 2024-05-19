import random

array = [random.randint(1,100) for i in range(15)]

print(array)

# 1st method
# store=[]
# for i in range(len(array)-1,-1,-1):
#         store.append(array[i])

# 2nd method
# print(array[::-1])

# 3rd method
n = len(array)
j = len(array)-1

for i in range(n//2):
    array[i], array[j] = array[j], array[i]
    j-=1