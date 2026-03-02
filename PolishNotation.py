# runtime:29ms
tokens = ["1","2","+","3","*","4","-"]

operator = ["+","-","*","/"]
stack = []


for token in tokens:
    if token in operator:
        temp = int(stack.pop())
        if token == "+":
            stack.append(int(stack.pop()) + temp)
        if token == "*":
            stack.append(int(stack.pop()) * temp)
        if token == "-":
            stack.append(int(stack.pop()) - temp)
        if token == "/":
            stack.append(int(stack.pop()) / temp)
    else:
        stack.append(int(token))

print(int(stack.pop()))
