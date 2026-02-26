#runtime:28ms

nums = [0,3,2,5,4,6,1,1]

nums.sort()
print(nums)

count = 1
maxcount = 1
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]-1:
        count += 1
    elif nums[i] == nums[i+1]:
        continue
    else:
        count = 1
    if count > maxcount:
        maxcount = count
print(maxcount)
        