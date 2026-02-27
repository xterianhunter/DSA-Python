#runtime: 28ms

s = "Was it a car or a cat I saw?"

alnumS = "".join(c for c in s if c.isalnum())
alnumS = alnumS.lower()
print(alnumS)
flag = True

for i in range(len(alnumS)):
    print(f"i: {i}, j:{len(alnumS)-i}")
    # print(f"s[{i}]: {alnumS[i]}, s[{len(alnumS)-i}]: {alnumS[len(alnumS)-1-i]}")
    if alnumS[i] != alnumS[len(alnumS)-1-i]:
        print(f"s[{i}]: {alnumS[i]}, s[{len(alnumS)-i}]: {alnumS[len(alnumS)-1-i]}")
        flag = False
if flag:
    print("is palindrome")
    
    
        