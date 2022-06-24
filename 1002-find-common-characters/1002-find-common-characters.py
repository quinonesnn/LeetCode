class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s = set(words[0])
        l = []
        for i in range(1,len(words)):
            s = s&set(words[i])
        for j in s:
            smallest = min([k.count(j) for k in words])
            l.extend(j*smallest)
        return l