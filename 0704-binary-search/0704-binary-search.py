class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for idx, num in enumerate(nums):
        if target in nums:
            return nums.index(target)
        return -1
    