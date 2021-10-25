class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #check for the highest in your array
        #check for the highest in your column
        columns = zip(*grid)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                highestRow = max(grid[i])
                highestColumn = max(columns[j])
                while grid[i][j] < highestRow and grid[i][j] < highestColumn:
                    grid[i][j] += 1
                    count += 1
        return count