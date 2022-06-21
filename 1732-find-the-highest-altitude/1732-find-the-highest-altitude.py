class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        count = 0
        for step in gain:
            count += step
            if count > highest:
                highest = count
        return highest