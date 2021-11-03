class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        alphabet = string.ascii_lowercase
        slist = list(s)
        for i in range(0, len(s) -1, 2):
            idx = alphabet.find(slist[i]) + int(slist[i+1])
            print(idx)
            slist[i+1] = alphabet[idx]
        return "".join(slist)
            