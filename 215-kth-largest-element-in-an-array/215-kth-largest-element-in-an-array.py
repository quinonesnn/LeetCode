class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        largest = 0
        for i in range(k):
            largest = max(nums)
            nums.remove(largest)
        return largest
            