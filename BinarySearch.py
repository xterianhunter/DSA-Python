nums = [-1,0,2,4,6,8]
target = 4

l,r = 0, len(nums)-1

while l<r:
    mid = int(l + (r-l)/2)
    print("nums: ", nums[mid])
    if target == nums[mid]:
        print("else")
        print(mid)
        break
    if target < nums[mid]:
        r = mid - 1
        print("if")
    elif target > nums[mid]:
        print("elif")
        l = mid+1
    # else:
    #     print("else")
    #     print(nums[mid])
    #     break
print(-1)
