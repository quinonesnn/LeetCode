class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        for string in arr:
            if arr.count(string) == 1:
                k -= 1
                if k == 0:
                    return string
        return ""