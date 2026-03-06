a = 4
b = 7
res = 0
mask = 0xFFFFFFFF

carry = 0
for i in range(32):
    a_bit = (a >> i) & 1
    b_bit = (b >> i) & 1
    cur_bit = a_bit ^ b_bit ^ carry
    carry = (a_bit + b_bit + carry) >= 2
    if cur_bit:
        res |= 1 << i

if res > 0x7FFFFFFF:
    res = ~(res ^ mask)

print(res)
