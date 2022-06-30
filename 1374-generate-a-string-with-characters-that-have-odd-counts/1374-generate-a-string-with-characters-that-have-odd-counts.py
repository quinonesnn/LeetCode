class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n % 2 == 0:
            return "".join(['a' for x in range(n - 1)]) + 'b'
        else:
            return "".join(['a' for x in range(n)])