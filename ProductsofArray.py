#runtime:27ms

nums = [-1,0,1,2,3]

suffix = [1]*len(nums)
prefix = [1]*len(nums)
nlist = []
for i in range(len(nums)-1):
    prefix[i+1] = nums[i]*prefix[i]
for i in range(len(nums)-1,0,-1):
    suffix[i-1] = nums[i]*suffix[i]
for i in range(len(nums)):
    nlist.append(suffix[i]*prefix[i])
print(nlist)