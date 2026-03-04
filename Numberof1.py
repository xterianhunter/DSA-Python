n = 8
res = 0

for i in range(0,32):
    print((1 << i) & n)
    if (1 << i) & n:
        res += 1

print(res)