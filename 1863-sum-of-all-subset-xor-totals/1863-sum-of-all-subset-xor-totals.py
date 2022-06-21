class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumXor = 0
        for num in nums:
            sumXor |= num
        return sumXor * 2 ** (len(nums)-1)