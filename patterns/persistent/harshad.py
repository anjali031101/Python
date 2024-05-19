def harshad(n):
    sum=0
    st = str(n)
    for i in st:
        sum = sum + int(i)
    if n % sum == 0:
        return True
    else:
        return False

for i in range(1,50):
    # print(i,"is a harshad Number : ",harshad(i))
    print(f"{i} is a harshad number : {harshad(i)}")