class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        nums.sort()
        for i in range (len(nums)):
            if nums[i] == target:
                output.append(i)
        return output