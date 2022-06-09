class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                for j in range(i, len(nums)):
                    if nums[j] % 2 == 0:
                        odd = nums[i]
                        nums[i] = nums[j]
                        nums[j] = odd                        
        return nums
                        