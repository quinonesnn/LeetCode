class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for string in operations:
            if "+" in string:
                x += 1
            else:
                x -= 1
        return x