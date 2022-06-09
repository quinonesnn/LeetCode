class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(str(x) for x in digits)) + 1
        string = str(num)
        return [ch for ch in string]
        
        
        