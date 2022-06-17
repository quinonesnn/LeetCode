class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums1:
            if num in nums2 or num in nums3:
                output.append(num)
        
        for num in nums2:
            if num in nums3:
                output.append(num)
        return list(set(output))