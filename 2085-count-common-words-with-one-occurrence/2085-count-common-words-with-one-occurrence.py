class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # output = 0
        # print(set(words1))
        # for word in set(words1):
        #     if words1.count(word) == words2.count(word):
        #         output += 1
        # return output
        
        output = 0
        for word in words1:
            if(Counter(words1)[word] == Counter(words2)[word]) and Counter(words2)[word] == 1:
                output += 1
        return output