
# s = "([{}])"
# s = "[(])"
s="]"

flag  = True
stack = []
closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

for c in s:
    if c in closeToOpen:
        if stack and stack[-1] == closeToOpen[c]:
            stack.pop()
        else:
            flag =  False
    else:
        stack.append(c)

if not stack:
    flag = False
    
print(flag)