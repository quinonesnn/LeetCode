class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for num in nums:
            if nums.count(num) % 2 != 0:
                return False
        return True