class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if arr.count(0) > 1:
            return True
        for num in arr:
            if num != 0 and num + num in arr:
                return True
        return False