class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        split = sentence.split(" ")
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        for i in range(len(split)):
            if split[i][0] in vowels:
                split[i] += "ma"
            if split[i][0] not in vowels:
                split[i] = split[i][1: len(split[i])] + split[i][0] + "ma"
                
            split[i] += ("a" * (i + 1))
        return " ".join(split)