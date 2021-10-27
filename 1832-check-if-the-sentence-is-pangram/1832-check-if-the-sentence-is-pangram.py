class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(string.ascii_lowercase) == len(set(sentence)):
            return True
        else:
            return False