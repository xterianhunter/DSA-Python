
heights = [7,1,7,2,2,4]
n = len(heights)

stack = []

leftMost = [-1] * n
for i in range(n):
    while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
    if stack:
        leftMost[i] = stack[-1]
    stack.append(i)
print("leftmost: ",leftMost)


stack = []
rightMost = [n] * n
for i in range(n - 1, -1, -1):
    while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
    if stack:
        rightMost[i] = stack[-1]
    stack.append(i)
print("rightmost: ",rightMost)

maxArea = 0
for i in range(n):
    leftMost[i] += 1
    rightMost[i] -= 1
    maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
print(maxArea)