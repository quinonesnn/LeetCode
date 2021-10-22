class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        add = 0
        mult = 1
        
        for char in str(n):
            add += int(char)
            mult *= int(char)
        return mult - add