class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = s.count(s[0])
        for char in set(s):
            if s.count(char) != count:
                return False
        return True