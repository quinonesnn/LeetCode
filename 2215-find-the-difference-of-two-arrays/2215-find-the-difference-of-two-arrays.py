class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = [[],[]]
        for num in (set(nums1) ^ set(nums2)):
            if num in nums1: 
                output[0].append(num)
            else:
                output[1].append(num)
        return output
        