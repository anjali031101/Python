import random

a=[random.randint(1,100) for i in range(10)]
su=0
for i in range(len(a)):
    su += a[i]
    
# print(sum(a))
print(su)