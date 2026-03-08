nums1 = [1,3]
nums2 = [2,4]

i = j = 0
median1 = median2 = 0

for count in range((len(nums1) + len(nums2))//2 + 1):
    median2 = median1
    if i<len(nums1) and j<len(nums2):
        if nums1[i] > nums2[j]:
            median1= nums2[j]
            j += 1
        else:
            median1 = nums1[i]
            i += 1
    elif i<len(nums1):
        median1 = nums1[i]
        i += 1
    else:
        median1 = nums2[j]
        j += 1

if (len(nums1)+len(nums2)) % 2 == 0:
    print((median1+median2) / 2.0)

print(median1)