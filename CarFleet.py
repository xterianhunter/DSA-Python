target = 10
position = [1,4]
speed = [3,2]
print("hii")
pair = [(p, s) for p, s in zip(position, speed)]
pair.sort(reverse=True)
stack = []
for p, s in pair:  # Reverse Sorted Order
    stack.append((target - p) / s)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
print(len(stack))