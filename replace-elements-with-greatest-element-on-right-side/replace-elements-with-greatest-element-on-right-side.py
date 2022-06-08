class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output = []
        if (len(arr) == 1):
            return [-1]
        for i in range(1, len(arr)):
            output.append(max(arr[i:]))
        output.append(-1)
        return output
            