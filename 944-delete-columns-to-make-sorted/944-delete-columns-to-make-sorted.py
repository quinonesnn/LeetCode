class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        for column in zip(*strs):
            if list(column) != sorted(column):
                count += 1
        return count
        