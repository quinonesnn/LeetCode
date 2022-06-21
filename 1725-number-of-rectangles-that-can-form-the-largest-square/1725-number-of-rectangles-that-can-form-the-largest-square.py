class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        lengths = []
        for rect in rectangles:
            lengths.append(min(rect))
        return lengths.count(max(lengths))
            