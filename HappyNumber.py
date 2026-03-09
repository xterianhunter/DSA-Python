def helperFun(n):
    sum = 0
    while n:

        # print("n: ",n)
        sum += (n%10)**2
        # print("sum: ",sum)
        n = n // 10
    return sum

n = 101
# print(helperFun(n))
dict= {}
flag = True

while True:
    n = helperFun(n)
    print(n)
    if n == 1:
        break
    else:
        if n not in dict:
            dict[n] = 1
        else:
            flag = False
            break