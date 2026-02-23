# runtime 26ms: beats 100%

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
                if (my_dict[num] > 1):
                    return True
            else:
                my_dict[num] = 1
        return False