class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        shortest = min(word1, word2, key=len)
        longest = max(word1, word2, key=len)
        for i in range(len(shortest)):
            output += word1[i]
            output += word2[i]
        return output + longest[len(shortest):]