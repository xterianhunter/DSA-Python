#runtime: 44ms

height = [1,7,2,5,4,7,3,6]

l,r = 0, len(height)-1

maxwater,currwater = 0,0

while l<r:
    currwater = min(height[l],height[r])*(r-l)
    if height[l] < height[r]:
        l = l+1
    else:
        r = r-1

    maxwater = max(currwater,maxwater)

print(maxwater)
    
