class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxUntilNow = [0] * len(nums)
        maxUntilNow[0] = nums[0]
        maximum = nums[0]
        
        for i in range(1, len(nums)):
            maxUntilNow[i] = max(nums[i], maxUntilNow[i - 1] + nums[i])
            maximum = max(maximum, maxUntilNow[i])
        return maximum