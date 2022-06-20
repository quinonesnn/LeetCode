class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        t = collections.Counter(target)
        a = collections.Counter(arr)
        return t==a
            