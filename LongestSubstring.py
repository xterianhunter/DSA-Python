# s = "zxyzxyz"
s="abcabcbb"

maxcount,count = 0,1
i,j = 0,1


while i < len(s)-1 and j < len(s):
    if s[i] == s[j]:
        i = i+1
        count = 1
        j = i+1
    else:
        count += 1
        j = j+1
    
    maxcount = max(maxcount,count)      

print(maxcount)
            