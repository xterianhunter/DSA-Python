nums = [3,4,5,6,1,2]

l,r = 0, len(nums)-1

min_ele = float('inf')

while l <= r:
    mid = int(l + (r-l)//2)
    if nums[r] < nums[mid]:
        l = mid + 1
    else:
        r = mid - 1
    min_ele = min(min_ele,nums[mid])

print(min_ele)