class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for idx, num in enumerate(nums):
            nums[idx] = num * num
            
        return sorted(nums)