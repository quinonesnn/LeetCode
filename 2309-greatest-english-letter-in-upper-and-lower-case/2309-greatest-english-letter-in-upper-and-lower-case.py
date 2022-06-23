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
        print(possible)
        greaterIdx = -1
        for char in possible:
            idx = string.ascii_uppercase.find(char)
            if idx > greaterIdx:
                greaterIdx = idx
                
        if greaterIdx == -1:
            return ""
        else:
            return string.ascii_uppercase[greaterIdx]
        