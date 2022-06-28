class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        output = []
        alpha = string.ascii_uppercase
        split = s.split(":")
        startLetter = split[0][0]
        startNum = int(split[0][1])
        endLetter = split[1][0]
        endNum = int(split[1][1])
        for i in range(startNum, endNum + 1):
            for letter in range(ord(startLetter)- 65, ord(endLetter) - 64):
                output.append(alpha[letter] + str(i))
        output.sort()
        return output