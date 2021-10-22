class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(nums)- 1, 2):
            arr = [nums[i+1]] * nums[i]
            result += arr
        return(result)