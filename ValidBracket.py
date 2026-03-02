# runtime: 27ms

# s = "([{}])"
# s = "[(])"
s="]"

stack = []
opening = "({["
# closing = 

flag = True
for i in range(len(s)):
    print("Begin: ", stack)
    if s[0] not in opening:
        flag = False
        break
    if s[i] in opening:
        stack.append(s[i])
    elif stack[-1] == '{' and s[i] == '}':
        stack.pop()
    elif stack[-1] == '(' and s[i] == ')':
        stack.pop()
    elif stack[-1] == '[' and s[i] == ']':
        stack.pop()
    else:
        flag = False
    print("End: ", stack)
    print(s[i])
if len(stack) != 0:
    flag = False
print(flag)