nums = [0,1,2,3,5,6]
nums.sort()
n = len(nums)

if nums[0] != 0:
    print(0)

sum = 0
for num in nums:
    sum += num

print(sum)

print( int((n*(n+1))/2)-sum )