# runtime: 27ms
temperatures = [30,38,30,36,35,40,28]

stack = []
res = [0]*len(temperatures)

for i,temperature in enumerate(temperatures):
    while stack and temperature > stack[-1][0]:
        stackT,stackInd = stack.pop()
        res[stackInd] = i-stackInd
    stack.append((temperature,i))

print(res)