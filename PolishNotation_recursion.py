# Runtime:29ms

tokens = ["1","2","+","3","*","4","-"]

def RPN():
    token = tokens.pop()
    if token not in "+-*/":
        return int(token)

    right = RPN()
    left = RPN()

    if token == "+":
        return left + right
    if token == "-":
        return left - right
    if token == "*":
        return left * right
    if token == "/":
        return int(left / right)
    
print(RPN())