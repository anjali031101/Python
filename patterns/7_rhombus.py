"""
n = 5
pattern = "* * * * *"
for i in range(n):
    print(" "*i,end=" ")
    print(pattern)
"""

n = 7

for i in range(n):
    print(" "*i,end=" ")
    for j in range(n):
        print("*",end=" ")
    print()