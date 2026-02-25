# runtime: 27ms

nums = [1,2,2,3,3,3]
k = 2

dict = {}
for num in nums:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
print(sorted(dict, key = dict.get, reverse = True)[:k])