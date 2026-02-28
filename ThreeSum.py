#runtime: 33ms

nums = [-1,0,1,2,-1,-4]

target0 = 0
nums.sort()
res = []
for i in range(len(nums)-2):
    if nums[i]>0:
        break
    l,r = i+1,len(nums)-1
    target = target0 - nums[i]
    while l<r:
        if nums[l]+nums[r] > target:
            r = r-1
        elif nums[l]+nums[r] < target:
            l = l+1
        elif nums[i] + nums[l] + nums[r] == target0:
            List = [nums[i],nums[l],nums[r]]
            if list not in res:
                res.append(List)
            l,r = l+1,r-1
print(res)