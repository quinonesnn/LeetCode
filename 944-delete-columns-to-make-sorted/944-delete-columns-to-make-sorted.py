class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        columns = list(zip(*strs))
        for column in columns:
            for i in range(len(column) - 1):
                if column[i] > column[i + 1]:
                    count += 1
                    break
        return count
        