class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        arr = zip(indices, s)
        result = ""
        for tup in sorted(arr):
            result += tup[1]
        return result