class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        output = set(nums[0])
        for arr in nums:
            output = output & set(arr)
            
        output = list(output)
        output.sort()
        return output