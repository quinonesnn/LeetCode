class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis1 = [None]
        for i in s:
            if lis1[-1] == i:
                lis1.pop()
            else:
                lis1.append(i)
        return ''.join(lis1[1:])