class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = {'a','e','i','o','u'}
        first = s[:len(s)/2]
        last = s[len(s)/2:]
        firstCount = 0
        lastCount = 0
        for vowel in vowels:
            firstCount += first.count(vowel)
            firstCount += first.count(vowel.upper())
            lastCount += last.count(vowel)
            lastCount += last.count(vowel.upper())
        if firstCount == lastCount:
            return True
        return False