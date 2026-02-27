#runtime:27ms

num = [1,2,3,5]
target = 7

l,r = 0,len(num)-1

while l<r:
    if num[l]+num[r] > target:
        r = r-1
    if num[l]+num[r] < target:
        l = l+1
    if num[l]+num[r] == target:
        list = [l,r]
        print(list)
        break
    
    