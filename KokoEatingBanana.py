import math
piles = [1,4,3,2]
h = 9
# piles = [25,10,11,4]
# h = 6


l,r = 1, max(piles)
curr_h = 0
res =0
# print(int(l + (r-l) // 2))

while l<=r:
    mid = int(l + (r-l) // 2)
    curr_h = 0
    for pile in piles:
        curr_h += math.ceil(pile/mid)
    if curr_h <= h :
        res = mid
        r = mid - 1
    else:
        l = mid + 1

    # print("mid: ", mid)
    # print("curr_h: ",curr_h)
print(res)

