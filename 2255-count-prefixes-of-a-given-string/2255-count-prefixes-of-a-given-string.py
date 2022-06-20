class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s) + 1):
            if s[:i] in words:
                count += words.count(s[:i])
        return count