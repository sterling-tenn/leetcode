class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # base case, only 1 permutation
        if len(nums) == 1:
            return [nums]
        
        for idx, num in enumerate(nums):
            # decrease the size of nums and find the permutations
            remaining = nums[:idx] + nums[idx + 1:]
            perms = self.permute(remaining)
            
            # attach those permutations associated to the number that was removed
            for perm in perms:
                res.append([num] + perm)
                
        return res # final result