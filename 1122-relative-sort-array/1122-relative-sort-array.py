class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        extra = []
        for num in arr2:
            for i in range(arr1.count(num)):
                output.append(num)
        for num in arr1:
            if num not in output:
                extra.append(num)
        extra.sort()
        output.extend(extra)
        return output