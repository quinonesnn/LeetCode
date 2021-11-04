class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        split = s.split()
        for string in split:
            arr =[]
            arr[:0] = string
            arr.reverse()
            result =""
            output.append(result.join(arr))
        return " ".join(output)
