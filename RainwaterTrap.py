# runtime: 27ms

# height = [0,2,0,3,1,0,1,3,2,1]
height = [0,1,0,2,1,0,1,3,2,1,2,1]

water = 0

prefix = []
suffix = [0]*len(height)
maxH = 0

for i in range(len(height)):
    maxH = max(maxH,height[i])
    prefix.append(maxH)


maxH = 0
# print(maxH)
for i in range(len(height)-1,-1,-1):
    maxH = max(maxH,height[i])
    suffix[i] = maxH

for i in range(len(height)):
    water += min(prefix[i],suffix[i]) - height[i]

print(prefix)
print(suffix)
print(water)
