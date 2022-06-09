class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0 and sum(nums[i+1:]) == 0:
                return i
            if i == len(nums) and sum(nums[:i]) == 0:
                return i
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1