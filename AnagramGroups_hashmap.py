# runtime: 44ms

from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

res = defaultdict(list)
for s in strs:
    sortedS = ''.join(sorted(s))
    print(sortedS)
    print(res[sortedS])
    res[sortedS].append(s)
print(list(res.values()))
