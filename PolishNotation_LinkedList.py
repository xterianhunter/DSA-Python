# Runtime:35ms

tokens = ["1","2","+","3","*","4","-"]

class LinkList:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

head = LinkList(tokens[0])
curr = head

for i in range(len(tokens)):
    curr.next = LinkList(tokens[i], prev=curr)
    curr = curr.next

while head is not None:
    if head.val in "+-*/":
        if head.val == "+":
            head.val = int(head.prev.prev.val) + int(head.prev.val)
        if head.val == "-":
            head.val = int(head.prev.prev.val) - int(head.prev.val)
        if head.val == "*":
            head.val = int(head.prev.prev.val) * int(head.prev.val)
        if head.val == "/":
            head.val = int(int(head.prev.prev.val) / int(head.prev.val))
        head.prev = head.prev.prev.prev
        if head.prev is not None:
            head.prev.next = head
    ans = int(head.val)
    head = head.next
    # print(head.val)
    print(ans)
