#runtime: 27ms

s = "Was it a car or a cat I saw?"

alnumS = "".join(c for c in s if c.isalnum())
alnumS = alnumS.lower()
print(alnumS)
flag = True

l = 0
r = len(alnumS)-1

while l < r:
    print(f"l: {l}, r:{r}")
    # print(f"s[{i}]: {alnumS[i]}, s[{len(alnumS)-i}]: {alnumS[len(alnumS)-1-i]}")
    if alnumS[l] != alnumS[r]:
        print(f"s[{l}]: {alnumS[l]}, s[{r}]: {alnumS[r]}")
        flag = False
        if not flag:
            break
    l , r = l + 1, r - 1
if flag:
    print("is palindrome")
    
    
        