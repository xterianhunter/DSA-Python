heights = [7,1,7,2,2,4]

area = 0
maxarea = 0
stack = []

for i in range(len(heights)):
    if stack and heights[i]<heights[i-1]:
        stack.append((heights[i],i))


print(maxarea)

