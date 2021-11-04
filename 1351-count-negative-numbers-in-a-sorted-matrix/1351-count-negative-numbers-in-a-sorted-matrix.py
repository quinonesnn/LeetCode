class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        for nums in grid:
            for num in nums:
                if num < 0:
                    output += 1
        return output