class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        output = 0
        for word in set(words1):
            if words1.count(word) == words2.count(word) and words1.count(word) == 1:
                output += 1
        return output
        