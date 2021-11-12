class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occur = {}
        for num in set(arr):
            occur.setdefault(num, arr.count(num))
        return len(set(occur.values())) == len(occur.values())