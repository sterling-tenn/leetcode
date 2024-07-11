class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        res = []
        for idx, num in enumerate(nums):
            remaining = nums[:idx] + nums[idx+1:]
            
            perms = self.permute(remaining)
            for perm in perms:
                res.append([num] + perm)
        return res