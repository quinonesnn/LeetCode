class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        result = []
        for char in address:
            if char == ".":
                result.append("[.]")
            else:
                result.append(char)
        return "".join(result)