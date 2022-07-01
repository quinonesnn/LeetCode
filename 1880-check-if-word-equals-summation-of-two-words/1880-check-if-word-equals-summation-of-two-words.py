class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        first = ""
        second = ""
        target = ""
        for word in firstWord:
            first += str(ord(word) - 97)
        for word in secondWord:
            second += str(ord(word) - 97)
        for word in targetWord:
            target += str(ord(word) - 97)
        return int(first) + int(second) == int(target)