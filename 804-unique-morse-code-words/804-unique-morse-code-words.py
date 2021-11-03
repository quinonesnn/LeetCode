class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        transformations = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
                 "-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            concat = ""
            for char in word:
                concat += morse[string.ascii_lowercase.find(char)]
            if concat not in transformations:
                transformations.append(concat)
        return len(transformations)
        