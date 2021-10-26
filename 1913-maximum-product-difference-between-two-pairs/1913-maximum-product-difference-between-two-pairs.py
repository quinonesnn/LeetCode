class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallest = []
        largest =[]
        for i in range(4):
            if i > 1:
                smallest.append(min(nums))
                nums.remove(min(nums))
            else:
                largest.append(max(nums))
                nums.remove(max(nums))
        return (largest[0] * largest[1]) - (smallest[0] * smallest[1])

            