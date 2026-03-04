heights = [7,1,7,2,2,4]

maxArea = 0
stack = []  # pair: (index, height)

for i, h in enumerate(heights):
    start = i
    while stack and stack[-1][1] > h:
        print("stack1: ", stack)
        index, height = stack.pop()
        print("stack2: ", stack)
        maxArea = max(maxArea, height * (i - index))
        print("maxarea: ",maxArea)
        start = index
    stack.append((start, h))
    print("stack3: ", stack)

for i, h in stack:
    maxArea = max(maxArea, h * (len(heights) - i))
print(maxArea)