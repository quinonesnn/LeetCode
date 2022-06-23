class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        possible = []
        for char in s:
            if char.islower() and s.find(char.upper()) != -1:
                possible.append(char.upper())
                
        if len(possible) != 0:
            return max(possible)
        else:
            return ""

        