class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxNum = 0
        for sentence in sentences:
            if len(sentence.split(" ")) > maxNum:
                maxNum = len(sentence.split(" "))
        return maxNum