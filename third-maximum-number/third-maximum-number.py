class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        if len(nums) >= 3:
            for i in range(2):
                nums.remove(max(nums))
        else:
            return max(nums)
        return max(nums)