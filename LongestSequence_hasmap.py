#runtime:30ms

nums = [0,3,2,5,4,6,1,1]

numSet = set(nums)
print(numSet)

longest = 0
for num in nums:
    if (num-1) not in numSet:
        length = 1
        while (num+length) in numSet:
            length += 1
        longest = max (length,longest)
print(longest)