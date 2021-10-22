class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = max(candies)
        result = []
        for amount in candies:
            if amount + extraCandies >= largest:
                result.append(True)
            else:
                result.append(False)
        return result