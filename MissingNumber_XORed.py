nums = [0,1,2,3,5,6]
n = len(nums)

xor = 0
for i in range(n+1):
    xor = xor ^ i
# print(xor)

for num in nums:
    xor = xor ^ num

print(xor)