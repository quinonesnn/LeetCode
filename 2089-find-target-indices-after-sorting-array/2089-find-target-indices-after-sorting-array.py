class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        nums.sort()
        occurs = nums.count(target)
        start = 0
        for i in range(occurs):
            idx = nums.index(target, start)
            output.append(idx)
            if idx != len(nums):
                start = idx + 1 
        return output