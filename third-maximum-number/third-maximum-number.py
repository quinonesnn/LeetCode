class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        nums = list(set(nums))
        print(nums)
        if len(nums) >= 3:
            for i in range(2):
                print(max(nums))
                nums.remove(max(nums))
        else:
            return max(nums)
        return max(nums)