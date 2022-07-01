class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        idx = s.find("b")
        if idx == -1:
            return True
        if "a" in s[idx:]:
            return False
        return True