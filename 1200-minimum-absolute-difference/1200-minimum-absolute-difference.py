class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        output = []
        arr.sort()
        minAbs = sys.maxint
        for i in range(len(arr) - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff < minAbs:
                minAbs = diff
        
        for j in range(len(arr) - 1):
            if abs(arr[j] - arr[j + 1]) == minAbs:
                output.append([arr[j], arr[j + 1]])
        return output