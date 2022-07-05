class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        length = 0
        for word in words:
            if not Counter(word) - Counter(chars):
                length += len(word)
        return length