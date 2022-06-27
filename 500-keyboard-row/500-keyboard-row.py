class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        for word in words:
            for row in rows:
                lower = set(word.lower())
                if len(lower) == len(set(row)&lower):
                    output.append(word)
     
        return output